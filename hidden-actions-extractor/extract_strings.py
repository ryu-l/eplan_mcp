"""
从 EPLAN Bin 目录的 .NET DLL 中离线提取动作名(Python 版,方法3交叉验证工具)。

与 extract_actions.ps1 互为补充:
  - PS 版用反射读类名和注册属性(准,但需要 Windows);
  - 本脚本直接解析 CLR 元数据的 #Strings / #US 堆 + 原始 UTF-16 扫描(可在任意
    系统运行,包括 macOS/Linux,只需把 Bin 目录拷过来)。

原理:.NET 程序集(PE 文件)里有一块 CLR 元数据区,类型名、成员名、字符串字面量
分别存在 #Strings(UTF-8)和 #US(UTF-16LE)堆里。动作名要么是类名,要么是注册
属性里的字符串字面量,两者都能从这两个堆里捞出来。

依赖:仅 Python 3.8+ 标准库(无第三方包)。

用法:
  python extract_strings.py <Bin目录或DLL路径> [输出目录]
  例: python extract_strings.py "C:/Program Files/EPLAN/Electric P8/2.9.4/Bin" output
"""
import os
import re
import struct
import sys

# ---- 动作名形态过滤 -------------------------------------------------------
JUNK = {
    "system", "microsoft", "windows", "nullable", "object", "string",
    "int", "void", "boolean", "exception", "eventargs", "attribute",
    "get", "set", "action", "version", "culture", "publickeytoken",
}
NAME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]{2,79}$")


def is_action_name(s):
    if not NAME_RE.match(s):
        return False
    if s.lower() in JUNK:
        return False
    # 动作样式:Action 后缀 / X 前缀家族 / 全小写动作词(如 gedRedraw 会被 X 规则漏掉,
    # 但 gedRedraw 是驼峰,归入下面规则) —— 放宽为:含大写字母或全小写
    if s.endswith("Action") or re.match(r"^X[A-Z][A-Za-z0-9]+$", s) or s == s.lower():
        return True
    # 驼峰混合(gedRedraw、exportToGraphics 这类)
    if re.search(r"^[a-z]+[A-Z]", s) or re.search(r"[a-z][A-Z][a-z]", s):
        return True
    return False


# ---- PE / CLR 解析 --------------------------------------------------------
def rva_to_offset(sections, rva):
    for name, va, vsize, raw, rawsize in sections:
        if va <= rva < va + max(vsize, rawsize):
            return raw + (rva - va)
    return None


def parse_pe(data):
    """返回 (cli_header_offset, sections);解析失败返回 (None, [])"""
    if data[:2] != b"MZ":
        return None, []
    e_lfanew = struct.unpack_from("<I", data, 0x3C)[0]
    if data[e_lfanew:e_lfanew + 4] != b"PE\x00\x00":
        return None, []
    coff = e_lfanew + 4
    num_sections = struct.unpack_from("<H", data, coff + 2)[0]
    opt_size = struct.unpack_from("<H", data, coff + 16)[0]
    opt = coff + 20
    magic = struct.unpack_from("<H", data, opt)[0]
    if magic == 0x10B:      # PE32
        dd_rva = opt + 96
    elif magic == 0x20B:    # PE32+
        dd_rva = opt + 112
    else:
        return None, []
    cli_rva, cli_size = struct.unpack_from("<II", data, dd_rva + 14 * 8)
    if cli_rva == 0 or cli_size == 0:
        return None, []
    sections = []
    sec = opt + opt_size
    for _ in range(num_sections):
        name = data[sec:sec + 8].rstrip(b"\x00").decode("ascii", "replace")
        vsize, va, rawsize, raw = struct.unpack_from("<IIII", data, sec + 8)
        sections.append((name, va, vsize, raw, rawsize))
        sec += 40
    off = rva_to_offset(sections, cli_rva)
    if off is None:
        return None, sections
    return off, sections


def parse_metadata(data, cli_off, sections):
    """解析 CLR 头 -> 元数据根 -> 提取 #Strings(UTF-8)和 #US(UTF-16LE)堆内容"""
    cb = struct.unpack_from("<I", data, cli_off)[0]
    md_rva, md_size = struct.unpack_from("<II", data, cli_off + 8)
    off = rva_to_offset(sections, md_rva)
    if off is None:
        return b"", b""
    if data[off:off + 4] != b"BSJB":
        return b"", b""
    ver_len = struct.unpack_from("<I", data, off + 12)[0]
    pos = off + 16 + ver_len
    pos += 2  # flags
    num_streams = struct.unpack_from("<H", data, pos)[0]
    pos += 2
    strings_heap, us_heap = b"", b""
    for _ in range(num_streams):
        stream_off, stream_size = struct.unpack_from("<II", data, pos)
        pos += 8
        name_end = data.index(b"\x00", pos)
        stream_name = data[pos:name_end].decode("ascii", "replace")
        pos = name_end + 1
        pos = (pos + 3) & ~3  # 4 字节对齐
        start = off + stream_off
        chunk = data[start:start + stream_size]
        if stream_name == "#Strings":
            strings_heap = chunk
        elif stream_name == "#US":
            us_heap = chunk
    return strings_heap, us_heap


def scan_file(path):
    """从一个 DLL 里提取候选动作名集合"""
    data = open(path, "rb").read()
    found = set()

    # 通道1: CLR 元数据堆(#Strings 里的类型/成员名 + #US 里的字符串字面量)
    try:
        cli_off, sections = parse_pe(data)
        if cli_off is not None:
            strings_heap, us_heap = parse_metadata(data, cli_off, sections)
            # #Strings: null 分隔的 UTF-8
            for s in strings_heap.split(b"\x00"):
                t = s.decode("utf-8", "ignore")
                if is_action_name(t):
                    found.add(t)
            # #US: 压缩长度前缀 + UTF-16LE;用正则粗扫
            for m in re.finditer(rb"(?:[\x20-\x7E]\x00){4,}", us_heap):
                t = m.group(0).decode("utf-16-le", "ignore")
                if is_action_name(t):
                    found.add(t)
    except Exception:
        pass

    # 通道2: 全文件 UTF-16LE 字符串扫描(兜底)
    for m in re.finditer(rb"(?:[\x20-\x7E]\x00){4,}", data):
        t = m.group(0).decode("utf-16-le", "ignore")
        if is_action_name(t):
            found.add(t)
    return found


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    target = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "output"
    os.makedirs(out_dir, exist_ok=True)

    if os.path.isdir(target):
        dlls = sorted(
            os.path.join(target, f)
            for f in os.listdir(target)
            if f.lower().endswith(".dll")
        )
    else:
        dlls = [target]
    print(f"扫描 {len(dlls)} 个 DLL ...")

    all_names = set()
    for i, dll in enumerate(dlls, 1):
        try:
            names = scan_file(dll)
            all_names.update(names)
            print(f"  [{i}/{len(dlls)}] {os.path.basename(dll)}: {len(names)} 个候选")
        except Exception as exc:
            print(f"  [{i}/{len(dlls)}] {os.path.basename(dll)}: 失败 ({exc})")

    out_txt = os.path.join(out_dir, "action_candidates.txt")
    with open(out_txt, "w", encoding="utf-8") as fh:
        fh.write("\n".join(sorted(all_names)) + "\n")
    print(f"\n完成: 共 {len(all_names)} 个候选动作名 -> {out_txt}")
    print("下一步: python probe_eplan_pages.py " + out_txt)


if __name__ == "__main__":
    main()
