# EPLAN 隐藏动作提取工具(方法 3:离线 DLL 分析)

针对 **EPLAN Electric P8 2.9** 设计(2022/2024/2025/2026 版同样适用)。

## 原理

EPLAN 的动作是 .NET 类,动作名字符串(如 `gedRedraw`、`XEsGetProjectPropertyAction`)
以**类名**和**注册属性字符串**的形式存在于安装目录 `Bin` 文件夹的 DLL 元数据中。
本工具**不需要运行 EPLAN、不需要授权**——只要拿到 DLL 文件,就能把动作名单离线提取出来。

提取后分两类变现:
1. **官网有对应文档页**的动作 → 抓页面入库(数据最完整);
2. **官网无页面的动作**(真"隐藏")→ 用 DLL 属性里的信息手工建档。

## 文件说明

| 文件 | 作用 | 依赖 |
|---|---|---|
| `extract_actions.ps1` | 主提取器:反射读类名 + 注册属性 + UTF-16 字符串扫描 | 仅 Windows PowerShell 5.1(系统自带) |
| `extract_strings.py` | 交叉验证提取器:解析 CLR 元数据堆(#Strings/#US)+ UTF-16 扫描,可在任意系统跑(把 Bin 拷到 Mac 上也能用) | 仅 Python 3.8+ 标准库 |
| `probe_eplan_pages.py` | 用候选名探测 eplan.help,区分"有官方页/真隐藏" | 仅 Python 3.8+ 标准库,需联网 |

## 使用步骤(在 Windows 机器上)

### 第 1 步:定位 Bin 目录

EPLAN Electric P8 2.9 默认安装位置:

```
C:\Program Files\EPLAN\Electric P8\2.9.4\Bin        # 或 2.9.0 / 2.9 SP1 等版本目录
C:\Program Files\EPLAN\Platform\2.9.4\Bin           # 部分安装是 Platform 结构
```

脚本会自动查找;找不到时用 `-BinPath` 手动指定。**只需要读权限**,把整个 Bin 目录
拷到任何机器(包括 Mac)上也能跑 Python 提取器。

### 第 2 步:运行 PowerShell 提取器(零依赖)

在 PowerShell 中:

```powershell
powershell -ExecutionPolicy Bypass -File extract_actions.ps1
# 或手动指定目录:
powershell -ExecutionPolicy Bypass -File extract_actions.ps1 -BinPath "C:\Program Files\EPLAN\Electric P8\2.9.4\Bin" -OutDir ".\output"
```

输出:
- `output/action_candidates.txt` —— 去重后的候选动作名单(预计几百~上千个);
- `output/action_details.json` —— 每个候选名的来源 DLL、来源类型(typename / attribute / utf16string)、所在类型与注册属性名。

### 第 3 步(可选):Python 交叉验证

```bash
python extract_strings.py "C:\Program Files\EPLAN\Electric P8\2.9.4\Bin" output
```

两版取并集,可互相弥补:PS 反射版更准(真实元数据),Python 版能发现更多字符串字面量。

### 第 4 步:探测官网,区分"有页/真隐藏"

```bash
python probe_eplan_pages.py output\action_candidates.txt output
```

输出:
- `output/found_pages.txt` —— 格式 `动作名 <TAB> 有页面的版本列表 <TAB> 首个URL`,
  这些 URL 交给 `../rebuild/crawl.py` 的抓取流程入库;
- `output/missing.txt` —— 全部版本都无页面的动作,即真"隐藏动作"。

### 第 5 步:入库

`found_pages.txt` 里的页面用仓库已有的 `rebuild/` 流程抓取并重建索引;
`missing.txt` 里的动作名配合 `action_details.json`(注册属性里的参数信息)手工整理
成 markdown 后一并入库。

## 常见问题

**Q: PowerShell 报"无法加载文件,因为在此系统上禁止运行脚本"?**
A: 用 `-ExecutionPolicy Bypass` 参数(见上),或先执行
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`。

**Q: 提示找不到 Bin 目录?**
A: 确认 EPLAN 装的是 "Electric P8" 产品(不是 "Fluid" 等);或手动 `-BinPath`。
2.9 各 SP 版本目录名不同(2.9.0 / 2.9.4 等),脚本按 `2.*` 通配查找。

**Q: 输出名单里有大量噪音?**
A: 正常。脚本故意放宽过滤(宁多勿漏)。`probe_eplan_pages.py` 会自然淘汰噪音
(噪音名在官网不会有页面)。若噪音过多,可用已知动作名(官方 60 个 + 指南
availableactions 页 + 仓库源码 Execute 调用)做白名单交集。

**Q: 2.9 的文档在哪个 api 版本?**
A: 探测脚本覆盖 `2.9 / 2022 / 2023 / 2024 / 2025 / 2026` 全部版本,有页即记。

## ⚠️ 法律提示

本工具本质是对 EPLAN 商业软件二进制做**逆向工程**。绝大多数软件许可协议
(包括 EPLAN 的 EULA)禁止 reverse engineering。请仅用于**个人学习研究**,
不要把提取结果公开发布或用于商业用途,也不要分发 EPLAN 的 DLL 文件。
更"干净"的替代方案是方案 1/2(在授权安装上用公开 API 探测),参见主仓库
调研结论。
