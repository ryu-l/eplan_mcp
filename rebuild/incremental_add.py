"""
增量嵌入:把"指定 manifest 里还没入库的页面"分块嵌入并 add 到现有 collection。

用途:补爬(backfill)后无需全量重建。sidecar 文件 indexed_md.txt 记录已入库的
md 路径;重跑自动跳过。

用法:
  python incremental_add.py --db-path <库路径> --manifest <manifest.jsonl> [--fresh-sidecar]

(默认 --manifest 对应 rebuild/manifest.jsonl;sidecar 按 db-path 区分存放)
"""
import argparse
import json
import os
import sys
import time
import uuid

import chromadb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from index import chunk_markdown  # noqa: E402
from sentence_transformers import SentenceTransformer  # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
COLLECTION = "eplan_docs"
MODEL_NAME = "BAAI/bge-base-en-v1.5"
BATCH = 256


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db-path", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--from-line", type=int, default=0,
                        help="manifest 中从第几行起视为新增(此前行视为已入库,"
                             "用于补爬后追加;0 表示用 sidecar 判断)")
    parser.add_argument("--fresh-sidecar", action="store_true",
                        help="忽略 sidecar,把 manifest 中全部页面都视为新增")
    args = parser.parse_args()

    records = [json.loads(l) for l in open(args.manifest, encoding="utf-8") if l.strip()]
    sidecar = os.path.join(ROOT, "indexed_md_" +
                           os.path.basename(os.path.normpath(args.db_path)) + ".txt")
    done = set()
    if args.from_line > 0:
        # 首次使用:把 from_line 之前的行写入 sidecar 作为"已入库"基线
        if not os.path.exists(sidecar):
            with open(sidecar, "w", encoding="utf-8") as sf:
                for r in records[:args.from_line]:
                    sf.write(r["md_path"] + "\n")
        done = {r["md_path"] for r in records[:args.from_line]}
    elif os.path.exists(sidecar) and not args.fresh_sidecar:
        done = {l.strip() for l in open(sidecar, encoding="utf-8") if l.strip()}
    if args.from_line > 0:
        todo = records[args.from_line:]
    else:
        todo = [r for r in records if r["md_path"] not in done]
    print(f"manifest {len(records)} 页,已入库基线 {len(done)},待嵌入 {len(todo)}",
          flush=True)
    if not todo:
        print("没有新增,退出。")
        return

    model = SentenceTransformer(MODEL_NAME, device="mps")
    client = chromadb.PersistentClient(path=os.path.abspath(args.db_path))
    col = client.get_collection(COLLECTION)
    print(f"当前库 count = {col.count()}", flush=True)

    t0 = time.time()
    batch_items = []
    added = 0
    def flush(items):
        nonlocal added
        if not items:
            return
        texts = [t for _, t in items]
        vectors = model.encode(texts, normalize_embeddings=True, batch_size=64).tolist()
        ids = [uuid.uuid4().hex for _ in texts]
        metas = [m for m, _ in items]
        col.add(ids=ids, embeddings=vectors, documents=texts, metadatas=metas)
        added += len(texts)
        print(f"  +{len(texts)} (累计 {added}/{len(todo)}, "
              f"{(time.time()-t0)/60:.1f} min)", flush=True)

    with open(sidecar, "a", encoding="utf-8") as sf:
        for rec in todo:
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
                batch_items.append((meta, chunk_text))
                if len(batch_items) >= BATCH:
                    flush(batch_items)
                    batch_items = []
            sf.write(md_path + "\n")
        flush(batch_items)
    print(f"DONE 新增 {added} 块,当前 count = {col.count()},"
          f"耗时 {(time.time()-t0)/60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
