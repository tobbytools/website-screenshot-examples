#!/usr/bin/env bash
# Full-page screenshots of two pages on desktop and mobile, returned as JSON in one HTTP call.
# Usage: APIFY_TOKEN=... ./screenshot.sh
set -euo pipefail
: "${APIFY_TOKEN:?Set APIFY_TOKEN (free account: https://console.apify.com/settings/integrations)}"

curl -sS -X POST \
  "https://api.apify.com/v2/acts/tobbyb~website-screenshot/run-sync-get-dataset-items" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
        "urls": ["https://example.com", "https://www.wikipedia.org"],
        "devices": ["desktop", "mobile"],
        "formats": ["png"],
        "fullPage": true
      }' | tee screenshots.json

# Each item has "screenshotUrl" (a signed link to the image) or "status": "error" with "howToFix".
