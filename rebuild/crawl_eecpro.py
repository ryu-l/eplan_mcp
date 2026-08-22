"""
Crawl the EPLAN EEC Pro 2026 user guide (MadCap Flare help) and append to the
rebuild corpus + manifest, so index.py picks it up on the next (re)build.

Topic list comes from the Flare-generated Sitemap.xml (complete topic
enumeration; BFS does not work here because the sidenav menu is JS-generated).
Reference size (official EEC Pro RAG): 1,648 pages; sitemap yields ~1,980.

Run: python crawl_eecpro.py
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
    BASE, RAW_DIR, MANIFEST, LOCK, STATS,
    fetch, norm_url, sanitize, raw_key, load_or_store_raw,
    extract_flare, html_to_md,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
CORPUS_EEC = os.path.join(ROOT, "corpus", "eecpro")
SITEMAP_URL = f"{BASE}/en-us/infoportal/content/eecpro/2026/Sitemap.xml"
SKIP_PATH = re.compile(r"/Print Only Topics/", re.I)
# 正文里的 Flare 面包屑与版权导航残留行
NOISE_LINE = re.compile(r"^\s*(You are here:?\s*.*|\[Info / Copyright\]\([^)]*\)\s*)$", re.I)

EEC_OK = 0


def discover_topics():
    xml_text = fetch(SITEMAP_URL)
    if xml_text is None:
        raise SystemExit("cannot fetch Sitemap.xml")
    root = ElementTree.fromstring(xml_text)
    urls = set()
    for loc in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
        u = norm_url(loc.text.strip())
        if not re.search(r"\.html?$", u):
            continue
        if SKIP_PATH.search(u):
            continue
        urls.add(u)
    return sorted(urls)


def convert_eec(url, html):
    """Convert one EEC Pro page; returns source path on success, else None."""
    title, crumb, body_html = extract_flare(html, url)
    if not title:
        title = os.path.basename(urlparse(url).path).rsplit(".", 1)[0]
    if not body_html:
        return None
    markdown = html_to_md(body_html, title)
    # 去除 "You are here:" 面包屑行与版权链接行
    markdown = "\n".join(
        l for l in markdown.splitlines() if not NOISE_LINE.match(l)
    )
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()
    # EEC Pro 有大量短参考页(单表/单段,~180 字符),阈值放宽到 60
    if len(markdown) < 60:
        return None
    parts = [sanitize(p) for p in crumb if p]
    if parts and parts[-1].lower() == title.lower():
        parts = parts[:-1]
    src = "EECPro/" + "/".join(parts or ["misc"]) + "/" + sanitize(title) + ".md"
    os.makedirs(CORPUS_EEC, exist_ok=True)
    md_path = os.path.join(CORPUS_EEC, raw_key(url) + ".md")
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
        with open(MANIFEST, "a", encoding="utf-8") as mf:
            mf.write(json.dumps(record, ensure_ascii=False) + "\n")
    return src


def process(url):
    global EEC_OK
    html = fetch(url)
    html = load_or_store_raw(url, html)
    if html is None:
        with LOCK:
            STATS["failed"] += 1
        return
    src = convert_eec(url, html)
    with LOCK:
        STATS["ok" if src else "failed"] += 1
        if src:
            EEC_OK += 1


def main():
    topics = discover_topics()
    print(f"sitemap 主题页: {len(topics)}", flush=True)

    # 清理之前失败 BFS 尝试写入的残留记录
    if os.path.exists(MANIFEST):
        lines = [l for l in open(MANIFEST, encoding="utf-8") if l.strip()]
        old_len = len(lines)
        lines = [l for l in lines
                 if json.loads(l).get("category") != "EEC Pro"]
        if len(lines) != old_len:
            with open(MANIFEST, "w", encoding="utf-8") as fh:
                fh.write("".join(lines))
            print(f"清理旧 EEC Pro 残留记录: {old_len - len(lines)} 条", flush=True)

    seen = set()
    if os.path.exists(MANIFEST):
        seen = {json.loads(l)["url"] for l in open(MANIFEST, encoding="utf-8") if l.strip()}
    todo = [u for u in topics if u not in seen]
    print(f"待抓取: {len(todo)} 页", flush=True)

    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = [pool.submit(process, u) for u in todo]
        done = 0
        for _ in futures:
            done += 1
            if done % 200 == 0 or done == len(todo):
                print(f"[eecpro] {done}/{len(todo)} ok={EEC_OK} stats={dict(STATS)}",
                      flush=True)
            time.sleep(0.02)
    print(f"[eecpro] DONE ok={EEC_OK} stats={dict(STATS)}", flush=True)


if __name__ == "__main__":
    main()
