"""
Re-convert cached raw HTML -> Markdown using the latest extractors
(mojibake fixes, Flare toc-path breadcrumbs). No network access needed.
Rewrites corpus md files and manifest.jsonl atomically.
"""
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crawl import (  # noqa: E402
    RAW_DIR, MANIFEST, extract_innovasys, extract_flare,
    html_to_md, source_path,
)

ROOT = os.path.dirname(os.path.abspath(__file__))


def main():
    if not os.path.exists(MANIFEST):
        raise SystemExit("no manifest yet")
    records = [json.loads(l) for l in open(MANIFEST, encoding="utf-8") if l.strip()]
    print(f"records: {len(records)}")

    out_records = []
    stats = {"ok": 0, "bad": 0}
    for rec in records:
        url = rec["url"]
        key = hashlib.sha1(url.encode()).hexdigest()
        raw_path = os.path.join(RAW_DIR, key + ".html")
        if not os.path.exists(raw_path):
            stats["bad"] += 1
            out_records.append(rec)
            continue
        html = open(raw_path, encoding="utf-8", errors="replace").read()
        is_api = "/Content/api/" in url
        extractor = extract_innovasys if is_api else extract_flare
        title, crumb, body_html = extractor(html, url)
        if not title:
            title = rec.get("title") or os.path.basename(url).rsplit(".", 1)[0]
        if not body_html:
            stats["bad"] += 1
            out_records.append(rec)
            continue
        markdown = html_to_md(body_html, title)
        if len(markdown) < 200:
            stats["bad"] += 1
            out_records.append(rec)
            continue
        src = source_path("Api" if is_api else "UserGuide", crumb, title)
        md_path = rec["md_path"]
        with open(md_path, "w", encoding="utf-8") as fh:
            fh.write(markdown)
        out_records.append({
            "url": url,
            "title": title,
            "category": rec["category"],
            "source": src,
            "source_url": url,
            "breadcrumb": crumb,
            "md_path": md_path,
        })
        stats["ok"] += 1

    tmp = MANIFEST + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        for r in out_records:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(tmp, MANIFEST)
    print(f"DONE {stats}")


if __name__ == "__main__":
    main()
