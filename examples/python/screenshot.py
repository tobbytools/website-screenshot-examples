"""Bulk full-page screenshots from a list of URLs or a sitemap, saved as files.

Usage:
    pip install -r requirements.txt
    export APIFY_TOKEN=...
    python screenshot.py https://example.com https://www.wikipedia.org
    python screenshot.py --sitemap https://crawlee.dev/sitemap.xml --max 5
"""
import argparse
import os
import pathlib
import urllib.parse
import urllib.request

from apify_client import ApifyClient

p = argparse.ArgumentParser()
p.add_argument("urls", nargs="*", default=[])
p.add_argument("--sitemap", action="append", default=[])
p.add_argument("--max", type=int, default=10, help="max pages taken from sitemaps")
p.add_argument("--device", action="append", default=None, help="desktop, desktop-hd, laptop, tablet, mobile")
args = p.parse_args()
if not args.urls and not args.sitemap:
    args.urls = ["https://example.com"]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("tobbyb/website-screenshot").call(run_input={
    "urls": args.urls,
    "sitemapUrls": args.sitemap,
    "maxSitemapUrls": args.max,
    "devices": args.device or ["desktop"],
    "formats": ["png"],
    "fullPage": True,
})

out = pathlib.Path("screenshots")
out.mkdir(exist_ok=True)
# apify-client 1.x/2.x returns a dict, 3.x returns a model object
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
for item in client.dataset(dataset_id).iterate_items():
    if item.get("status") != "ok":
        print(f"SKIPPED {item.get('url')}: {item.get('errorTitle')} -> {item.get('howToFix')}")
        continue
    host = urllib.parse.urlparse(item["url"]).hostname
    name = out / f"{host}-{item['device']}-{abs(hash(item['url'])) % 10**6}.png"
    urllib.request.urlretrieve(item["screenshotUrl"], name)
    print(f"{name}  {item['imageWidth']}x{item['imageHeight']}  complete={item['fullPageComplete']}")
