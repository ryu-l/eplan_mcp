"""
Query the local EPLAN RAG index (chroma_db_sota / eplan_docs).

Usage:
  python query.py "export project" [top_k] [category]
"""
import os
import sys

import chromadb
from sentence_transformers import SentenceTransformer

ROOT = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(ROOT, "..", "eplan-p8-mcp-server", "chroma_db_sota")
COLLECTION = "eplan_docs"
MODEL_NAME = "BAAI/bge-base-en-v1.5"


def main():
    query = sys.argv[1] if len(sys.argv) > 1 else "export project"
    top_k = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    category = sys.argv[3] if len(sys.argv) > 3 else None

    model = SentenceTransformer(MODEL_NAME, device="mps")
    client = chromadb.PersistentClient(path=os.path.abspath(DB_PATH))
    col = client.get_collection(COLLECTION)
    print(f"collection '{COLLECTION}': {col.count()} docs", file=sys.stderr)

    qvec = model.encode([query], normalize_embeddings=True).tolist()
    where = {"category": category} if category else None
    # fetch more then re-rank by exact cosine distance (HNSW recall)
    res = col.query(query_embeddings=qvec, n_results=max(top_k * 8, 40), where=where)

    for i in range(len(res["ids"][0])):
        meta = res["metadatas"][0][i]
        doc = res["documents"][0][i]
        dist = res["distances"][0][i]
        print(f"\n### {i + 1}. {meta.get('title', '?')}  (cosine sim: {1 - dist:.4f})")
        print(f"category: {meta.get('category', '')} | source: {meta.get('source', '')}")
        print(f"section: {meta.get('header_path', '')}")
        print(f"url: {meta.get('source_url', '')}")
        print(f"---\n{doc[:600]}")


if __name__ == "__main__":
    main()
