"""
Local MCP server for the rebuilt EPLAN RAG index.

Protocol-compatible with the live Cloudflare worker (cloudflare-rag-eplan-p8):
  - POST /mcp          JSON-RPC (initialize / tools/list / tools/call)
  - GET  /health, /stats
  - POST /search       REST search
Tools: eplan_search, eplan_stats (identical schemas to the live worker).
Backend: local chroma_db_sota / eplan_docs + bge-base-en-v1.5 (MPS).

Run:  python local_mcp.py [--port 8765]
"""
import argparse
import json
import os
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import chromadb
from sentence_transformers import SentenceTransformer

ROOT = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(ROOT, "..", "eplan-p8-mcp-server", "chroma_db_sota")
COLLECTION = "eplan_docs"
MODEL_NAME = "BAAI/bge-base-en-v1.5"

CATEGORIES = ["API Reference", "User Guide", "Api"]

print("loading model ...", flush=True)
MODEL = SentenceTransformer(MODEL_NAME, device="mps")
CLIENT = chromadb.PersistentClient(path=os.path.abspath(DB_PATH))
COL = CLIENT.get_collection(COLLECTION)
print(f"ready: {COL.count()} docs", flush=True)

TOOLS = [
    {
        "name": "eplan_search",
        "description": "Search EPLAN documentation (API Reference, User Guide). "
                       "Use natural language queries. Returns relevant chunks with metadata.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string",
                          "description": "Natural language search query about EPLAN"},
                "topK": {"type": "number", "minimum": 1, "maximum": 20,
                         "default": 5, "description": "Number of results to return"},
                "category": {"type": "string", "enum": CATEGORIES,
                             "description": "Filter by doc category"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "eplan_stats",
        "description": "Get statistics about the EPLAN RAG index "
                       "(vector count, dimensions, metric).",
        "inputSchema": {"type": "object", "properties": {}},
    },
]


def search(query, top_k=5, category=None):
    top_k = min(top_k, 20)
    # HNSW recall at this index size is imperfect: fetch several times the
    # requested k, then re-rank by exact cosine distance and keep top_k.
    fetch_k = max(top_k * 8, 40)
    qvec = MODEL.encode([query], normalize_embeddings=True).tolist()
    where = {"category": category} if category else None
    res = COL.query(query_embeddings=qvec, n_results=fetch_k, where=where)
    out = []
    for i in range(len(res["ids"][0])):
        meta = res["metadatas"][0][i]
        out.append({
            "id": res["ids"][0][i],
            "score": 1.0 - res["distances"][0][i],  # cosine similarity
            "title": meta.get("title", ""),
            "category": meta.get("category", ""),
            "source": meta.get("source", ""),
            "source_url": meta.get("source_url", ""),
            "content": res["documents"][0][i],
            "header_path": meta.get("header_path", ""),
        })
    out.sort(key=lambda x: -x["score"])
    return out[:top_k]


def stats():
    return {
        "index": "eplan_docs-local",
        "model": MODEL_NAME,
        "dimensions": 768,
        "vectorCount": COL.count(),
    }


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def _send(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
        self.end_headers()

    def do_GET(self):
        if self.path == "/health":
            self._send({"status": "ok", "mcp": True,
                        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime())})
        elif self.path == "/stats":
            self._send(stats())
        elif self.path == "/mcp":
            self._send({"name": "eplan-rag-local", "version": "1.0.0",
                        "description": "Local EPLAN RAG MCP - use POST /mcp for JSON-RPC"})
        else:
            self._send({"error": "Not found",
                        "endpoints": ["/health", "/search", "/stats", "/mcp"]}, 404)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length) or b"{}")
        if self.path == "/search":
            if not body.get("query"):
                return self._send({"error": "Missing 'query' field"}, 400)
            results = search(body["query"], int(body.get("topK", 5)),
                             body.get("category"))
            return self._send({"query": body["query"], "results": results,
                               "count": len(results)})
        if self.path == "/mcp":
            return self._handle_mcp(body)
        self._send({"error": "Not found"}, 404)

    def _handle_mcp(self, body):
        method = body.get("method")
        rpc_id = body.get("id")
        if method == "initialize":
            return self._send({
                "jsonrpc": "2.0", "id": rpc_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {"listChanged": False}},
                    "serverInfo": {"name": "eplan-rag-local", "version": "1.0.0"},
                }})
        if method == "notifications/initialized":
            self.send_response(204)
            self.end_headers()
            return
        if method == "ping":
            return self._send({"jsonrpc": "2.0", "id": rpc_id, "result": {}})
        if method == "tools/list":
            return self._send({"jsonrpc": "2.0", "id": rpc_id, "result": {"tools": TOOLS}})
        if method == "tools/call":
            params = body.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {}) or {}
            try:
                if name == "eplan_search":
                    query = args.get("query")
                    if not query:
                        text = "Error: query is required"
                        is_err = True
                    else:
                        results = search(query, int(args.get("topK", 5)),
                                         args.get("category"))
                        lines = [f"Found {len(results)} results for \"{query}\":\n"]
                        for i, m in enumerate(results):
                            part = [f"### {i + 1}. {m['title']} (score: {m['score']:.4f})"]
                            if m["category"]:
                                part.append(f"**Category:** {m['category']}")
                            if m["source_url"]:
                                part.append(f"**Source:** {m['source_url']}")
                            if m["header_path"]:
                                part.append(f"**Section:** {m['header_path']}")
                            if m["content"]:
                                part.extend(["", m["content"]])
                            lines.append("\n".join(part))
                        text = "\n\n---\n\n".join(lines)
                        is_err = False
                elif name == "eplan_stats":
                    text = json.dumps(stats(), indent=2)
                    is_err = False
                else:
                    return self._send({
                        "jsonrpc": "2.0", "id": rpc_id,
                        "error": {"code": -32601, "message": f"Unknown tool: {name}"}})
                return self._send({
                    "jsonrpc": "2.0", "id": rpc_id,
                    "result": {"content": [{"type": "text", "text": text}],
                               "isError": is_err}})
            except Exception as exc:  # noqa: BLE001
                return self._send({
                    "jsonrpc": "2.0", "id": rpc_id,
                    "result": {"content": [{"type": "text",
                                            "text": f"Error: {exc}"}],
                               "isError": True}})
        return self._send({
            "jsonrpc": "2.0", "id": rpc_id,
            "error": {"code": -32601, "message": f"Unknown method: {method}"}})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"local MCP listening on http://127.0.0.1:{args.port}/mcp", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
