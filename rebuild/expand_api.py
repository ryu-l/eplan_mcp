"""
Expand the API crawl: webindex.html only lists class-level pages, but the
individual member pages (Methods / Properties / Events overloads, linked
from the *_members.html list pages) are missing.

Scans all cached raw pages for in-scope api/2026 links, fetches the missing
ones, and iterates until no new pages are discovered.
"""
import hashlib
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crawl import (  # noqa: E402
    BASE, API_DIR_URL, RAW_DIR, CORPUS_API, MANIFEST, SKIP_EXT,
    fetch, load_or_store_raw, convert_and_record, extract_innovasys,
    norm_url, raw_key, LOCK, STATS,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
HREF_RE = re.compile(r'href="([^"]+\.html?)"', re.I)


def load_manifest_urls():
    if not os.path.exists(MANIFEST):
        return set()
    return {json.loads(l)["url"] for l in open(MANIFEST, encoding="utf-8") if l.strip()}


def scan_cached_links():
    """Discover candidate api/2026 links from every cached raw page."""
    urls = load_manifest_urls()
    candidates = set()
    scanned = 0
    for url in urls:
        path = os.path.join(RAW_DIR, raw_key(url) + ".html")
        if not os.path.exists(path):
            continue
        scanned += 1
        html = open(path, encoding="utf-8", errors="replace").read()
        for href in HREF_RE.findall(html):
            abs_url = norm_url(urljoin(url, href))
            if not abs_url.startswith(API_DIR_URL):
                continue
            if SKIP_EXT.search(abs_url):
                continue
            if "webindex.html" in abs_url:
                continue
            candidates.add(abs_url)
    print(f"scanned {scanned} cached pages, found {len(candidates)} candidate urls",
          flush=True)
    return candidates


def fetch_new(url):
    html = fetch(url)
    html = load_or_store_raw(url, html)
    if html is None:
        with LOCK:
            STATS["failed"] += 1
        return None
    ok = convert_and_record(url, "Api", extract_innovasys, CORPUS_API, html)
    with LOCK:
        STATS["ok" if ok else "failed"] += 1
    return html


def main():
    for round_no in range(1, 6):
        before = load_manifest_urls()
        candidates = scan_cached_links()
        new = sorted(candidates - before)
        print(f"round {round_no}: {len(new)} new pages to fetch", flush=True)
        if not new:
            print("converged.", flush=True)
            break
        with ThreadPoolExecutor(max_workers=6) as pool:
            list(pool.map(fetch_new, new))
        after = load_manifest_urls()
        print(f"round {round_no} done: manifest {len(before)} -> {len(after)}, "
              f"stats={dict(STATS)}", flush=True)
        time.sleep(0.5)
    total = len(load_manifest_urls())
    print(f"FINISHED total manifest pages: {total}", flush=True)


if __name__ == "__main__":
    main()
