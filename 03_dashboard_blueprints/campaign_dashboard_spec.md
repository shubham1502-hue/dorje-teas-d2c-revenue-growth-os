# Campaign Dashboard Spec  -  Dorje Teas

> Defines the weekly campaign performance dashboard used by Growth / Performance operator.
> Covers Google Ads (primary) with Meta structure where applicable.
> All figures are synthetic and illustrative. No internal Dorje ad account data used.

---

## Purpose

The campaign dashboard answers one question: **which campaigns are creating profitable customers, and which are spending without producing them?**

It is not a vanity metrics board. CTR and impressions matter only insofar as they connect to orders, CAC, and contribution margin.

---

## Dashboard Structure (6 Views)

---

### View 1  -  Campaign Efficiency Summary

The primary weekly view. Every active campaign, ranked by Contribution ROAS descending.

All example values and thresholds in this dashboard spec are illustrative [SYNTHETIC] placeholders.

| Campaign | Objective | Spend | Impressions | CTR | CPC | Sessions | CVR | Orders | Revenue | CAC | ROAS | CM | Contribution ROAS | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| First Flush  -  Branded Search | Conversion | ₹ | # | % | ₹ | # | % | # | ₹ | ₹ | x | ₹ | x | Scale |
| Darjeeling Tea  -  Non-Brand Search | Conversion | ₹ | # | % | ₹ | # | % | # | ₹ | ₹ | x | ₹ | x | Hold |
| Tea Gifts  -  Shopping | Conversion | ₹ | # | % | ₹ | # | % | # | ₹ | ₹ | x | ₹ | x | Hold |
| Premium Tea  -  Retargeting | Conversion | ₹ | # | % | ₹ | # | % | # | ₹ | ₹ | x | ₹ | x | Scale |
| Meta  -  Prospecting (New Audiences) | Awareness/Conv | ₹ | # | % | ₹ | # | % | # | ₹ | ₹ | x | ₹ | x | Fix |
| Meta  -  Retargeting (ATC + Visitors) | Conversion | ₹ | # | % | ₹ | # | % | # | ₹ | ₹ | x | ₹ | x | Scale |
| **Total** | | **₹** | | | | | | **#** | **₹** | **₹** | **x** | **₹** | **x** | |

**Contribution Margin per campaign = Revenue − (COGS + Packaging + Shipping + Gateway Fee) − Campaign Spend**

**Status Decision Logic [illustrative benchmark]:**

| Status | Criteria |
|---|---|
| Scale | Contribution ROAS >1.5x AND CAC below break-even AND CVR stable or rising |
| Hold | Contribution ROAS 1.0–1.5x OR one metric soft (monitor before committing more budget) |
| Fix | Contribution ROAS <1.0x OR CAC above break-even for 2+ weeks (diagnose before spending more) |
| Pause | CM negative for 2+ weeks with no improvement signal (stop spend, review structure) |

---

### View 2  -  Funnel by Campaign

Diagnoses where each campaign loses the buyer. Not all CVR problems are the same problem.

| Campaign | Sessions | → Product Page | → Add-to-Cart | → Checkout | → Purchase | Overall CVR | Drop-Off Stage |
|---|---|---|---|---|---|---|---|
| First Flush Search | # | % | % | % | % | % |  -  |
| Non-Brand Search | # | % | % | % | % | % | ATC → Checkout |
| Meta Prospecting | # | % | % | % | % | % | Product Page → ATC |
| Retargeting | # | % | % | % | % | % |  -  |

**How to read this view:**

- If the drop is at Product Page → ATC: trust, clarity, or price framing problem on the product page
- If the drop is at ATC → Checkout: cart friction, shipping cost surprise, or low urgency
- If the drop is at Checkout → Purchase: payment friction, delivery concern, or final-price remorse
- If the drop is consistent across all stages: traffic quality issue  -  wrong audience for all stages

**Operator annotation:**
> [Which campaign has the worst funnel leak this week? What stage? What is being done about it?]

---

### View 3  -  Creative Performance (Google Ads RSA / Meta Ad Level)

Tracks creative fatigue and identifies highest-performing messaging angles.

**For Google Search (RSA asset performance):**

| Ad Group | Headline / Description | Impressions | CTR | CVR | Status |
|---|---|---|---|---|---|
| First Flush Darjeeling | "Estate-grown First Flush Darjeeling" | # | % | % | Best performer |
| First Flush | "₹X per cup of exceptional Darjeeling" | # | % | % | Test  -  strong CTR |
| First Flush | "Picked at Selim Hill  -  shipped to your door" | # | % | % | Weak  -  low CTR |
| Original Darjeeling Chai | "Original Darjeeling Chai brewed in Darjeeling" | # | % | % | Strong |
| Chai | "Premium Chai. Direct from the Estate." | # | % | % | Moderate |

**For Meta (Ad level):**

| Ad Set | Creative Description | Spend | CPM | CTR | CPC | CVR | CAC | Status |
|---|---|---|---|---|---|---|---|---|
| Prospecting | Estate origin video  -  15s | ₹ | ₹ | % | ₹ | % | ₹ | Active |
| Prospecting | Price-per-cup static image | ₹ | ₹ | % | ₹ | % | ₹ | Fatiguing |
| Retargeting | Product carousel  -  visited pages | ₹ | ₹ | % | ₹ | % | ₹ | Active |

**Creative fatigue signal:** CTR declining >20% WoW on stable impressions → refresh creative.

**Messaging angles to rotate for Dorje (specific to brand positioning):**

| Angle | Message | Best Format | Best Segment |
|---|---|---|---|
| Estate provenance | "From a 150-year-old garden in Darjeeling" | Static / Video | Darjeeling Loyalist, Climate/Story-Led Buyer |
| Price-per-cup | "₹X per cup. Selim Hill quality." | Static | Daily Premium Tea Drinker, Health/Wellness Consumer |
| Harvest freshness | "Picked in April. Shipped to you." | Static / RSA | Darjeeling Loyalist |
| Gift story | "Give Darjeeling. Give something that matters." | Static / Carousel | Gift Buyer |
| Brewing ritual | "Your morning, elevated." | Video / Reel | Health/Wellness Consumer, Daily Premium Tea Drinker |
| Social proof | "1,00,000 cups brewed. What will yours taste like?" | Static | All segments |

---

### View 4  -  Search Intent Analysis (Google Ads)

Identifies whether search traffic is high-intent (Darjeeling-specific) or low-intent (generic tea queries).

**Search term report  -  top 20 queries by spend this week:**

| Search Term | Intent Level | Clicks | CTR | CPC | CVR | Orders | Status |
|---|---|---|---|---|---|---|---|
| "buy darjeeling first flush tea" | High | # | % | ₹ | % | # | Keep |
| "selim hill tea" | High | # | % | ₹ | % | # | Keep |
| "darjeeling tea online" | High | # | % | ₹ | % | # | Keep |
| "premium loose leaf tea india" | Medium | # | % | ₹ | % | # | Keep / watch |
| "tea gift box india" | Medium | # | % | ₹ | % | # | Keep |
| "green tea benefits" | Low | # | % | ₹ | % | # | Negative keyword |
| "chai recipe" | Low | # | % | ₹ | % | # | Negative keyword |
| "tea brands india" | Low-Medium | # | % | ₹ | % | # | Watch |

**Intent classification:**
- High: estate-specific, flush-specific, origin-specific, or brand-specific searches
- Medium: category-level searches with purchase intent signals
- Low: informational, recipe, or generic health queries  -  typically low CVR, wasted CPC spend

**Action:** Add consistently low-CVR, low-intent queries to the negative keyword list. Review weekly.

**Negative keyword build-up (running list to add):**

```
- tea recipe
- how to make chai
- green tea benefits
- tea for weight loss (unless you have a wellness campaign)
- cheap tea
- tea bags near me
- tea shop near me
```

---

### View 5  -  Landing Page Performance by Campaign

Confirms whether campaign traffic is reaching the right page and converting on it.

| Campaign | Landing Page URL | Sessions | Bounce Rate | ATC Rate | CVR | Revenue | Status |
|---|---|---|---|---|---|---|---|
| First Flush Search | /products/first-flush-2026 | # | % | % | % | ₹ | Healthy |
| Non-Brand Darjeeling | /collections/darjeeling | # | % | % | % | ₹ | Watch  -  generic page |
| Chai Search | /products/original-chai | # | % | % | % | ₹ | Healthy |
| Meta Prospecting | Homepage | # | % | % | % | ₹ | Act  -  wrong page |
| Wellness Search | /products/green-tea | # | % | % | % | ₹ | Watch |
| Gift Campaign | /collections/gift-boxes | # | % | % | % | ₹ | Healthy |

**Page-campaign match rules:**
- First Flush campaign → First Flush product page (not homepage, not collections page)
- Gift Buyer campaign → Gift box landing page (not generic shop)
- Wellness search → Green Tea product page with health framing above the fold (not estate origin above the fold)
- Non-brand Darjeeling → Consider a dedicated "Why Dorje Darjeeling?" landing page rather than a collections page

**Operator annotation:**
> [Which campaign-to-landing-page match is broken this week? What is the fix?]

---

### View 6  -  New vs. Returning Customer Revenue by Channel

Shows whether each channel is primarily acquiring new customers or re-engaging existing ones.

| Channel | New Customer Orders | New Customer Revenue | Returning Orders | Returning Revenue | New vs. Returning Split |
|---|---|---|---|---|---|
| Google Search | # | ₹ | # | ₹ | 70% / 30% |
| Meta Prospecting | # | ₹ | # | ₹ | 85% / 15% |
| Meta Retargeting | # | ₹ | # | ₹ | 20% / 80% |
| Email / WhatsApp | # | ₹ | # | ₹ | 5% / 95% |
| Organic / Direct | # | ₹ | # | ₹ | 40% / 60% |

**Why this matters:**
- Paid channels should primarily drive new customers. If a paid prospecting campaign is generating mostly returning customer orders, it may be retargeting existing customers unnecessarily (wasted spend  -  they would have returned anyway)
- Email and WhatsApp should be almost entirely returning customers. If they are driving significant new customer orders, check attribution  -  a new customer who clicked an email before the paid click may be mis-attributed
- Retargeting channels should show a high returning split by design

---

## Weekly Campaign Decision Checklist

Before closing the campaign dashboard:

- [ ] Is any campaign spending with Contribution ROAS below 1.0? → Fix or pause
- [ ] Is any campaign's CAC above break-even CAC for 2+ weeks? → Escalate
- [ ] Is any creative fatiguing (CTR declining >20% WoW)? → Queue refresh
- [ ] Are low-intent search terms being added to negative keywords? → Update list
- [ ] Is any campaign landing on the wrong page? → Fix URL
- [ ] Is the highest-performing campaign budget-constrained? → Request increase
- [ ] Are there any anomalies in the new vs. returning split? → Investigate attribution

---

## Campaign Dashboard Data Sources

| Data Element | Source | Pull Frequency |
|---|---|---|
| Spend, impressions, clicks, CTR, CPC | Google Ads / Meta Ads Manager | Daily pull, weekly summary |
| Sessions by campaign | GA4 (utm_campaign parameter) | Daily pull, weekly summary |
| Add-to-cart, checkout, purchase by campaign | GA4 + Shopify (campaign attribution) | Weekly |
| Revenue by campaign | Shopify (last-click attribution baseline) | Weekly |
| New vs. returning by channel | Shopify customer tag + GA4 | Weekly |
| COGS, packaging, shipping | Finance / ops input | Monthly (or on change) |
| Contribution margin | Calculated in Google Sheets dashboard | Weekly |
