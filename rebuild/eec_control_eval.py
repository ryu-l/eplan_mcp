"""
EEC 类查询的正确对照评测:官方 EEC Pro 服务(rageecpro)vs 两个本地库。

之前的 28 组评测把 EEC 查询发给了官方 P8 服务(rag2026)——那是错误对照
(P8 服务本来就不含 EEC 数据)。本脚本把 4 组 EEC 查询发给:
  - 官方 EEC Pro 服务 https://rageecpro.covaga.xyz(工具名动态探测)
  - 本地 2026 库(:8765,eplan_search)
  - 本地 2.9 库(:8766,eplan_search)
同 topK=5,输出摘要并保存 rebuild/eval3_eec_control.json。
"""
import json
import re
import time
import urllib.request

TARGETS = [
    ("官方EEC", "https://rageecpro.covaga.xyz", None),   # 工具名运行时探测
    ("本地2026", "http://127.0.0.1:8765", "eplan_search"),
    ("本地2.9", "http://127.0.0.1:8766", "eplan_search"),
]
QUERIES = [
    "creating a configuration by importing an XML file",
    "formula language abs function",
    "model variables administration",
    "EEC scripting reference",
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


def list_tools(base):
    resp = mcp_call(base, "tools/list")
    return [t["name"] for t in resp["result"]["tools"]]


def search(base, tool, query, top_k=5):
    mcp_call(base, "initialize", {
        "protocolVersion": "2024-11-05", "capabilities": {},
        "clientInfo": {"name": "eec-control", "version": "1.0"}})
    t0 = time.time()
    resp = mcp_call(base, "tools/call", {
        "name": tool, "arguments": {"query": query, "topK": top_k}}, rpc_id=2)
    latency = time.time() - t0
    if "error" in resp or resp["result"].get("isError"):
        return {"error": resp.get("error", "isError"), "latency": latency, "results": []}
    text = resp["result"]["content"][0]["text"]
    results = []
    for line in text.splitlines():
        m = re.match(r"### \d+\. (.*) \(score: ([\d.]+)\)", line)
        if m:
            results.append({"title": m.group(1), "score": float(m.group(2))})
    return {"latency": latency, "results": results}


def main():
    # 探测官方 EEC 服务的工具名
    try:
        tools = list_tools(TARGETS[0][1])
        print("官方 EEC 服务工具列表:", tools)
        TARGETS[0] = (TARGETS[0][0], TARGETS[0][1],
                      next((t for t in tools if "search" in t), None))
    except Exception as exc:  # noqa: BLE001
        print("官方 EEC 服务 tools/list 失败:", exc)
    out = {}
    print("=" * 90)
    for query in QUERIES:
        print(f"\n查询: {query}")
        row = {}
        for name, base, tool in TARGETS:
            if not tool:
                row[name] = {"error": "no search tool"}
                print(f"  {name:8} 无可用搜索工具")
                continue
            try:
                r = search(base, tool, query)
            except Exception as exc:  # noqa: BLE001
                r = {"error": str(exc)[:80], "latency": None, "results": []}
            row[name] = r
            if r.get("error"):
                print(f"  {name:8} 错误: {r['error']}")
                continue
            top1 = r["results"][0] if r["results"] else {"title": "-", "score": 0}
            print(f"  {name:8} {r['latency']*1000:6.0f}ms top1={top1['score']:.4f} "
                  f"'{top1['title'][:55]}' 返回{len(r['results'])}条")
        out[query] = row
    with open("/Users/mac/program/eplan-rag-mcp/rebuild/eval3_eec_control.json",
              "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print("\n明细已存 rebuild/eval3_eec_control.json")


if __name__ == "__main__":
    main()
