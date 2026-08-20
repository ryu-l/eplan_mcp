"""
Side-by-side comparison: live Cloudflare MCP vs local rebuilt MCP.

Runs the same queries through both /mcp endpoints (JSON-RPC initialize +
tools/call) and prints latency + top results for each.
"""
import json
import time
import urllib.request

LIVE = "https://rag2026.covaga.xyz"
LOCAL = "http://127.0.0.1:8765"

QUERIES = [
    ("action", "export project to EPJ format"),
    ("api-ref", "ReadProjectInfo method parameters"),
    ("api-ref", "connection definition point properties"),
    ("user-guide", "how to correct project data in the project management"),
    ("user-guide", "generate terminal diagrams from the schematic"),
    ("hidden", "hidden action redraw / gedRedraw"),
]


def mcp_call(base, method, params=None, rpc_id=1):
    body = {"jsonrpc": "2.0", "id": rpc_id, "method": method}
    if params is not None:
        body["params"] = params
    req = urllib.request.Request(
        base + "/mcp",
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json",
                 "Accept": "application/json, text/event-stream",
                 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                               "AppleWebKit/537.36 (KHTML, like Gecko) "
                               "Chrome/126.0.0.0 Safari/537.36"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def search_via_mcp(base, query, top_k=5):
    t0 = time.time()
    mcp_call(base, "initialize", {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "compare", "version": "1.0"},
    })
    resp = mcp_call(base, "tools/call", {
        "name": "eplan_search",
        "arguments": {"query": query, "topK": top_k},
    }, rpc_id=2)
    latency = time.time() - t0
    if "error" in resp:
        return {"error": resp["error"], "latency": latency}
    text = resp["result"]["content"][0]["text"]
    if resp["result"].get("isError"):
        return {"error": text, "latency": latency}
    # parse "### N. title (score: x)" lines
    results = []
    for line in text.splitlines():
        if line.startswith("### "):
            import re
            m = re.match(r"### \d+\. (.*) \(score: ([\d.]+)\)", line)
            if m:
                results.append((m.group(1)[:70], float(m.group(2))))
    return {"results": results, "latency": latency, "raw_head": text[:400]}


def stats_via_mcp(base):
    mcp_call(base, "initialize", {
        "protocolVersion": "2024-11-05", "capabilities": {},
        "clientInfo": {"name": "compare", "version": "1.0"},
    })
    resp = mcp_call(base, "tools/call", {"name": "eplan_stats"}, rpc_id=2)
    return resp["result"]["content"][0]["text"]


def main():
    print("=" * 78)
    print("MCP 对比测试: 线上 Cloudflare  vs  本地重建库")
    print("=" * 78)

    print("\n--- eplan_stats ---")
    for label, base in (("线上", LIVE), ("本地", LOCAL)):
        try:
            print(f"[{label}] {stats_via_mcp(base)}")
        except Exception as exc:  # noqa: BLE001
            print(f"[{label}] FAILED: {exc}")

    print("\n" + "=" * 78)
    for kind, query in QUERIES:
        print(f"\n查询 [{kind}]: \"{query}\"")
        print("-" * 78)
        for label, base in (("线上", LIVE), ("本地", LOCAL)):
            try:
                r = search_via_mcp(base, query)
                if "error" in r:
                    print(f"  [{label}] 错误: {str(r['error'])[:120]}")
                    continue
                print(f"  [{label}] 耗时 {r['latency'] * 1000:.0f} ms, "
                      f"返回 {len(r['results'])} 条:")
                for title, score in r["results"][:5]:
                    print(f"     {score:.4f}  {title}")
            except Exception as exc:  # noqa: BLE001
                print(f"  [{label}] FAILED: {exc}")
    print("\n" + "=" * 78)


if __name__ == "__main__":
    main()
