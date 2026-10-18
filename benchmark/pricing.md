# Pro screenshot API pricing (checked 2026-10-18, ~14:30 EDT)

Source: public pricing pages read on 2026-10-18 (read from each provider's public pricing page). Prices are USD, monthly billing unless noted, excluding VAT. "Effective $/shot" = plan price ÷ included screenshots, i.e. the **best case when you use the whole quota**. Nothing here was tested for quality; these are list prices only.

Ours: **tobbyb/website-screenshot = $0.004 per screenshot file** (pay per event; one URL × device × format; full page included, failed URLs free; no subscription, no start fee).

| Provider | Plan | $/month | Included | Effective $/shot | Full page counts as 1? | Over quota / PAYG |
|---|---|---|---|---|---|---|
| ScreenshotOne | Free | 0 | 100 | – | – | – |
| ScreenshotOne | **Basic (entry)** | 17 | 2,000 | **$0.0085** | Yes as far as stated: full page listed as an included feature; quota counts successful, non-cached renders | $0.009 per extra |
| ScreenshotOne | Growth (mid) | 79 | 10,000 | $0.0079 | same | $0.006 per extra |
| ScreenshotOne | Scale | 259 | 50,000 | $0.0052 | same | $0.004 per extra |
| Urlbox | Lo-Fi | 19 | 2,000 | $0.0095 | Not always: 1 render per 30 s of render time and per 5 MB of file | Auto-upgrade to next tier. Lo-Fi = "websites you own", only low-quality thumbnails of 3rd-party sites |
| Urlbox | **Hi-Fi (entry for 3rd-party sites)** | 49 | 5,000 | **$0.0098** | same rule (file limit 10 MB, 90 s timeout) | Auto-upgrade to next tier |
| Urlbox | Ultra (mid) | 99 | 15,000 | $0.0066 | same rule | Auto-upgrade |
| Urlbox | Business | 495 base | – | $0.003 | same rule | $3 per 1,000 renders |
| ScreenshotAPI.net | **Essential (entry)** | 9 (shown as a discount from a struck-through $20) | 1,000 | **$0.009** ($0.020 at $20) | Full-page screenshot listed in the plan; counting not stated | Not readable (FAQ answer not in page HTML) |
| ScreenshotAPI.net | Startup (mid) | 29 (struck-through $35) | 10,000 | $0.0029 | not stated | not readable |
| ScreenshotAPI.net | Business | 175 (struck-through $200) | 100,000 | $0.00175 | not stated | not readable |
| ApiFlash | Free | 0 | 100 | – | – | – |
| ApiFlash | **Lite (entry)** | 7 | 1,000 | **$0.007** | Yes: quota = successful API calls; full page is a parameter | Not stated on pricing page |
| ApiFlash | Medium (mid) | 35 | 10,000 | $0.0035 | same | not stated |
| ApiFlash | Large | 180 | 100,000 | $0.0018 | same | not stated |
| ScrapingBee (scraping API with screenshots) | Hobby (entry) | 19 | 75,000 credits = 15,000 screenshots (screenshots need render_js = 5 credits) | $0.0013 (or $0.0063 with premium proxy, 25 credits) | Yes: `screenshot_full_page` has no extra credit cost stated | Not stated on pricing page |
| ScrapingBee | Freelance (mid) | 49 | 250,000 credits = 50,000 screenshots | $0.0010 | same | not stated |
| Browserless (headless browser hosting, not a screenshot API) | Prototyping | 25 billed annually (monthly price not in page HTML; annual "saves 30%") | 20k units (1 unit = up to 30 s of browser time) | ~$0.00125 if 1 shot = 1 unit | Time-based, not per shot | $0.0020 per unit overage |
| Browserless | Starter | 140 billed annually | 180k units | ~$0.0008 | time-based | $0.0017 per unit |

URLs (all read 2026-10-18):
- ScreenshotOne: https://screenshotone.com/pricing/ (and https://screenshotone.com/docs/options/ for "failed requests are not counted", "cached requests don't count")
- Urlbox: https://urlbox.com/pricing
- ScreenshotAPI.net: https://screenshotapi.net/pricing (top cards show $9 / $29 / $175 with $20 / $35 / $200 struck through; the feature table with "Monthly" selected shows $9 / $29 / $175; "2 Month Free on Yearly Plan")
- ApiFlash: https://apiflash.com/ (pricing section; https://apiflash.com/pricing returns 404) and https://apiflash.com/documentation (quota = API calls)
- ScrapingBee: https://www.scrapingbee.com/pricing/ and https://www.scrapingbee.com/documentation/ ("render_js … costs 5 credits per request", "Screenshots are only available when using render_js=True", premium proxy 25 credits with JS)
- Browserless: https://www.browserless.io/pricing (annual prices only in static HTML)

## What the data supports

Per-shot list price at the entry plan (full quota used), ours $0.004 as a share of theirs:
- ScreenshotOne Basic $0.0085 → ours is **47%** (less than half)
- Urlbox Hi-Fi $0.0098 → **41%** (Lo-Fi $0.0095 → 42%)
- ScreenshotAPI.net Essential $0.009 → **44%**
- ApiFlash Lite $0.007 → **57%** (cheaper, but NOT half)
- ScrapingBee Hobby $0.0013 → ours is **3× more** per shot if you use the quota
- Mid plans: ApiFlash Medium ($0.0035) and ScreenshotAPI.net Startup ($0.0029) are cheaper per shot than us; ScreenshotOne Growth ($0.0079) and Urlbox Ultra ($0.0066) are not.

Monthly bill at low volume (no subscription vs. cheapest plan that covers the volume, from the table above):

| Screenshots/month | Ours | ApiFlash | ScreenshotAPI.net | ScreenshotOne | Urlbox (Hi-Fi) | ScrapingBee |
|---|---|---|---|---|---|---|
| 250 | $1 | $7 | $9 | $17 | $49 | $19 |
| 1,000 | $4 | $7 | $9 | $17 | $49 | $19 |
| 2,000 | $8 | $35 (Medium; Lite overage not stated) | $29 (Startup) | $17 | $49 | $19 |
| 5,000 | $20 | $35 | $29 | $44 (17 + 3,000 × $0.009) | $49 | $19 |

Ours is the lowest bill in this set up to ~4,750 screenshots/month (ScrapingBee Hobby's $19 ÷ $0.004). Under 100/month, the free tiers of ScreenshotOne and ApiFlash cost $0.

**Not supported:** "about half the cost of pro screenshot APIs" in general (false vs ApiFlash, ScrapingBee and several mid/large plans), or any claim of equal quality to these services (not tested).

**Claim used:** "No monthly subscription: $0.004 per screenshot, and you pay only for screenshots delivered. That is less than half the per-screenshot price of the entry plans at ScreenshotOne ($0.0085), Urlbox ($0.0098) and ScreenshotAPI.net ($0.009) (list prices checked 18 Oct 2026)."
