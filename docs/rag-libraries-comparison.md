# EPLAN RAG:官方线上库 vs 本地自建库 —— 完整对比与使用说明

> 本文档基于 2026-08-20 ~ 2026-08-22 的完整调研、构建与实测过程编写。
> 所有数据均来自真实抓取、真实查询,非估算(推断处已标注)。

---

## 目录

1. [背景](#1-背景)
2. [官方线上库](#2-官方线上库)
3. [本地自建库](#3-本地自建库)
4. [内容差别对照](#4-内容差别对照)
5. [效果差别(实测)](#5-效果差别实测)
6. [使用指南](#6-使用指南)
7. [已知差距与补齐路径](#7-已知差距与补齐路径)
8. [维护与更新](#8-维护与更新)
9. [构建过程中的关键技术结论](#9-构建过程中的关键技术结论)
10. [附录:文件结构与工具清单](#10-附录文件结构与工具清单)

---

## 1. 背景

本项目([covagashi/eplan-rag-mcp](https://github.com/covagashi/eplan-rag-mcp))包含**两条相互独立的
远程 RAG 服务**(外加一个本地 EPLAN 控制 MCP server):

- **P8 文档 RAG**:`https://rag2026.covaga.xyz`(Cloudflare Worker + Vectorize 索引
  `eplan-knowledge-base`),数据源为作者本机构建的 ChromaDB
  `eplan-p8-mcp-server/chroma_db_sota`(已随 `.gitignore` 排除,不在仓库中);
- **EEC Pro 2026 文档 RAG**:`https://rageecpro.covaga.xyz`(独立 Worker + 独立索引
  `eecpro-knowledge-base`),数据源为 `eplan-eecpro-rag-builder/rag_db_llama_chroma`
  (builder 仓库同样未公开)。

由于数据库本体不可获取(不在 GitHub、不在我们账户的 Cloudflare、原始 Windows 机器不可达),
我们采取**从公开文档重建**的方式,在本机构建了等价(部分超出)的本地库,并做了逐项对比实测。

---

## 2. 官方线上库(两条独立服务)

### 2.1 P8 文档 RAG(`rag2026.covaga.xyz`)

| 组件 | 内容 |
|---|---|
| 部署形态 | Cloudflare Workers(worker 源码在仓库 `cloudflare-rag-eplan-p8/worker/src/index.ts`) |
| 向量索引 | Cloudflare Vectorize,索引名 `eplan-knowledge-base` |
| 嵌入模型 | `@cf/baai/bge-base-en-v1.5`(768 维,cosine) |
| 向量规模 | **55,000 条**(README 写的 57,492 为旧数字;`/stats` 实测 55,000) |
| 构建时间 | `processedUpToDatetime: 2026-03-27`(索引数据截止时间) |
| 接口 | MCP(`POST /mcp`,工具 `eplan_search`/`eplan_stats`)+ REST(`GET /health`、`POST /search`、`GET /stats`、`POST /add-vectors`) |
| 访问控制 | `/search`、`/mcp` 公开无鉴权;仅 `/add-vectors` 有 `WORKER_API_KEY` 保护 |

**数据来源与版本(实测结论,仅针对本服务):**

- **文档版本:仅 api/2026(2026 版)**。至今所有探针(~10 组查询、50+ 条结果)的 `source_url`
  **100% 指向 `/Content/api/2026/`**,从未出现 2025/2024/2.9 等旧版 URL;索引构建时间
  (2026-03)与 wrangler 配置 `compatibility_date: 2026-03-23` 互相印证。
- **"三个类别"实为同一文档集内的三本书**:worker 的 `category` 枚举
  `["API Reference", "User Guide", "Api"]` 对应 api/2026 帮助系统内部的书结构
  (面包屑实测:`Eplan API / API Reference / ...`、`Eplan API / User Guide / API DataModel / ...`)。
  用产品指南味十足的关键词("Backstage view"、"graphical editor"等)查询,线上**零次**返回
  Plattform 产品指南(`/Content/Plattform/`)URL → **P8 服务大概率不包含 EPLAN 平台产品用户指南**。
- **hidden actions**:作者 README 声称索引含"隐藏/未文档化动作"。推断其来源为作者在装有
  EPLAN 的 Windows 机器上通过运行时捕捉获得(其 [EPLANHTTP](https://github.com/covagashi/EPLANHTTP)
  仓库有 `onActionEnd.String.*` 事件捕捉器佐证;官方 ActionManager 类无"枚举全部动作"的公开 API)。
  体量未知,但**所有探针中未发现任何"本地缺失"的 source_url**,预期体量不大。

### 2.2 EEC Pro 文档 RAG(`rageecpro.covaga.xyz`)

| 组件 | 内容 |
|---|---|
| 部署形态 | 独立 Cloudflare Worker(源码在仓库 `cloudflare-rag-eecpro/`) |
| 向量索引 | Cloudflare Vectorize,索引名 `eecpro-knowledge-base` |
| 嵌入模型 | `@cf/baai/bge-base-en-v1.5`(与 P8 服务同款,768 维,cosine) |
| 向量规模 | **6,760 条**(`/stats` 实测,与 README 的 ~6,760 一致) |
| 构建时间 | `processedUpToDatetime: 2026-04-08` |
| 接口 | MCP(`POST /mcp`,工具 `eecpro_search`/`eecpro_stats`,支持 36 个 category 过滤)+ REST(`/health`、`/search`、`/stats`) |
| 数据来源 | **EEC Pro 2026 产品用户指南**:1,648 个 markdown 页面、36 个分类,来源 URL 实测为 `eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/...`(公开站点) |
| 索引方式 | LlamaIndex(MarkdownNodeParser + SentenceSplitter),源库 `eplan-eecpro-rag-builder/rag_db_llama_chroma`(~102MB) |
| 主要分类 | `refformulas`(公式语言,317 页)、`admin`(安装配置,304 页)、`eecbase`(119 页)、`refformui`、`refcommands`、`refscripting`、`concept`、`eececad`、`eecplc` 等 |

**结论:P8 服务与 EEC Pro 服务是完全独立的两条管线、两个索引、两套数据源**——
P8 服务的数据来自 api/2026 文档(2.1 节结论仅针对它),EEC Pro 服务的数据来自
EEC Pro 2026 产品指南。两者都在线可用、公开无鉴权。

### 2.3 已知问题

1. **category 过滤无效**:索引创建时未配置 filterable 字段,带 `category` 过滤的搜索返回空结果;
2. **非浏览器 UA 被 403**:Cloudflare Bot Fight Mode 拦截 Python-urllib 等默认 UA(浏览器 UA 正常);
3. **无任何枚举/导出接口**:只有 top-K 查询,55,000 条向量不可穷举(详见 9.4 节);
4. **公开服务消耗作者配额**:一次搜索 ≈ 60~180 neurons(免费额度 10,000 neurons/天);
   Vectorize 存储约 $1.6/月,查询按"查询维度"计费(55k×768≈4,200 万维度/次,付费档每月
   含 5,000 万)。**大量使用会直接产生作者账单,请礼貌使用。**

### 2.4 许可

仓库本体为 MIT License(作者 Christian D. Lopez)。线上服务本身无服务条款,属作者自用/小圈子
性质的基础设施。

---

## 3. 本地自建库

本地现在有**两个独立数据库**:

| 库 | 路径 | 定位 | 页数 / 向量数 |
|---|---|---|---|
| **2026 库** | `eplan-p8-mcp-server/chroma_db_sota/` | 与官方两条服务对齐的最新版 | 30,141 页 / 46,210 向量 |
| **2.9 库** | `eplan-p8-mcp-server/chroma_db_p8_2_9/` | 与 P8 2.9 机器版本匹配(2026-08-22 新增) | 29,478 页 / 44,630 向量 |

### 3.1 构建流水线(全部脚本在 `rebuild/`)

```
官网公开页面
   │  crawl.py          (api/2026:webindex 1,969 页 + 链接扩展 23,522 页;Plattform 指南 BFS)
   │  expand_api.py     (补漏成员页:webindex 只列类页,成员页靠类页链接发现)
   │  crawl_eecpro.py   (EEC Pro 指南:Flare Sitemap.xml 全量清单 + 短页阈值 60 字符)
   │  crawl_29.py       (api/2.9 webindex+扩展 + Plattform/2.9 指南 BFS;输出 manifest29.jsonl)
   │  crawl_eec29.py    (EEC Pro 2.9 指南:sitemap 文件名重写到 2.9 路径,见 3.5)
   │  reconvert.py      (本地重转换:修复官网双重编码乱码、提取 Flare toc-path 面包屑)
   ▼
Markdown 语料(rebuild/corpus/ 与 corpus/{api29,guide29,eec29}/;raw 缓存)
   │  index.py --fresh  (按标题分块 450 词/60 词重叠;剔除"Reference"导航样板;
   │                     bge-base-en-v1.5 本地 MPS 嵌入;写入 chroma)
   ▼
eplan-p8-mcp-server/chroma_db_sota        (collection: eplan_docs, 44,242 向量,2026 版)
eplan-p8-mcp-server/chroma_db_p8_2_9      (collection: eplan_docs, 42,968 向量,2.9 版)
```

### 3.2 数据来源清单(实测统计)

**总计 30,141 页 → 46,210 个 chunks**

| 来源 | 页数 | 说明 |
|---|---|---|
| **api/2026 帮助系统** | 25,491 | `eplan.help/en-us/Infoportal/Content/api/2026/`,与官方库同一文档源 |
| ├─ DataModel 命名空间 | 12,344 | 数据模型类/属性/枚举 |
| ├─ DataModel.E3D | 3,136 | 3D 布局 |
| ├─ MasterData | 3,078 | 主数据(符号/表格/部件) |
| ├─ DataModel.Planning | 2,036 | 预规划 |
| ├─ HEServices / Graphics / 其他 | ~4,600 | 项目服务、图形编辑、Base/Gui/ApplicationFramework 等 |
| ├─ User Guide 书 | 105 | api/2026 系统内部的使用指南书(官方库"User Guide"类别所指) |
| └─ **Actions** | **98** | 动作页(export / gedRedraw / XEs* 系列) |
| **Plattform 2026 产品用户指南** | 2,699 | `Content/Plattform/2026/Content/htm/`;BFS 初爬 1,710 页后用 **Sitemap.xml 核验补爬**(覆盖率 99.8%,见 3.6) |
| **EEC Pro 2026 产品用户指南** | 1,950 | `content/eecpro/2026/`,用 Flare `Sitemap.xml` 全量清单抓取(与官方 EEC Pro 服务同源;官方索引 1,648 页,本地更全) |
| **隐藏动作** | 0 | 待补齐(见第 7 节) |

### 3.3 库规格

| 项 | 值 |
|---|---|
| 位置 | `eplan-p8-mcp-server/chroma_db_sota/` |
| Collection | `eplan_docs`(cosine 距离,768 维) |
| 向量数 | 46,210(过滤前更多;剔除 24,900 条纯导航"Reference"样板块后,含 api 25,491 页 + Plattform 2,699 页 + EEC Pro 1,950 页) |
| 嵌入模型 | `BAAI/bge-base-en-v1.5`(与官方库同款,保证语义空间一致) |
| 元数据 schema | `title` / `category` / `source` / `source_url` / `header_path`(对齐线上 worker);`category` 取值:`Api` / `User Guide` / `EEC Pro` |
| 分块策略 | 按标题分段,450 词/块,60 词重叠;纯链接段与 "Reference" 段剔除 |

### 3.4 2.9 库规格(版本匹配库)

| 项 | 值 |
|---|---|
| 位置 | `eplan-p8-mcp-server/chroma_db_p8_2_9/`(由 2026 库复制后全量替换) |
| Collection | `eplan_docs`(同 2026 库,工具无感切换) |
| 向量数 | **44,630** |
| 数据来源 | api/2.9(24,350 页)+ Plattform/2.9 指南(3,229 页)+ EEC Pro 2.9(1,899 页)= **29,478 页,100% 为 /2.9/ 版本 URL**(逐页验证,零 2026 混入) |
| 替换策略 | **全部替换**(非混库):副本上三类内容整体换成 2.9 版。理由见 7.4 节的替换 vs 增量调研 |
| 嵌入模型/分块 | 与 2026 库完全相同(bge-base-en-v1.5,450 词/块) |

### 3.5 官网怪状:EEC Pro 2.9 的 sitemap 是坏的

EEC Pro 2.9 的两个 Sitemap.xml 指向的都是**已下架的 `/eecpro/2.8/` 路径(404)**;
实测 2.9 主题以**相同文件名**存活于 `/Infoportal/Content/EECPro/2.9/Content/htm/`。
`crawl_eec29.py` 的处理:从 sitemap 取文件名 → 重写到 2.9 正确路径再抓取(1,876 页成功)。
顺带发现:EEC Pro 的 2.8 内容已被 EPLAN 从官网删除,2.9 时代 EEC 在线帮助仅此一份。

### 3.6 Plattform 指南覆盖率核验与补爬(2026-08-22)

Flare 站点都有 `Sitemap.xml`(全量主题清单)。用它核验最初靠 BFS 爬的指南,**发现
BFS 漏了约三分之一**——这是 api(webindex+链接穷举)与 EEC(sitemap 清单)都没有
的覆盖风险:

| | BFS 初爬 | Sitemap 全量 | 缺失 | 补爬后 | 覆盖率 |
|---|---|---|---|---|---|
| Plattform/2026 | 1,709 | 2,705 | 996(37%) | 2,699 | 99.8% |
| Plattform/2.9 | 2,216 | 3,233 | 1,017(31%) | 3,229 | 99.9% |

缺失内容为真实功能页(功能校正 adjustdata、Rittal 面板加工 amlgui、部件数据
articlesgui、自动处理 autoprocgui、availableactions 动作页等),补爬后 how-to 类
查询 top1 均分由 0.767 升至 0.792(见 5.7)。工具:`rebuild/backfill_plattform.py`
(sitemap 清单 → 抓取转换 → `incremental_add.py --from-line` 增量嵌入,避免全量重建)。

---

## 4. 内容差别对照

| 维度 | 官方线上库(2 服务) | 本地 2026 库 | 本地 2.9 库 | 说明 |
|---|---|---|---|---|
| api/2026 文档(P8 服务) | ✅ 全量 | ✅ 全量(25,491 页) | ❌(不含) | 同一文档源,本地经链接图穷举 |
| **api/2.9 文档** | ❌ 无 | ❌ 无 | ✅ **全量(24,350 页)** | 版本匹配 P8 2.9 机器 |
| Plattform 产品用户指南 | ❌ 未实证到(P8 服务) | ✅ 2,699 页(2026,99.8% 覆盖) | ✅ **3,229 页(2.9,99.9%)** | 本地两库均为超集;覆盖率经 Sitemap 核验(3.6) |
| EEC Pro 指南(EEC Pro 服务) | ✅ 6,760 向量 / 1,648 页(2026) | ✅ 1,950 页(2026,超出官方) | ✅ **1,899 页(2.9)** | 2.9 版为官网仅存的 2.9 时代 EEC 帮助(见 3.5) |
| hidden actions(P8 服务) | ✅ 有(体量未知) | ❌ 无 | ❌ 无 | 唯一实质缺口(补齐路径见第 7 节) |
| 向量数 | 55,000 + 6,760(合计 61,760) | 46,210 | 44,630 | 差值主要由分块粒度解释,不代表内容缺失 |
| 版本纯度 | 100% 2026 | 100% 2026 | **100% 2.9(逐页验证)** | 评测时按结果 URL 自动统计 |
| 库位置 | 云端,依赖网络与作者配额 | 本地,离线 | 本地,离线 | |
| 数据可维护性 | 不可导出、不可枚举 | 可重建、可增量 | 可重建、可增量 | |

---

## 5. 效果差别(实测)

### 5.1 评测设计:查询怎么选、为什么是 6 个

查询是**按真实使用场景刻意构造**的,覆盖三类查询形态 × 两个知识域:

| # | 查询 | 形态 | 目标域 | 选取理由 |
|---|---|---|---|---|
| 1 | export project to EPJ format | 自然语言+专有名词 | Action 文档 | 动作页/指南混合命中能力的代表 |
| 2 | ReadProjectInfo method parameters | **精确名称查找** | API 参考 | 已知难点:webindex 不含成员页,专门检验补漏效果 |
| 3 | connection definition point properties | 术语组合 | API 参考 | 属性类精确检索 |
| 4 | how to correct project data in the project management | 长句 how-to | 用户指南 | 自然语言问答场景 |
| 5 | generate terminal diagrams from the schematic | 长句 how-to | 用户指南 | 自然语言问答场景 |
| 6 | hidden action redraw / gedRedraw | 专有名词+噪声词 | 隐藏动作 | 检验 hidden actions 缺口的影响 |

选取原则:

- **模拟真实开发者提问**,不是随机词表——每条都是 EPLAN 脚本/项目开发中会实际问到的问题;
- **覆盖三种查询形态**:精确名称查找(2/3)、自然语言 how-to(1/4/5)、带噪声的混合查询(6);
- **故意放入一个已知难点**(#2 ReadProjectInfo)——评测的价值在于暴露短板,而不是全选"稳赢"的题;
- **6 条即可做定性对比**:本评测的目的是"两边水平是否同档、短板在哪",不是统计显著性检验
  (n=6 不做定量结论,局限见 5.5)。

调查过程中的其余几十次查询(数据来源取证、分类探测等)不属于本评测,未计入记分卡。

### 5.2 分数怎么定义、两边是否可比

- **两边用的是同一个嵌入模型**(`bge-base-en-v1.5`)和**同一种度量**(cosine 相似度),
  都在归一化后的 768 维向量空间里计算,因此**分数在语义上是可比的**;
- 线上分数 = Vectorize 返回的 `matches.score`(余弦相似度);
- 本地分数 = `1 − chroma 距离`(chroma 在 cosine 空间返回的 distance 即 `1 − 余弦相似度`)。
  我们做过直接验证:手动用模型对查询和块向量算余弦,与本地 MCP 报告的分数完全吻合
  (如 export 块 0.7462/0.7501 ↔ 报告 0.75);
- **分数经验区间**(bge 归一化向量,供解读):`>0.7` 强相关;`0.5~0.7` 中等相关/同类主题;
  `<0.5` 弱相关。分数是**相对**指标,判读时看的是**同查询跨系统的对比**,不看绝对值;
- 一个方法论要点:**分块粒度影响分数分布**——线上按小节细切,小块对"恰好命中该小节"的
  查询天然得分更高(这解释了 #2 线上 5 条全中);本地 450 词粗切,块更完整、覆盖面更好
  (这解释了 #1/#4/#5 本地得分更高)。所以跨系统对比时,**排名与相关性 > 原始分数差**。

### 5.3 测试环境与执行方式

| 项 | 说明 |
|---|---|
| 协议 | 两边都走 **MCP 协议**(JSON-RPC:`initialize` → `tools/call eplan_search`,参数 `topK=5`),完全同一套工具、同一套参数,避免接口差异引入偏差 |
| 执行 | 由 `rebuild/mcp_compare.py` 自动完成,可复现 |
| 执行时间 | 2026-08-21(记分卡);本地库版本 = 41,550 块(不含 EEC Pro,EEC 不影响 P8 查询) |
| 延迟测量 | 端到端:从发起 initialize 到解析完 tools/call 响应;单次测量(非多次平均,见 5.5 局限) |
| 网络 | 本地服务 127.0.0.1:8765;线上 rag2026.covaga.xyz(经 Cloudflare 边缘节点) |
| 线上 UA | 线上有 Bot Fight 拦截,测试用浏览器 UA(否则 403) |

### 5.4 记分卡结果

| 查询 | 线上最佳分(命中的内容) | 本地最佳分(命中的内容) | 结论 |
|---|---|---|---|
| export project to EPJ format | 0.676(action 页 export) | **0.773**(指南"Exporting Projects") | 本地更全(指南+action+方法混合) |
| ReadProjectInfo method parameters | 0.713(**5 条全中方法重载页**) | **0.791**(#1 "ReadProjectInfo Method" 正确,其余为相关方法) | 线上精度略胜;本地首位正确 |
| connection definition point properties | 0.691(属性枚举页) | **0.858**(指南"Connection Definition Points") | 本地明显更好 |
| correct project data(how-to) | 0.617(API 方法 CorrectProjectItems) | **0.743**(指南"Finding and Storing Missing Project Master Data") | 本地更对题 |
| generate terminal diagrams | 0.588(API 方法 Terminals) | **0.760**(指南"Generating and Editing Terminals") | 本地明显更好 |
| hidden action redraw / gedRedraw | 0.612(gedRedraw,疑似隐藏动作条目) | **0.789**(官方动作页 gedRedraw) | 打平;官方动作页双方都有,隐藏条目线上独占 |

**延迟:本地 71~97ms vs 线上 925~1,268ms(约 10~15 倍差距,且本地无网络抖动)。**

### 5.5 评测局限(诚实声明)

1. **n=6,单次测量**:样本小、延迟未做多次平均,结论是定性的("同档/谁有短板"),不具备统计显著性;
2. **相关性由人工判读**:未做盲评/多标注者,判断基于我对结果内容的阅读;
3. **线上库可能已变化**:索引数据截止 2026-03-27,作者可能随时更新/下线,记分卡结果以
   执行日为准;复测需重跑 `mcp_compare.py`;
4. **分块粒度使分数不完全对等**:见 5.2 最后一条——因此结论表述为"排名与相关性",而非
   "本地分数高 0.1 所以好 15%";
5. **EEC Pro 不在记分卡内**:记分卡执行时本地尚无 EEC 库。EEC 入库后做了抽样验证:
   "creating a configuration by importing an XML file" 本地 top-1 命中与官方 EEC 服务
   **同源页面**(0.80 分),且 P8 旧查询回归无变化(0.7726/0.7707 与记分卡一致)。

### 5.6 如何复现

```bash
# 1. 启动本地 MCP(模型加载约 30~60 秒)
python rebuild/local_mcp.py --port 8765 &

# 2. 运行对比(自动执行 6 组查询 + eplan_stats,输出到终端)
python rebuild/mcp_compare.py
# 结果亦保存于 rebuild/compare_final.txt(本仓库)
```

### 5.7 三库大样本评测(2026-08-22,2.9 库建成后)

按 5.1~5.3 的同一套方法,扩展到**三个库**、**28 组查询**:

- **目标**:线上 2026 服务 / 本地 2026 库(:8765)/ 本地 2.9 库(:8766);
- **查询构成**:action 5 组、api-exact 6 组、how-to 6 组、version 4 组、eec 4 组、noise 3 组
  (含超长口语化问题、无关领域问题 "python sort list by key"、单词查询 "export");
- 执行脚本:`rebuild/mcp_compare3.py`,全量明细 `rebuild/eval3_results.json`;
- **版本纯度自动核验**:每次查询统计返回结果的 URL 版本构成——线上/本地2026 全部
  api|Plattform|eecpro **/2026/**,本地2.9 全部 **/2.9/**,零混版(28×3 组全部通过)。

**总体结果(n=28,top1 均分 / 平均延迟;2026-08-22 补爬后复测):**

| 库 | top1 均分 | 平均延迟 | 错误 |
|---|---|---|---|
| 线上 2026 | 0.620 | 582ms | 0 |
| 本地 2026 | **0.784** | 58ms | 0 |
| 本地 2.9 | 0.775 | **35ms** | 0 |

**分类型 top1 均分:**

| 类型 | 线上 2026 | 本地 2026 | 本地 2.9 | 解读 |
|---|---|---|---|---|
| action | 0.631 | **0.780** | 0.746 | 两个本地库均显著领先 |
| api-exact | 0.677 | 0.811 | **0.818** | 本地两库相近,2.9 略高 |
| howto | 0.601 | **0.792** | 0.784 | 本地有产品指南;补爬后提升(0.767→0.792) |
| version | 0.650 | **0.793** | 0.789 | 版本专属查询本地更强 |
| eec | (对照无效,见 5.8) | **0.775** | 0.776 | 见下方说明 |
| noise | 0.563 | **0.720** | 0.698 | 三库均无"无结果"机制(见 7.6) |

> ⚠️ **EEC 行的对照对象更正**:28 组评测中的 4 组 EEC 查询发给了官方 **P8 服务**
> (rag2026),该服务本来就不含 EEC 数据,分数 0.562 只能证明这一点,**不能作为
> "官方 vs 本地"的 EEC 效果对照**。正确对照(官方 EEC 服务 rageecpro)见 5.8 节。

**重点发现:**

1. **版本匹配价值实证**:如 "XEsGetProjectPropertyAction parameters" —— 2.9 库 top1 返回
   `XEsSetProjectPropertyAction`(0.80),2026 库返回同名 Get 页(0.85):两版文档确有差异,
   混库查询将无法区分;
2. **本地两库分数互有胜负但同档**(0.775 vs 0.784):2.9 语料规模略小、部分 2.9 页面
   内容较 2026 精简,属正常版本差异,不影响结论;
3. **噪声鲁棒性**是三库共同短板:无关查询也返回 0.5~0.7 的"最接近"结果,改进项见 7.6。

### 5.8 EEC 类查询的正确对照(官方 EEC 服务,2026-08-22)

4 组 EEC 查询发给**官方 EEC Pro 服务**(`rageecpro.covaga.xyz`,工具 `eecpro_search`,
topK=5)与两个本地库,top1 均分:

| 官方 EEC 服务 | 本地 2026 | 本地 2.9 |
|---|---|---|
| 0.789 | 0.775 | 0.776 |

**三库同档(0.78 附近),top1 排名高度一致**("abs()"、"Model variables: Overview" 等
均相互印证)。执行脚本 `rebuild/eec_control_eval.py`,明细 `rebuild/eval3_eec_control.json`。

---

## 6. 使用指南

### 6.1 本地 MCP 服务(两个库各起一个实例)

```bash
# 2026 库(:8765)
python rebuild/local_mcp.py --port 8765 --db-path eplan-p8-mcp-server/chroma_db_sota

# 2.9 库(:8766)
python rebuild/local_mcp.py --port 8766 --db-path eplan-p8-mcp-server/chroma_db_p8_2_9

# 接入 Claude Code(按需选一个)
claude mcp add eplan-rag-2026 http://127.0.0.1:8765/mcp
claude mcp add eplan-rag-29   http://127.0.0.1:8766/mcp

# 或 REST 直接调用
curl -X POST http://127.0.0.1:8766/search \
  -H "Content-Type: application/json" \
  -d '{"query":"export project to EPJ format","topK":5}'

# 统计
curl http://127.0.0.1:8766/stats
```

> ⚠️ 两个实例各加载一份嵌入模型,共占用约 3~4GB 内存,且共享 MPS 设备——
> **不要在任一实例运行期间执行索引重建**(MPS 争用会使嵌入速度下降约 20 倍)。

协议与线上 worker 完全一致(同样的工具名、参数、返回格式),可无缝替换。

### 6.2 直接查询 chroma / 验证数量

```bash
cd ~/program/eplan-rag-mcp
python -c "import chromadb; c=chromadb.PersistentClient(path='eplan-p8-mcp-server/chroma_db_sota'); x=c.get_collection('eplan_docs'); print(x.count())"
# 输出: 46210  (2026 库;2.9 库路径换为 chroma_db_p8_2_9,输出 44630)

python rebuild/query.py "export project" 5          # CLI 查询
```

### 6.3 重要运维经验

1. **不要与索引重建同时运行 MCP 服务**:两者都占 Apple Silicon 的 MPS 设备,并发会导致
   嵌入速度下降约 20 倍(实测 1,300 块/分钟 → 150 块/分钟);
2. **重建后必须重启 MCP 服务**:chroma 长进程的 collection 句柄会因 `--fresh` 删除重建而
   失效(`Collection does not exist` 报错)。当前 local_mcp.py 已改为每请求重新解析,
   但仍建议重建后重启一次;
3. `--fresh` 重建会删除旧 collection,约需 20~60 分钟(取决于 MPS 是否被占用)。

---

## 7. 已知差距与补齐路径

### 7.1 hidden actions(唯一实质缺口)

按性价比排序:

| 方案 | 说明 | 状态 |
|---|---|---|
| **A. 找作者要导出** | GitHub issue 索要 `vectors_batch_*.ndjson`(作者部署脚本显示有 12 批现成导出)或原 chroma 库 | 未执行,草稿可随时写 |
| **B. 2.9 DLL 离线提取** | 用 `hidden-actions-extractor/` 工具套件:拷 EPLAN 2.9 的 Bin 目录 → 提取动作名 → 探测 eplan.help 区分"有官方页/真隐藏" | **工具已就绪并本地验证**(见附录);待拿到 Bin 目录执行 |
| **C. Windows API 探测** | 在装有 EPLAN 的 Windows 上用 FindAction 词表暴力 + 反射 dump 注册表 | 需要 Windows + EPLAN 授权 |
| **D. 反推线上库** | 用候选名查询线上 RAG 收集新 source | ❌ 已证伪:所有探针无本地缺失 URL,且消耗作者配额 |

### 7.2 版本匹配(P8 2.9)—— ✅ 已完成(2026-08-22)

已构建独立的 **2.9 版本地库**(`chroma_db_p8_2_9`,42,968 向量):api/2.9 全量
(24,350 页)+ Plattform/2.9 指南(2,217 页)+ EEC Pro 2.9(1,899 页),100% 版本纯净
(评测中按结果 URL 逐条核验)。使用方式见 6.1 节;替换 vs 增量的决策记录见 7.4 节。

### 7.3 EEC Pro 2026 指南补充 —— ✅ 已完成(2026-08-22)

已用 `rebuild/crawl_eecpro.py` 爬取并入本地库:**1,950 页**(官方 EEC Pro 服务索引
1,648 页,本地为其超集)。要点:

- **清单来源**:Flare 生成的 `Sitemap.xml`(BFS 不适用——EEC Pro 的侧边菜单是
  JS 动态生成,页面互链少,Sitemap 才是全量主题清单);
- **短页阈值**:EEC Pro 有大量单表/单段短参考页(~180 字符),转换阈值放宽到 60 字符
  (113 个短参考页因此被成功收录);
- **合理排除**:6 个"Print Only Topics"打印版式页、2 个空壳页(EPLAN_Help/Search)、
  21 个纯图片页(EPLAN 把公式/图表渲染成图片,无文本可索引);
- **验证**:EEC 查询("creating a configuration by importing an XML file")本地
  top-1 命中与官方 EEC 服务同源页面,分数 0.80;旧查询无回归。

### 7.4 2.9 库的"替换 vs 增量"决策记录

构建 2.9 库前调研了两条路线,结论:**全部替换**(非混库):

| | 增量(2026+2.9 混库) | 替换(纯 2.9) |
|---|---|---|
| 版本纯净度 | ❌ 结果混两版,不细看 URL 分不清 | ✅ 100% 2.9 |
| 正确性风险 | ❌ 2026 才有的 API/动作会给 2.9 机器错误建议 | ✅ 无 |
| 检索质量 | ❌ 近重复页挤占 top-K,密集簇风险 | ✅ 与已验证配置同档 |
| 体积 | ~85k 块 | ~43k 块 |

P8 2.9 机器的日常查询只关心 2.9:混库唯一好处(跨版本对照)是低频需求且可由
"两个库分别查"替代;其危害(错误版本建议)是高频风险。故选替换。

### 7.5 已知瑕疵

- **指南页 source 路径**:Flare 的 toc-path 占位符未清理干净,部分 Plattform 指南页
  (1,136 个)与 EEC Pro 页的 `source` 以 "You are here_" 开头,如
  `UserGuide/You are here_/...`、`EECPro/You are here_/...`。不影响搜索质量
  (title/URL/内容均正确),后续 `reconvert.py` 可在 `extract_flare` 中过滤该前缀修复。

### 7.6 检索鲁棒性(待改进)

三库共同短板:对无关查询(如 "python sort list by key")仍返回 0.5~0.7 分的"最接近"
结果,没有"无结果"机制。改进方案:在 `local_mcp.py` 的 `search()` 中加分数阈值
(如 top1 < 0.55 时返回"未找到相关内容"),可在 MCP 响应中同时给出分数供调用方判断。
预计收益:消除误导性答案;风险:阈值过高会误伤弱相关但有用的结果(需用 noise 类
查询回归验证)。

### 7.7 EEC Pro 机器版本风险(⚠️ 与 hidden actions 同级,待确认)

- 本地 2.9 库的 EEC 部分取自官网仅存的 **EEC Pro 2.9** 帮助;
- 官网已删除 EEC Pro **2.8** 内容,且 [Wayback Machine](https://web.archive.org)
  实测**无任何存档** → **若使用者的 EEC Pro 机器是 2.8,对应文档永远无法重建**;
- 使用者的 EEC Pro 实际版本**尚未确认**,待填入:
  > 【待确认】EEC Pro 机器版本:______(若为 2.8,本条与 hidden actions 同列最高风险)

---

## 8. 维护与更新

- **文档更新(如 EPLAN 2027 发布)**:改 `rebuild/crawl.py` 顶部 `API_INDEX_URL` /
  `GUIDE_SEEDS` 为新版本 URL,重跑 `crawl.py` → `reconvert.py` → `index.py --fresh`;
- **增量补充**(如 api/2.9):新爬取会追加到 manifest,重跑 `index.py --fresh` 全量重建
  (当前无增量模式,介意时间可自行改造);
- **环境依赖**:Python 3.13 + `chromadb` + `sentence-transformers` + `beautifulsoup4` +
  `lxml` + `markdownify`(均在 miniconda3 中已装好)。

---

## 9. 构建过程中的关键技术结论

1. **webindex 不是全量**:官网 Innovasys 帮助系统的 `webindex.html` 只列类级页面,
   成员页(方法/属性/事件重载)必须靠链接扩展发现——扩展后页数从 1,969 增至 25,491;
2. **样板簇污染检索**:大量页面尾部有内容雷同的 "Reference" 导航段(占 37%),形成密集向量簇
   吞噬 HNSW 近邻结果。剔除后检索质量恢复;并采用"多取再重排"(取 top_k×8 后按精确
   cosine 距离重排)补偿 HNSW 召回;
3. **官网双重编码**:eplan.help 部分文本双重 UTF-8 编码(如 `•` 显示为 `â€¢`),已在
   `reconvert.py` 中用映射表修复;
4. **向量库不可穷举的原理**:`/search` 只返回 top-20。55,000 个向量分布在 768 维空间中,
   要捞出一个块必须构造让它进入 top-20 的查询——而查询词汇只能来自已知词汇,
   "未知的词对应的块永远不可达"(自指悖论)。这决定了 hidden actions 只能靠"知道名字"
   的途径(提取/探测/作者导出)补齐,而非反推。

---

## 10. 附录:文件结构与工具清单

```
eplan-rag-mcp/
├── docs/
│   └── rag-libraries-comparison.md       # 本文档
├── rebuild/                              # 重建流水线
│   ├── crawl.py                          # 爬取+转换(webindex + BFS,可断点续爬)
│   ├── expand_api.py                     # 成员页链接扩展(补漏 23,522 页)
│   ├── crawl_eecpro.py                   # EEC Pro 指南爬取(Sitemap.xml 清单,短页阈值 60)
│   ├── crawl_29.py                       # api/2.9 + Plattform/2.9 爬取(webindex+扩展+BFS)
│   ├── crawl_eec29.py                    # EEC Pro 2.9 爬取(sitemap 文件名重写到 2.9 路径)
│   ├── backfill_plattform.py             # Plattform 覆盖率补爬(sitemap 核验 BFS 漏页)
│   ├── incremental_add.py                # 增量嵌入(--from-line,补爬后免全量重建)
│   ├── eec_control_eval.py               # EEC 正确对照评测(官方 EEC 服务 vs 本地)
│   ├── reconvert.py                      # 本地重转换(乱码修复/面包屑)
│   ├── index.py [--fresh] [--db-path] [--manifest] [--collection]
│   │                                     # 分块+嵌入+写 chroma(参数化,可建多库)
│   ├── query.py                          # CLI 查询
│   ├── local_mcp.py [--port] [--db-path] # 本地 MCP 服务(协议同线上 worker,可多实例)
│   ├── mcp_compare.py                    # 线上 vs 本地(6 组记分卡)
│   ├── mcp_compare3.py                   # 三库大样本评测(28 组查询)
│   ├── corpus/                           # markdown 语料(2026:api/guide/eec)
│   ├── corpus/{api29,guide29,eec29}/     # 2.9 语料
│   ├── raw/ raw29/                       # 原始 HTML 缓存
│   ├── manifest.jsonl                    # 2026 页面元数据(29,151 条)
│   └── manifest29.jsonl                  # 2.9 页面元数据(28,466 条)
├── hidden-actions-extractor/             # 隐藏动作提取工具(方法3)
│   ├── extract_actions.ps1               # Windows PowerShell 反射提取器(零依赖)
│   ├── extract_strings.py                # CLR 元数据提取器(跨平台,纯标准库)
│   ├── probe_eplan_pages.py              # 候选名探测官网(区分有页/真隐藏)
│   └── README.md                         # 使用说明(依赖/步骤/法律提示)
└── eplan-p8-mcp-server/
    ├── chroma_db_sota/                   # 本地 2026 库(46,210 向量)
    └── chroma_db_p8_2_9/                 # 本地 2.9 库(44,630 向量)
```

**验证状态**:`extract_strings.py` 已用真实 .NET 程序集实测通过;`probe_eplan_pages.py`
已联网实测通过(gedRedraw/export/XEsGetProjectPropertyAction 全部正确分类,
并确认 api/2.9 目录在线);`extract_actions.ps1` 需在 Windows 实机首次验证。

---

*文档生成:2026-08-22。所有数字可复核:manifest 统计脚本、`mcp_compare.py`、
`/stats` 与 `/search` 实测输出均在本仓库与对话记录中。*
