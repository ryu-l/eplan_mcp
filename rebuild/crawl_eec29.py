"""
Crawl the EPLAN EEC Pro 2.9 user guide (MadCap Flare help) for the
version-matched 2.9 database. Same sitemap-driven pipeline as crawl_eecpro.py.

Writes corpus/eec29/ and appends to manifest29.jsonl (category "EEC Pro").

Run: python crawl_eec29.py
"""
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
from xml.etree import ElementTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crawl import (  # noqa: E402
    BASE, LOCK, STATS,
    fetch, norm_url, sanitize, raw_key, load_or_store_raw,
    extract_flare, html_to_md,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
CORPUS_EEC29 = os.path.join(ROOT, "corpus", "eec29")
MANIFEST29 = os.path.join(ROOT, "manifest29.jsonl")
SITEMAP_URL = f"{BASE}/en-us/infoportal/content/eecpro/2.9/Sitemap.xml"
SKIP_PATH = re.compile(r"/Print Only Topics/", re.I)
NOISE_LINE = re.compile(r"^\s*(You are here:?\s*.*|\[Info / Copyright\]\([^)]*\)\s*)$", re.I)

EEC_OK = 0


def discover_topics():
    xml_text = fetch(SITEMAP_URL)
    if xml_text is None:
        raise SystemExit("cannot fetch Sitemap.xml (eecpro 2.9)")
    root = ElementTree.fromstring(xml_text)
    urls = set()
    for loc in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
        u = norm_url(loc.text.strip())
        if not re.search(r"\.html?$", u):
            continue
        if SKIP_PATH.search(u):
            continue
        # sitemap 是过期的(指向已下架的 2.8 路径);实测 2.9 主题以相同文件名
        # 存活在 /Infoportal/Content/EECPro/2.9/Content/htm/ 下 —— 重写路径
        fn = u.rsplit("/", 1)[-1]
        u = f"{BASE}/en-us/Infoportal/Content/EECPro/2.9/Content/htm/{fn}"
        urls.add(u)
    return sorted(urls)


def convert_eec(url, html):
    title, crumb, body_html = extract_flare(html, url)
    if not title:
        title = os.path.basename(urlparse(url).path).rsplit(".", 1)[0]
    if not body_html:
        return None
    markdown = html_to_md(body_html, title)
    markdown = "\n".join(
        l for l in markdown.splitlines() if not NOISE_LINE.match(l)
    )
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()
    if len(markdown) < 60:
        return None
    parts = [sanitize(p) for p in crumb if p]
    if parts and parts[-1].lower() == title.lower():
        parts = parts[:-1]
    src = "EECPro/" + "/".join(parts or ["misc"]) + "/" + sanitize(title) + ".md"
    os.makedirs(CORPUS_EEC29, exist_ok=True)
    md_path = os.path.join(CORPUS_EEC29, raw_key(url) + ".md")
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(markdown)
    record = {
        "url": url,
        "title": title,
        "category": "EEC Pro",
        "source": src,
        "source_url": url,
        "breadcrumb": crumb,
        "md_path": md_path,
    }
    with LOCK:
        with open(MANIFEST29, "a", encoding="utf-8") as mf:
            mf.write(json.dumps(record, ensure_ascii=False) + "\n")
    return src


def process(url):
    global EEC_OK
    html = fetch(url)
    html = load_or_store_raw29(url, html)
    if html is None:
        with LOCK:
            STATS["failed"] += 1
        return
    src = convert_eec(url, html)
    with LOCK:
        STATS["ok" if src else "failed"] += 1
        if src:
            EEC_OK += 1


def load_or_store_raw29(url, html):
    raw_dir = os.path.join(ROOT, "raw29")
    path = os.path.join(raw_dir, raw_key(url) + ".html")
    if os.path.exists(path):
        return open(path, encoding="utf-8", errors="replace").read()
    if html is None:
        return None
    with LOCK:
        os.makedirs(raw_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
    return html


def main():
    topics = discover_topics()
    print(f"eecpro/2.9 sitemap 主题页: {len(topics)}", flush=True)
    seen = set()
    if os.path.exists(MANIFEST29):
        seen = {json.loads(l)["url"] for l in open(MANIFEST29, encoding="utf-8") if l.strip()}
    todo = [u for u in topics if u not in seen]
    print(f"待抓取: {len(todo)} 页", flush=True)
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = [pool.submit(process, u) for u in todo]
        done = 0
        for _ in futures:
            done += 1
            if done % 200 == 0 or done == len(todo):
                print(f"[eec29] {done}/{len(todo)} ok={EEC_OK} stats={dict(STATS)}",
                      flush=True)
            time.sleep(0.02)
    print(f"[eec29] DONE ok={EEC_OK} stats={dict(STATS)}", flush=True)


if __name__ == "__main__":
    main()
