"""
Chunk crawled Markdown, embed with bge-base-en-v1.5 (same model as the live
Cloudflare index), and store into local ChromaDB.

Target: eplan-p8-mcp-server/chroma_db_sota  collection: eplan_docs
Metadata schema mirrors the live worker:
  title, category, source, source_url, header_path
Chunk text is stored as the chroma document.
"""
import argparse
import json
import os
import re
import time
import uuid

import chromadb
from sentence_transformers import SentenceTransformer

ROOT = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(ROOT, "manifest.jsonl")
DB_PATH = os.path.join(ROOT, "..", "eplan-p8-mcp-server", "chroma_db_sota")
COLLECTION = "eplan_docs"
MODEL_NAME = "BAAI/bge-base-en-v1.5"

MAX_CHUNK_WORDS = 450      # ~600 tokens per chunk
OVERLAP_WORDS = 60
MIN_CHUNK_WORDS = 30       # drop tiny fragments
BATCH = 256                # embedding batch size


def chunk_markdown(text, title):
    """Split markdown by headers; each section becomes a chunk.
    Returns list of (header_path, chunk_text)."""
    lines = text.splitlines()
    chunks = []
    cur_path = [title]
    cur_buf = []

    def flush(path, buf):
        body = "\n".join(buf).strip()
        body = re.sub(r"\n{3,}", "\n\n", body)
        if not body:
            return
        # Drop navigation boilerplate: "Reference" sections are pure markdown
        # link lists (Members/Namespace pages) with no real content.
        if path and path[-1].strip().lower() == "reference":
            return
        url_chars = len("".join(re.findall(r"\]\([^)]*\)", body)))
        if url_chars > 0.6 * len(body):
            return
        words = body.split()
        if len(words) <= MAX_CHUNK_WORDS:
            if len(words) >= MIN_CHUNK_WORDS:
                chunks.append((" > ".join(path), body))
            return
        # oversized section: split with overlap
        start = 0
        while start < len(words):
            part = " ".join(words[start:start + MAX_CHUNK_WORDS])
            if len(part.split()) >= MIN_CHUNK_WORDS:
                chunks.append((" > ".join(path), part))
            start += MAX_CHUNK_WORDS - OVERLAP_WORDS

    for line in lines:
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            flush(cur_path, cur_buf)
            level = len(m.group(1))
            heading = m.group(2).strip()
            cur_path = cur_path[:level] + [heading]
            cur_buf = [line]
        else:
            cur_buf.append(line)
    flush(cur_path, cur_buf)
    return chunks


def main():
    global FRESH
    parser = argparse.ArgumentParser()
    parser.add_argument("--fresh", action="store_true",
                        help="delete existing collection and rebuild from scratch")
    args = parser.parse_args()
    FRESH = args.fresh

    t0 = time.time()
    if not os.path.exists(MANIFEST):
        raise SystemExit(f"manifest not found: {MANIFEST}")

    records = [json.loads(l) for l in open(MANIFEST, encoding="utf-8") if l.strip()]
    print(f"manifest: {len(records)} pages", flush=True)

    print(f"loading model {MODEL_NAME} ...", flush=True)
    model = SentenceTransformer(MODEL_NAME, device="mps")

    # Build chunk list
    all_items = []  # (metadata, text)
    for rec in records:
        md_path = rec["md_path"]
        if not os.path.exists(md_path):
            continue
        text = open(md_path, encoding="utf-8").read()
        meta_base = {
            "title": rec["title"][:500] or "Untitled",
            "category": rec["category"],
            "source": rec["source"],
            "source_url": rec["url"],
        }
        for header_path, chunk_text in chunk_markdown(text, rec["title"]):
            meta = dict(meta_base)
            if header_path:
                meta["header_path"] = header_path[:800]
            all_items.append((meta, chunk_text))

    print(f"chunks: {len(all_items)}", flush=True)

    # Embed in batches
    client = chromadb.PersistentClient(path=os.path.abspath(DB_PATH))
    if FRESH:
        try:
            client.delete_collection(COLLECTION)
            print("deleted existing collection (--fresh)", flush=True)
        except Exception:
            pass
    col = client.get_or_create_collection(
        COLLECTION, metadata={"hnsw:space": "cosine"}
    )
    print(f"existing count before indexing: {col.count()}", flush=True)

    texts = [t for _, t in all_items]
    total_embedded = 0
    for i in range(0, len(texts), BATCH):
        batch_texts = texts[i:i + BATCH]
        vectors = model.encode(
            batch_texts, normalize_embeddings=True, batch_size=64
        ).tolist()
        ids = [uuid.uuid4().hex for _ in batch_texts]
        metas = [m for m, _ in all_items[i:i + BATCH]]
        col.add(ids=ids, embeddings=vectors, documents=batch_texts, metadatas=metas)
        total_embedded += len(batch_texts)
        if total_embedded % (BATCH * 10) < BATCH or total_embedded == len(texts):
            print(f"embedded {total_embedded}/{len(texts)} "
                  f"({(time.time() - t0) / 60:.1f} min elapsed)", flush=True)

    print(f"DONE count={col.count()} elapsed={(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
