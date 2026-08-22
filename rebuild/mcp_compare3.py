"""
三库大样本评测:线上官方(2026)/ 本地 2026 库 / 本地 2.9 库。

28 条查询覆盖:动作、API 精确查找、指南 how-to、EEC、噪声边界。
每库同协议(MCP eplan_search topK=5)执行,记录 top-5 标题+分数+延迟,
并统计结果 URL 的版本构成(2026 vs 2.9),验证各库版本纯度。

输出:rebuild/eval3_results.json(全量明细)+ 终端摘要。
"""
import json
import re
import time
import urllib.request
from collections import Counter

TARGETS = [
    ("线上2026", "https://rag2026.covaga.xyz"),
    ("本地2026", "http://127.0.0.1:8765"),
    ("本地2.9", "http://127.0.0.1:8766"),
]

QUERIES = [
    # (类型, 查询)
    ("action", "export project to EPJ format"),
    ("action", "gedRedraw"),
    ("action", "generate connections from the schematic"),
    ("action", "import device list from Excel"),
    ("action", "compress project"),
    ("api-exact", "ReadProjectInfo method parameters"),
    ("api-exact", "ConnectionDefPointProperties Property"),
    ("api-exact", "OpenProject overloads"),
    ("api-exact", "Layer Management class"),
    ("api-exact", "Terminal property"),
    ("api-exact", "FindAction method"),
    ("howto", "how to correct project data in the project management"),
    ("howto", "generate terminal diagrams from the schematic"),
    ("howto", "create a plot frame"),
    ("howto", "create page macros"),
    ("howto", "navigate the 3D layout space"),
    ("howto", "edit the graphical layer table"),
    ("version", "XEsGetProjectPropertyAction parameters"),
    ("version", "preplanning segments"),
    ("version", "save workspace action"),
    ("version", "API action list"),
    ("eec", "creating a configuration by importing an XML file"),
    ("eec", "formula language abs function"),
    ("eec", "model variables administration"),
    ("eec", "EEC scripting reference"),
    ("noise", "python sort list by key"),
    ("noise", "export"),
    ("noise", "I have a very specific problem: when I place a device symbol onto a "
              "schematic page and the part number is empty, is there an automatic "
              "way to fill it from the parts database for all pages at once"),
]

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126 Safari/537.36")


def mcp_call(base, method, params=None, rpc_id=1):
    body = {"jsonrpc": "2.0", "id": rpc_id, "method": method}
    if params is not None:
        body["params"] = params
    req = urllib.request.Request(
        base + "/mcp", data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json",
                 "Accept": "application/json, text/event-stream",
                 "User-Agent": UA}, method="POST")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def search(base, query, top_k=5):
    mcp_call(base, "initialize", {
        "protocolVersion": "2024-11-05", "capabilities": {},
        "clientInfo": {"name": "compare3", "version": "1.0"}})
    t0 = time.time()
    resp = mcp_call(base, "tools/call", {
        "name": "eplan_search", "arguments": {"query": query, "topK": top_k}}, rpc_id=2)
    latency = time.time() - t0
    if "error" in resp or resp["result"].get("isError"):
        return {"error": resp.get("error", "isError"), "latency": latency,
                "results": []}
    text = resp["result"]["content"][0]["text"]
    results = []
    for line in text.splitlines():
        m = re.match(r"### \d+\. (.*) \(score: ([\d.]+)\)", line)
        if m:
            results.append({"title": m.group(1), "score": float(m.group(2))})
    # 从返回文本中提取 source URL(两库格式都在 **Source:** 行)
    urls = re.findall(r"\*\*Source:\*\* (https?://\S+)", text)
    return {"latency": latency, "results": results, "urls": urls}


def version_of(url):
    m = re.search(r"/Content/(api|Plattform)/([0-9.]+)/", url)
    if m:
        return f"{m.group(1)}/{m.group(2)}"
    m = re.search(r"/content/(eecpro)/([0-9.]+)/", url, re.I)
    if m:
        return f"eecpro/{m.group(2)}"
    return "other"


def main():
    out = {}
    print("=" * 100)
    print("三库大样本评测")
    print("=" * 100)
    for kind, query in QUERIES:
        row = {}
        print(f"\n[{kind}] {query[:70]}")
        for name, base in TARGETS:
            try:
                r = search(base, query)
            except Exception as exc:  # noqa: BLE001
                r = {"error": str(exc)[:80], "latency": None, "results": []}
            row[name] = r
            if r.get("error"):
                print(f"  {name:8} 错误: {r['error']}")
                continue
            vers = Counter(version_of(u) for u in r["urls"]).most_common(4)
            ver_str = ", ".join(f"{k}:{v}" for k, v in vers)
            top1 = r["results"][0] if r["results"] else {"title": "-", "score": 0}
            n_rel = len(r["results"])
            print(f"  {name:8} {r['latency']*1000:6.0f}ms top1={top1['score']:.4f} "
                  f"'{top1['title'][:42]}' 返回{n_rel}条 | 版本构成: {ver_str}")
        out[f"{kind}||{query}"] = row
    with open("/Users/mac/program/eplan-rag-mcp/rebuild/eval3_results.json",
              "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print("\n全量明细已存 rebuild/eval3_results.json")


if __name__ == "__main__":
    main()
