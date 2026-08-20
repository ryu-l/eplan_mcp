"""
Crawl the public EPLAN documentation on eplan.help and convert pages to
Markdown for local RAG index rebuild.

Sources:
  Part A - API system  : /en-us/Infoportal/Content/api/2026/*.html
                          (topic list from webindex.html, Innovasys help)
  Part B - User Guide   : /en-us/Infoportal/Content/Plattform/2026/Content/htm/**
                          (MadCap Flare help, parallel BFS from start pages)

Output:
  rebuild/raw/<sha1>.html     raw page cache
  rebuild/corpus/api/*.md     converted API pages
  rebuild/corpus/guide/*.md   converted User Guide pages
  rebuild/manifest.jsonl      one JSON line per page (metadata for indexing)
  rebuild/guide_state.json    BFS resume state
"""
import hashlib
import json
import os
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE = "https://www.eplan.help"
API_INDEX_URL = f"{BASE}/en-us/Infoportal/Content/api/2026/webindex.html"
API_DIR_URL = f"{BASE}/en-us/Infoportal/Content/api/2026/"
GUIDE_SEEDS = [
    f"{BASE}/en-us/Infoportal/Content/Plattform/2026/Content/htm/planninggui_k_start.htm",
    f"{BASE}/en-us/Infoportal/Content/Plattform/2026/Content/htm/cabinetgui_k_start.htm",
]
GUIDE_SCOPE = re.compile(
    r"^https://www\.eplan\.help/en-us/Infoportal/Content/"
    r"Plattform/[^/]+/Content/htm/"
)
GUIDE_MAX = 6000
SKIP_EXT = re.compile(r"\.(css|js|png|jpg|jpeg|gif|svg|ico|pdf|mp4|zip|woff2?|ttf|eot|xml|json|txt|map)$", re.I)

# eplan.help serves double-encoded UTF-8 in places (e.g. bullet "•" arrives as
# the literal characters "â€¢"). Map the common sequences back.
MOJIBAKE = {
    "â€¢": "•", "â€“": "–", "â€”": "—", "â€™": "'", "â€˜": "'",
    "â€œ": '"', "â€": '"', "â€¦": "…", "â†’": "→", "â†": "↑",
    "â€ƒ": " ", "Ã©": "é", "Ã¨": "è", "Ã¼": "ü", "Ã¶": "ö",
    "Ã¤": "ä", "ÃŸ": "ß", "Ã±": "ñ", "Ã¡": "á", "Ã³": "ó",
    "Ã­": "í", "Ãº": "ú", "Â·": "·", "Â°": "°", "Â²": "²", "Â³": "³",
}

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(ROOT, "raw")
CORPUS_API = os.path.join(ROOT, "corpus", "api")
CORPUS_GUIDE = os.path.join(ROOT, "corpus", "guide")
MANIFEST = os.path.join(ROOT, "manifest.jsonl")
GUIDE_STATE = os.path.join(ROOT, "guide_state.json")

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"})
LOCK = threading.Lock()
STATS = {"ok": 0, "failed": 0, "skipped": 0}
GUIDE_OK = 0
SEEN_MANIFEST = set()


def fix_mojibake(text):
    for bad, good in MOJIBAKE.items():
        if bad in text:
            text = text.replace(bad, good)
    return text


def norm_url(url):
    p = urlparse(url)
    return urlunparse((p.scheme, p.netloc, p.path, "", "", ""))


def fetch(url):
    """GET with retries; returns HTML text or None. Short timeout, 2 tries."""
    for attempt in range(2):
        try:
            r = SESSION.get(url, timeout=15)
            if r.status_code == 200:
                return r.text
            if r.status_code in (404, 410):
                return None
        except requests.RequestException:
            pass
        time.sleep(1.0 * (attempt + 1))
    return None


def sanitize(segment):
    s = re.sub(r'[\\/:*?"<>|]+', "_", segment).strip().strip(".")
    return s or "_"


def raw_key(url):
    return hashlib.sha1(url.encode()).hexdigest()


def load_or_store_raw(url, html):
    path = os.path.join(RAW_DIR, raw_key(url) + ".html")
    if os.path.exists(path):
        return open(path, encoding="utf-8", errors="replace").read()
    if html is None:
        return None
    with LOCK:
        os.makedirs(RAW_DIR, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
    return html


def breadcrumb_text(soup):
    container = soup.find("div", id="i-breadcrumbs-container") or soup.find("div", class_="i-breadcrumbs-container")
    if container:
        parts = [a.get_text(" ", strip=True) for a in container.find_all("a")]
        if parts:
            return parts
    return []


def extract_innovasys(html, url):
    """Return (title, breadcrumb, body_html)."""
    soup = BeautifulSoup(html, "lxml")
    title = soup.title.get_text(strip=True) if soup.title else ""
    crumb = breadcrumb_text(soup)
    for noise in soup.select("#i-in-this-topic-container, .i-in-this-topic-container"):
        noise.decompose()
    body = soup.find("div", id="i-body-content")
    if body is None:
        body = soup.find("div", class_="i-body-content")
    return title, crumb, str(body) if body else ""


def extract_flare(html, url):
    """MadCap Flare topic: return (title, breadcrumb, body_html)."""
    soup = BeautifulSoup(html, "lxml")
    title = soup.title.get_text(strip=True) if soup.title else ""
    crumb = []
    body_el = soup.body
    if body_el and body_el.get("data-mc-toc-path"):
        path = body_el["data-mc-toc-path"].replace("[%=System.LinkedTitle%]", "")
        crumb = [p.strip() for p in path.split("|") if p.strip()]
    if not crumb:
        for cls in soup.find_all(class_=re.compile(r"Breadcrumb", re.I)):
            txt = cls.get_text(" ", strip=True)
            if txt and len(txt) < 300:
                crumb = [p.strip() for p in txt.split(">") if p.strip()]
                break
    body = (soup.find("div", class_=re.compile(r"^body$|topic-body|MCBody", re.I))
            or soup.find("div", id=re.compile(r"body|topic", re.I)))
    if body is None:
        for tag in soup(["header", "footer", "nav", "script", "style", "noscript"]):
            tag.decompose()
        for div in soup.find_all("div", class_=re.compile(r"(nav|toc|menu|search|toolbar)", re.I)):
            div.decompose()
        body = soup.body or soup
    return title, crumb, str(body)


def html_to_md(body_html, title):
    md_text = md(body_html, heading_style="ATX", bullets="-", strip=["script", "style", "noscript"])
    md_text = fix_mojibake(md_text)
    md_text = re.sub(r"\n{3,}", "\n\n", md_text).strip()
    if not md_text:
        return ""
    return f"# {title}\n\n{md_text}"


def source_path(category_key, crumb, title):
    """Build the stable relative 'source' path mirroring the live index scheme.

    Live example: breadcrumb [Eplan API, API Reference, Actions, export]
                  -> "Api/Actions/export.md"
    """
    parts = list(crumb)
    if parts and parts[0].lower().startswith("eplan api"):
        parts = parts[1:]
    if parts and parts[0].lower() in ("api reference", "api_reference"):
        parts = parts[1:]
    if parts and parts[-1].lower() == title.lower():
        parts = parts[:-1]
    segments = [sanitize(p) for p in parts if p]
    segments = segments or ["misc"]
    return f"{category_key}/{'/'.join(segments)}/{sanitize(title)}.md"


def page_links(html, base_url):
    """In-scope page links found in an HTML document."""
    soup = BeautifulSoup(html, "lxml")
    out = set()
    for a in soup.find_all("a", href=True):
        abs_url = norm_url(urljoin(base_url, a["href"]))
        if not abs_url.startswith(BASE):
            continue
        if SKIP_EXT.search(abs_url):
            continue
        if GUIDE_SCOPE.match(abs_url):
            out.add(abs_url)
    return out


def convert_and_record(url, category, extractor, out_dir, html):
    """Convert fetched html to md and append manifest record. Returns True on success."""
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
    md_name = raw_key(url) + ".md"
    with open(os.path.join(out_dir, md_name), "w", encoding="utf-8") as fh:
        fh.write(markdown)
    record = {
        "url": url,
        "title": title,
        "category": category,
        "source": src,
        "source_url": url,
        "breadcrumb": crumb,
        "md_path": os.path.join(out_dir, md_name),
    }
    with LOCK:
        with open(MANIFEST, "a", encoding="utf-8") as mf:
            mf.write(json.dumps(record, ensure_ascii=False) + "\n")
    return True


def process_api(url):
    url = norm_url(url)
    if url in SEEN_MANIFEST:
        with LOCK:
            STATS["skipped"] += 1
        return
    html = fetch(url)
    html = load_or_store_raw(url, html)
    if html is None:
        with LOCK:
            STATS["failed"] += 1
        return
    ok = convert_and_record(url, "Api", extract_innovasys, CORPUS_API, html)
    with LOCK:
        STATS["ok" if ok else "failed"] += 1


def process_guide(url):
    """Fetch + convert one guide page; returns newly discovered in-scope links."""
    url = norm_url(url)
    if url in SEEN_MANIFEST:
        return set()
    html = fetch(url)
    html = load_or_store_raw(url, html)
    if html is None:
        return set()
    ok = convert_and_record(url, "User Guide", extract_flare, CORPUS_GUIDE, html)
    global GUIDE_OK
    with LOCK:
        STATS["ok" if ok else "failed"] += 1
        if ok:
            GUIDE_OK += 1
    return page_links(html, url)


def discover_api_urls():
    html = fetch(API_INDEX_URL)
    if html is None:
        raise SystemExit("cannot fetch webindex.html")
    soup = BeautifulSoup(html, "lxml")
    urls = set()
    for a in soup.find_all("a", href=True):
        abs_url = urljoin(API_INDEX_URL, a["href"])
        if SKIP_EXT.search(abs_url):
            continue
        if abs_url.startswith(API_DIR_URL) and abs_url.endswith(".html"):
            if "webindex.html" not in abs_url:
                urls.add(abs_url)
    return sorted(urls)


def crawl_api(urls):
    print(f"[api] {len(urls)} pages", flush=True)
    with ThreadPoolExecutor(max_workers=6) as pool:
        list(pool.map(process_api, urls))
    print(f"[api] done stats={dict(STATS)}", flush=True)


def crawl_guide():
    # resume state
    state = {"seen": [], "queue": []}
    if os.path.exists(GUIDE_STATE):
        state = json.load(open(GUIDE_STATE, encoding="utf-8"))
    seen = set(state["seen"])
    queue = state["queue"] or [norm_url(u) for u in GUIDE_SEEDS]
    while queue and GUIDE_OK < GUIDE_MAX:
        wave = queue[:300]
        queue = queue[300:]
        new_links = set()
        with ThreadPoolExecutor(max_workers=6) as pool:
            for result in pool.map(process_guide, wave):
                if result:
                    new_links.update(result)
        for link in new_links:
            if link not in seen:
                seen.add(link)
                queue.append(link)
        with open(GUIDE_STATE, "w", encoding="utf-8") as fh:
            json.dump({"seen": sorted(seen), "queue": queue}, fh)
        print(f"[guide] seen={len(seen)} queue={len(queue)} guide_ok={GUIDE_OK} "
              f"stats={dict(STATS)}", flush=True)
        time.sleep(0.3)
    print(f"[guide] done stats={dict(STATS)}", flush=True)


def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(CORPUS_API, exist_ok=True)
    os.makedirs(CORPUS_GUIDE, exist_ok=True)
    global SEEN_MANIFEST
    if os.path.exists(MANIFEST):
        SEEN_MANIFEST = {json.loads(l)["url"] for l in open(MANIFEST, encoding="utf-8") if l.strip()}
    print(f"manifest urls already recorded: {len(SEEN_MANIFEST)}", flush=True)

    crawl_api(discover_api_urls())
    crawl_guide()
    print(f"FINISHED stats={dict(STATS)}", flush=True)


if __name__ == "__main__":
    main()
