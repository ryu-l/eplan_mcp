"""
用候选动作名探测 eplan.help,找哪些动作有官方文档页(方法3的"变现"步骤)。

对每个候选名,尝试访问 https://www.eplan.help/en-us/Infoportal/Content/api/<版本>/<名字>.html
(P8 2.9 时代的文档对应 api/2.9 或 api/2022;同时探测 2023~2026 各版本,有页即记录)。

输出:
  found_pages.txt  存在官方页面的动作(可直接交给 rebuild/crawl.py 抓取)
  missing.txt      全部版本都没有页面的动作(真"隐藏",需靠 DLL 属性/方案1补参数说明)

依赖:仅 Python 3.8+ 标准库。限速并发 6,请勿调大。

用法: python probe_eplan_pages.py [候选名单txt] [输出目录]
"""
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = "https://www.eplan.help/en-us/Infoportal/Content/api"
# P8 2.9 的文档在 2.9 / 2022 下;新版本逐年。全部探测,互相印证。
VERSIONS = ["2.9", "2022", "2023", "2024", "2025", "2026"]
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
}


def check(name, version):
    url = f"{BASE}/{version}/{name}.html"
    req = urllib.request.Request(url, headers=HEADERS, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status == 200:
                return name, version, url
    except urllib.error.HTTPError as exc:
        if exc.code in (405, 501):  # 服务器不支持 HEAD,换 GET 试一次
            try:
                req2 = urllib.request.Request(url, headers=HEADERS)
                with urllib.request.urlopen(req2, timeout=15) as resp:
                    if resp.status == 200:
                        return name, version, url
            except urllib.error.HTTPError:
                pass
    except Exception:
        pass
    return None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    names_file = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(names_file))
    names = sorted({l.strip() for l in open(names_file, encoding="utf-8") if l.strip()})
    print(f"候选动作名: {len(names)} 个,版本: {VERSIONS}")

    tasks = [(n, v) for n in names for v in VERSIONS]
    found, missing = {}, set(names)
    done = 0
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = [pool.submit(check, n, v) for n, v in tasks]
        for f in futures:
            r = f.result()
            done += 1
            if done % 500 == 0:
                print(f"  进度 {done}/{len(tasks)} ...")
            if r:
                name, version, url = r
                found.setdefault(name, []).append((version, url))
                missing.discard(name)
            time.sleep(0.02)

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "found_pages.txt"), "w", encoding="utf-8") as fh:
        for name in sorted(found):
            versions = ", ".join(v for v, _ in found[name])
            first_url = found[name][0][1]
            fh.write(f"{name}\t{versions}\t{first_url}\n")
    with open(os.path.join(out_dir, "missing.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(sorted(missing)) + "\n")

    print(f"\n完成:")
    print(f"  有官方页面的动作: {len(found)} 个 -> {os.path.join(out_dir, 'found_pages.txt')}")
    print(f"  无页面(真隐藏):   {len(missing)} 个 -> {os.path.join(out_dir, 'missing.txt')}")
    print("下一步: found_pages.txt 里的 URL 可交给 ../rebuild/crawl.py 的抓取流程入库;")


if __name__ == "__main__":
    main()
