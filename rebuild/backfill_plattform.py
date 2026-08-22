"""
用 Plattform Sitemap.xml 补齐 BFS 漏爬的用户指南页(覆盖率核验后的补爬)。

输入:/tmp/pf26_missing.txt、/tmp/pf29_missing.txt(或命令行参数给出的清单文件)
2026 缺失页 -> manifest.jsonl + corpus/guide/
2.9  缺失页 -> manifest29.jsonl + corpus/guide29/
之后用 incremental_add.py 把新页的块增量嵌入对应 chroma 库。

Run: python backfill_plattform.py
"""
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crawl import fetch, extract_flare, html_to_md, raw_key, load_or_store_raw, LOCK, STATS  # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW26 = os.path.join(ROOT, "raw")
RAW29 = os.path.join(ROOT, "raw29")
MISSING26 = "/tmp/pf26_missing.txt"
MISSING29 = "/tmp/pf29_missing.txt"


def wwwify(url):
    """统一 host 为 www.eplan.help"""
    p = urlparse(url)
    host = "www.eplan.help"
    return p._replace(netloc=host, scheme="https").geturl()


def convert_and_append(url, html, corpus_dir, manifest_file, raw_dir):
    from crawl import sanitize
    from crawl import source_path
    title, crumb, body_html = extract_flare(html, url)
    if not title:
        title = os.path.basename(urlparse(url).path).rsplit(".", 1)[0]
    if not body_html:
        return False
    markdown = html_to_md(body_html, title)
    if len(markdown) < 200:
        return False
    src = source_path("UserGuide", crumb, title)
    os.makedirs(corpus_dir, exist_ok=True)
    md_path = os.path.join(corpus_dir, raw_key(url) + ".md")
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(markdown)
    record = {
        "url": url,
        "title": title,
        "category": "User Guide",
        "source": src,
        "source_url": url,
        "breadcrumb": crumb,
        "md_path": md_path,
    }
    with LOCK:
        with open(manifest_file, "a", encoding="utf-8") as mf:
            mf.write(json.dumps(record, ensure_ascii=False) + "\n")
    return True


def process(url, corpus_dir, manifest_file, raw_dir):
    cache_key_url = wwwify(url)
    # 断点续跑:该页已转换成功则跳过
    md_path = os.path.join(corpus_dir, raw_key(cache_key_url) + ".md")
    if os.path.exists(md_path):
        with LOCK:
            STATS["skipped"] += 1
        return
    try:
        html = fetch(url)
        # 缓存(裸域名与 www 视为同一页,统一按 www 键)
        if html is None:
            cached = os.path.join(raw_dir, raw_key(cache_key_url) + ".html")
            if os.path.exists(cached):
                html = open(cached, encoding="utf-8", errors="replace").read()
        if html is None:
            with LOCK:
                STATS["failed"] += 1
            return
        with LOCK:
            os.makedirs(raw_dir, exist_ok=True)
            with open(os.path.join(raw_dir, raw_key(cache_key_url) + ".html"), "w",
                      encoding="utf-8") as fh:
                fh.write(html)
        ok = convert_and_append(cache_key_url, html, corpus_dir, manifest_file, raw_dir)
        with LOCK:
            STATS["ok" if ok else "failed"] += 1
    except Exception as exc:  # noqa: BLE001
        with LOCK:
            STATS["failed"] += 1
            with open("/Users/mac/program/eplan-rag-mcp/rebuild/backfill_errors.log",
                      "a", encoding="utf-8") as ef:
                ef.write(f"{cache_key_url}\t{type(exc).__name__}: {exc}\n")


def run(missing_file, corpus_dir, manifest_file, raw_dir, label):
    if not os.path.exists(missing_file):
        print(f"[{label}] 清单不存在,跳过: {missing_file}")
        return
    urls = [wwwify(u.strip()) for u in open(missing_file, encoding="utf-8") if u.strip()]
    print(f"[{label}] 补爬 {len(urls)} 页 ...", flush=True)
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = [pool.submit(process, u, corpus_dir, manifest_file, raw_dir) for u in urls]
        done = 0
        for f in futures:
            f.result()  # 让异常浮出(process 内部已捕获并计数)
            done += 1
            if done % 200 == 0 or done == len(urls):
                print(f"[{label}] {done}/{len(urls)} stats={dict(STATS)}", flush=True)
            time.sleep(0.02)
    print(f"[{label}] DONE stats={dict(STATS)}", flush=True)


def main():
    run(MISSING26, os.path.join(ROOT, "corpus", "guide"),
        os.path.join(ROOT, "manifest.jsonl"), RAW26, "plattform26")
    run(MISSING29, os.path.join(ROOT, "corpus", "guide29"),
        os.path.join(ROOT, "manifest29.jsonl"), RAW29, "plattform29")


if __name__ == "__main__":
    main()
