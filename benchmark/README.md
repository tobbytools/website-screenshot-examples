> Disclosure: "Ours" is our own Actor, [tobbyb/website-screenshot](https://apify.com/tobbyb/website-screenshot). Competitor runs used each Actor's documented best full-page settings (see the run settings below). Run IDs are listed so the Apify team or the Actor authors can check them.

# 30-URL head-to-head (Apify platform, 2026-10-18)
Ours = build 0.1.4 run M1v8KzXxrMMEQAprU (2 GB) + build 0.1.5 run OClpKckmw6o6QzpFF for getemoji/MDN (those 2 were lost to the old watchdog bug in 0.1.4).
apify/screenshot-url = run MjQoe0cK5DOmOn0GX (png, viewportWidth 1440, scrollToBottom; I aborted it at 41 min for budget after 29/30 URLs).
cheapapi/website-screenshot-api = run j23KS5AEjJrQQJuOc (fullPage, desktop_1440, jpeg q85).
Heights for every capture: [`heights.json`](heights.json). URL list: [`sites30.txt`](sites30.txt). Side-by-side examples: [`getemoji-compare.jpg`](getemoji-compare.jpg) (emoji fonts, consent pop-up) and [`vercel-compare.jpg`](vercel-compare.jpg) (100vh layout: ours complete, apify repeats the fixed hero over the footer, cheapapi's lower half is blank). The full set of 30 side-by-side sheets (12 MB of third-party page images) is kept out of this repo; open an issue if you want it.
Verdict basis: ✅ complete and visually correct; ◐ captured but with a visible defect; ❌ wrong, truncated or blocked. Rows marked (h) were judged on captured height vs. true page height only (no visual inspection); the others were inspected visually.

| # | URL | Ours | apify/screenshot-url | cheapapi |
|---|---|---|---|---|
| 0 | stripe.com | ✅ 15,455 px | ◐ large blank sections (lazy/animated content never rendered) | ✅ 15,056 px |
| 1 | theguardian.com | ✅ 22,016 px (empty grey ad bands) | ✅ 20,502 px (ads shown) | ❌ truncated at 1,440 px |
| 2 | bbc.com (h) | ✅ 13,832 | ✅ 13,814 | ✅ 13,848 |
| 3 | en.wikipedia Emoji | ✅ 22,953 | ✅ 22,868 | ✅ 22,265 (narrow layout) |
| 4 | github.com (h) | ✅ | ✅ | ✅ |
| 5 | apple.com (h) | ✅ | ✅ | ✅ |
| 6 | linear.app (h) | ✅ | ✅ | ✅ |
| 7 | vercel.com | ✅ 5,930 | ◐ fixed hero repeated over the footer | ❌ lower half blank |
| 8 | tailwindcss.com (h) | ✅ | ✅ | ✅ |
| 9 | notion.com (h) | ✅ | ✅ | ✅ |
| 10 | airbnb.com | ✅ 4 rows of listings | ◐ only 1 row loaded | ✅ 2 rows |
| 11 | medium.com | ⚠ BLOCKED error item, not charged | ❌ 1,080 px challenge page | ❌ 1,440 px challenge page |
| 12 | dev.to | ✅ 5,796 | ✅ 20,699 (infinite feed) | ✅ |
| 13 | news.ycombinator.com (h) | ✅ | ✅ | ✅ |
| 14 | smashingmagazine.com (h) | ✅ | ✅ | ✅ |
| 15 | unsplash.com | ⚠ HTTP_401 error item, not charged | ❌ no output (stuck retrying) | ❌ bot-check page |
| 16 | pexels.com | ✅ 4,583 (feed) | ✅ 16,385 (feed) | ❌ 1,440 px blocked page |
| 17 | getemoji.com | ✅ 23,769, colour emoji | ❌ monochrome/box emoji + cookie dialog | ❌ consent modal, truncated 1,440 |
| 18 | emojipedia.org | ◐ "Support Emoji Content" (adblock) modal over content | ◐ cookie modal over the lower half | ◐ consent modal |
| 19 | ja.wikipedia (CJK) (h) | ✅ 5,026 | ✅ 5,049 | ✅ 4,964 |
| 20 | shopify.com (h) | ✅ | ✅ | ✅ |
| 21 | figma.com (h) | ✅ | ✅ | ✅ |
| 22 | mozilla.org | ✅ 7,799 | ◐ rendered 800 px wide | ✅ |
| 23 | developer.mozilla.org (h) | ✅ 18,629 | ✅ 18,825 | ❌ truncated 1,440 |
| 24 | booking.com | ◐ grey skeleton placeholders | ◐ skeletons, 800 px wide | ◐ sign-in modal over content |
| 25 | spiegel.de | ◐ capped at the default maxHeight 30,000 of 34,356 px (flagged fullPageComplete:false) | ❌ cookie wall only (1,080 px) | ◐ 34,367 px but most images missing |
| 26 | lemonde.fr | ✅ 7,348 | ◐ consent modal in footer area | ✅ |
| 27 | ikea.com | ✅ 14,798 | ✅ 15,706 | ❌ truncated 1,440 |
| 28 | wired.com (h) | ✅ 7,095 | ✅ 8,780 | ✅ 7,739 |
| 29 | theverge.com | ◐ empty ad band + some blank image placeholders | ✅ (dark theme) | ❌ truncated 1,440 |

**Totals (30 URLs):** Ours **24 ✅ / 4 ◐ / 0 ❌**, plus 2 bot-blocked sites returned as free error items. apify/screenshot-url **19 ✅ / 7 ◐ / 4 ❌**. cheapapi **18 ✅ / 3 ◐ / 9 ❌**.
**Full-page completeness on reachable pages:** ours 27/28 (spiegel deliberately capped and flagged), apify 25/28, cheapapi 21/28.
**Speed/cost on the platform:** ours 652 s at 2 GB for 30 URLs, $0.075; apify more than 2,488 s at 2 GB for 29 URLs, $0.318 (aborted); cheapapi 258 s at 4 GB, $0.087 including its event fees.


## Competitor run settings
- apify/screenshot-url: `{"urls":[...], "format":"png", "waitUntil":"load", "delay":0, "viewportWidth":1440, "scrollToBottom":true}`
- cheapapi/website-screenshot-api: `{"url":..., "urls":[...], "fullPage":true, "device":"desktop_1440", "format":"jpeg", "quality":85}`
- Ours: `{"urls":[...], "devices":["desktop"], "formats":["jpeg"], "fullPage":true}` at 2 GB.

## Limits of this test
- One run per tool, from Apify's datacenter, on one day. Sites change; rerun before relying on it.
- 13 of 30 rows (marked (h)) were judged only by captured height vs. true page height.
- We stopped the apify/screenshot-url run at 41 minutes for budget (29 of 30 URLs done); it is scored on those 29.
- Quality was compared only between these three Apify Actors, not against hosted screenshot APIs. The [pricing comparison](pricing.md) compares list prices only.
