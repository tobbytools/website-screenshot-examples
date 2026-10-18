"""Visual change detection: run this on a schedule (cron, GitHub Actions, or an Apify Schedule).

The first run saves a baseline. Every later run with the same monitor name compares each page
with the previous run and reports the % of pixels changed plus a red-highlighted diff image.

Usage:
    export APIFY_TOKEN=...
    python visual_monitor.py --name competitors https://stripe.com/pricing https://vercel.com/pricing
Exit code 2 if any page changed by more than the threshold (useful in CI).
"""
import argparse
import os
import sys

from apify_client import ApifyClient

p = argparse.ArgumentParser()
p.add_argument("urls", nargs="+")
p.add_argument("--name", required=True, help="monitor name; keep it the same between runs")
p.add_argument("--threshold", default="1", help="% of pixels that must differ to count as changed")
args = p.parse_args()

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("tobbyb/website-screenshot").call(run_input={
    "urls": args.urls,
    "devices": ["desktop"],
    "formats": ["jpeg"],
    "changeDetectionName": args.name,
    "changeThresholdPercent": args.threshold,  # the input field is a string
    "saveDiffImage": True,
})

changed = 0
# apify-client 1.x/2.x returns a dict, 3.x returns a model object
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
for item in client.dataset(dataset_id).iterate_items():
    ch = item.get("change") or {}
    status = ch.get("status") or item.get("status")
    print(f"{item.get('url')}: {status} {ch.get('diffPercent') if ch.get('diffPercent') is not None else ''}")
    if ch.get("changed"):
        changed += 1
        print(f"  diff image: {ch.get('diffImageUrl')}")
sys.exit(2 if changed else 0)
