"""
Crawl the EPLAN P8 2.9 documentation (api/2.9 + Plattform/2.9 user guide) for
the version-matched local database.

Same pipeline as the 2026 crawl:
  - api/2.9: webindex.html topic list + member-page link expansion (webindex
    only lists class-level pages), category "Api"
  - Plattform/2.9 guide: MadCap Flare, BFS from planning/cabinet GUI start
    pages, category "User Guide"

Writes corpus/api29/, corpus/guide29/ and manifest29.jsonl (separate from the
2026 manifest on purpose: the two databases are built independently).

Run: python crawl_29.py
"""
import hashlib
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse, urlunparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crawl import (  # noqa: E402
    BASE, SKIP_EXT, LOCK, STATS,
    fetch, norm_url, sanitize, raw_key, load_or_store_raw,
    extract_innovasys, extract_flare, html_to_md, source_path,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW29 = os.path.join(ROOT, "raw29")
CORPUS_API29 = os.path.join(ROOT, "corpus", "api29")
CORPUS_GUIDE29 = os.path.join(ROOT, "corpus", "guide29")
MANIFEST29 = os.path.join(ROOT, "manifest29.jsonl")
GUIDE_STATE29 = os.path.join(ROOT, "guide29_state.json")

API_INDEX = f"{BASE}/en-us/Infoportal/Content/api/2.9/webindex.html"
API_DIR = f"{BASE}/en-us/Infoportal/Content/api/2.9/"
GUIDE_SEEDS = [
    f"{BASE}/en-us/Infoportal/Content/Plattform/2.9/Content/htm/planninggui_k_start.htm",
    f"{BASE}/en-us/Infoportal/Content/Plattform/2.9/Content/htm/cabinetgui_k_start.htm",
]
GUIDE_SCOPE = re.compile(
    r"^https://www\.eplan\.help/en-us/Infoportal/Content/Plattform/2\.9/Content/htm/"
)
GUIDE_MAX = 4000
HREF_RE = re.compile(r'href="([^"]+\.html?)"', re.I)


def convert_and_record(url, category, extractor, out_dir, html):
    title, crumb, body_html = extractor(html, url)
    if not title:
        title = os.path.basename(urlparse(url).path).rsplit(".", 1)[0]
    if not body_html:
        return False
    markdown = html_to_md(body_html, title)
    if len(markdown) < 200:
        return False
    src = source_path("Api" if category == "Api" else "UserGuide", crumb, title)
    os.makedirs(out_dir, exist_ok=True)
    md_path = os.path.join(out_dir, raw_key(url) + ".md")
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(markdown)
    record = {
        "url": url,
        "title": title,
        "category": category,
        "source": src,
        "source_url": url,
        "breadcrumb": crumb,
        "md_path": md_path,
    }
    with LOCK:
        with open(MANIFEST29, "a", encoding="utf-8") as mf:
            mf.write(json.dumps(record, ensure_ascii=False) + "\n")
    return True


def process_api(url):
    if url in seen_manifest29:
        with LOCK:
            STATS["skipped"] += 1
        return
    html = fetch(url)
    html = load_or_store_raw29(url, html)
    if html is None:
        with LOCK:
            STATS["failed"] += 1
        return
    ok = convert_and_record(url, "Api", extract_innovasys, CORPUS_API29, html)
    with LOCK:
        STATS["ok" if ok else "failed"] += 1


def load_or_store_raw29(url, html):
    path = os.path.join(RAW29, raw_key(url) + ".html")
    if os.path.exists(path):
        return open(path, encoding="utf-8", errors="replace").read()
    if html is None:
        return None
    with LOCK:
        os.makedirs(RAW29, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
    return html


def discover_api_urls():
    html = fetch(API_INDEX)
    if html is None:
        raise SystemExit("cannot fetch api/2.9 webindex")
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml")
    urls = set()
    for a in soup.find_all("a", href=True):
        abs_url = norm_url(urljoin(API_INDEX, a["href"]))
        if SKIP_EXT.search(abs_url):
            continue
        if abs_url.startswith(API_DIR) and abs_url.endswith(".html"):
            if "webindex.html" not in abs_url:
                urls.add(abs_url)
    return sorted(urls)


def api_links_in(html, base_url):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml")
    out = set()
    for a in soup.find_all("a", href=True):
        abs_url = norm_url(urljoin(base_url, a["href"]))
        if abs_url.startswith(API_DIR) and not SKIP_EXT.search(abs_url):
            if "webindex.html" not in abs_url:
                out.add(abs_url)
    return out


def crawl_api():
    urls = discover_api_urls()
    print(f"[api29] webindex 页面: {len(urls)}", flush=True)
    with ThreadPoolExecutor(max_workers=6) as pool:
        list(pool.map(process_api, urls))
    # 链接扩展:成员页
    for round_no in range(1, 5):
        have = load_manifest29_urls()
        candidates = set()
        scanned = 0
        for url in have:
            p = os.path.join(RAW29, raw_key(url) + ".html")
            if not os.path.exists(p):
                continue
            scanned += 1
            candidates.update(api_links_in(
                open(p, encoding="utf-8", errors="replace").read(), url))
        new = sorted(candidates - have)
        print(f"[api29] 扩展 round {round_no}: 新页面 {len(new)}", flush=True)
        if not new:
            break
        with ThreadPoolExecutor(max_workers=6) as pool:
            list(pool.map(process_api, new))
    print(f"[api29] DONE 总页数 {len(load_manifest29_urls())} stats={dict(STATS)}",
          flush=True)


def process_guide(url):
    if url in seen_manifest29:
        return set()
    html = fetch(url)
    html = load_or_store_raw29(url, html)
    if html is None:
        return set()
    ok = convert_and_record(url, "User Guide", extract_flare, CORPUS_GUIDE29, html)
    with LOCK:
        STATS["ok" if ok else "failed"] += 1
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml")
    out = set()
    for a in soup.find_all("a", href=True):
        abs_url = norm_url(urljoin(url, a["href"]))
        if GUIDE_SCOPE.match(abs_url) and not SKIP_EXT.search(abs_url):
            out.add(abs_url)
    return out


def crawl_guide():
    state = {"seen": [], "queue": []}
    if os.path.exists(GUIDE_STATE29):
        state = json.load(open(GUIDE_STATE29, encoding="utf-8"))
    seen = set(state["seen"])
    queue = state["queue"] or [norm_url(u) for u in GUIDE_SEEDS]
    ok_before = STATS["ok"]
    while queue:
        wave = queue[:300]
        queue = queue[300:]
        new_links = set()
        with ThreadPoolExecutor(max_workers=6) as pool:
            for result in pool.map(process_guide, wave):
                if result:
                    new_links.update(result)
        for link in new_links:
            if link not in seen and link not in seen_manifest29:
                seen.add(link)
                queue.append(link)
        with open(GUIDE_STATE29, "w", encoding="utf-8") as fh:
            json.dump({"seen": sorted(seen), "queue": queue}, fh)
        print(f"[guide29] seen={len(seen)} queue={len(queue)} "
              f"ok={STATS['ok'] - ok_before} stats={dict(STATS)}", flush=True)
        time.sleep(0.3)
    print(f"[guide29] DONE stats={dict(STATS)}", flush=True)


def load_manifest29_urls():
    if not os.path.exists(MANIFEST29):
        return set()
    return {json.loads(l)["url"] for l in open(MANIFEST29, encoding="utf-8") if l.strip()}


def main():
    os.makedirs(RAW29, exist_ok=True)
    os.makedirs(CORPUS_API29, exist_ok=True)
    os.makedirs(CORPUS_GUIDE29, exist_ok=True)
    global seen_manifest29
    seen_manifest29 = load_manifest29_urls()
    print(f"manifest29 已有: {len(seen_manifest29)} 页", flush=True)
    crawl_api()
    crawl_guide()
    print(f"FINISHED manifest29 总页数: {len(load_manifest29_urls())} "
          f"stats={dict(STATS)}", flush=True)


seen_manifest29 = set()

if __name__ == "__main__":
    main()
