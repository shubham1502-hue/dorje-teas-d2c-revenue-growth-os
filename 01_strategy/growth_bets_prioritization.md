# Growth Bets Prioritization — Dorje Teas

> Founder-facing prioritization of D2C growth initiatives for the next 6 months.
> Based on category analysis and the product-ladder framework. No internal Dorje data used.
> All scores are illustrative. Actual prioritization should be recalibrated with internal data.

---

## Scoring Framework

Each growth bet is scored on four dimensions:

| Dimension | Definition |
|---|---|
| **Impact** | Expected revenue or margin lift if the bet succeeds. Scored 1–5. |
| **Confidence** | How certain are we this will work, based on category logic and public observations? Scored 1–5. |
| **Speed** | How quickly can this be executed and measured? Scored 1–5 (5 = fastest). |
| **Complexity** | How hard is this to build and operate? Scored 1–5 (5 = simplest). |

**Priority Score = Impact × Confidence × Speed × Complexity**

Higher score = do first.

This is a **triage tool**, not a roadmap. The founder should review this quarterly and reweight based on what the data shows.

---

## The Growth Bets

### Bet 1 — Post-Purchase Retention Flows (Email + WhatsApp)

**Description:** Build Day 7 / Day 21 / Day 30 / Day 45 automated flows for each key product type (Chai, First Flush, Green Tea, Gift Box). Segment by product purchased and new vs. returning status.

**Why it matters:** Every customer acquired with CAC has a second purchase potential that costs near nothing to trigger. The retention flow is the single highest-ROI lever available before spending more on acquisition.

**What it requires:** Email or WhatsApp platform access, Shopify order data, segment-level copywriting, basic automation setup.

| Dimension | Score | Reasoning |
|---|---|---|
| Impact | 5 | Directly improves repeat purchase rate, which improves LTV:CAC across every channel |
| Confidence | 5 | Category-proven for premium consumables. Product education + replenishment nudge is standard retention logic. |
| Speed | 4 | Can be live in 2–3 weeks with basic email platform access |
| Complexity | 4 | Low tech complexity; requires strong copy and segment logic |

**Priority Score: 400** ← Build first.

---

### Bet 2 — First Flush Darjeeling Dedicated Landing Page and Campaign

**Description:** Build a standalone First Flush Darjeeling landing page with harvest story, estate origin, tasting notes, price-per-cup framing, and a bundle offer. Run a targeted search campaign against high-intent Darjeeling and First Flush queries.

**Why it matters:** First Flush is a seasonal window. It cannot be recovered if missed. A segment-specific landing page with harvest narrative will outconvert a generic product page for this intent.

**What it requires:** Landing page build (Shopify or separate), copywriting, estate photography or assets, Google Ads campaign setup.

| Dimension | Score | Reasoning |
|---|---|---|
| Impact | 5 | Highest-margin, highest-conviction acquisition window of the year |
| Confidence | 4 | High-intent seasonal search traffic responds well to specific landing pages; tested category logic |
| Speed | 3 | Requires landing page build + campaign setup (3–4 weeks if starting now) |
| Complexity | 3 | Moderate — landing page, copy, campaign, and measurement all required |

**Priority Score: 180** ← Do in Month 1–2 alongside retention flows.

---

### Bet 3 — Contribution Margin Dashboard (Weekly Visibility)

**Description:** Build a Google Sheets contribution margin view that connects orders, channel spend, COGS, packaging, shipping, and gateway fees into a weekly per-order and per-channel CM number.

**Why it matters:** Without CM visibility, scaling decisions are made on ROAS alone. ROAS-positive, CM-negative campaigns are a common D2C failure mode for premium brands with complex logistics.

**What it requires:** Shopify order export, ad spend export, COGS/packaging/shipping input from ops/finance, Google Sheets build.

| Dimension | Score | Reasoning |
|---|---|---|
| Impact | 4 | Prevents margin leakage at scale; every subsequent spending decision improves |
| Confidence | 5 | Operational certainty — this is instrumentation, not an experiment |
| Speed | 5 | Can be built in 1 week with data access |
| Complexity | 5 | Google Sheets; no engineering required |

**Priority Score: 500** ← Build in Week 1. This is table stakes before any spend scaling.

---

### Bet 4 — Product Page Conversion Testing

**Description:** Test asset sequencing on 2–3 key product pages (First Flush, Chai, Gift Box). Hypothesis: benefit → price-per-cup → estate proof → reviews → brewing guide → subscription prompt outperforms the current layout.

**Why it matters:** Product page CVR improvement compounds across all acquisition channels simultaneously. A 10% lift in CVR from a product page change improves every campaign that sends traffic to that page.

**What it requires:** Current product page CVR baseline, Shopify or Hotjar session data, A/B test or before/after comparison, copy and layout changes.

| Dimension | Score | Reasoning |
|---|---|---|
| Impact | 4 | CVR improvement is a multiplier across all channels |
| Confidence | 3 | Landing page tests are high-variance; need traffic volume to read results |
| Speed | 3 | 3–4 weeks per test to reach statistical significance |
| Complexity | 3 | Requires testing framework and sufficient traffic per page |

**Priority Score: 108**

---

### Bet 5 — Tea Club Subscription Push (Post-Second-Purchase)

**Description:** Trigger a subscription offer specifically after a customer's second purchase on any product. Frame as "never run out" + mild benefit (free shipping on subscription, or small quantity bonus).

**Why it matters:** Subscription attach rate after second purchase is significantly higher than after first purchase. Most brands push subscription too early and get low conversion or early churn.

**What it requires:** Post-purchase email/WhatsApp trigger, Shopify order history logic, subscription landing page with specific offer.

| Dimension | Score | Reasoning |
|---|---|---|
| Impact | 5 | Subscription is the highest-LTV commercial outcome in the product ladder |
| Confidence | 4 | Timing subscription after demonstrated repeat behavior is category-proven |
| Speed | 4 | Can be configured in email/WhatsApp platform with Shopify trigger in 2–3 weeks |
| Complexity | 4 | Low complexity; requires only order-count logic in automation |

**Priority Score: 320**

---

### Bet 6 — Gift Buyer to Self-Purchaser Conversion Flow

**Description:** After a gift box purchase, trigger a Day 14 email to the buyer with a "keep some for yourself" message and a soft self-purchase prompt. If gift receiver email is capturable, send a separate introduction email to the receiver.

**Why it matters:** Gift Buyer customers are a paid acquisition. If they never self-purchase, the cost is sunk on a single high-AOV order. Converting even 15–20% to self-purchasers makes gifting an acquisition channel.

**What it requires:** Gift order identification in Shopify (gift box SKU filter), email sequence, gift receiver email capture mechanism (optional but high-value).

| Dimension | Score | Reasoning |
|---|---|---|
| Impact | 3 | High per-convert value but smaller segment volume |
| Confidence | 4 | Category logic is sound; gift-to-self conversion is a standard D2C play |
| Speed | 4 | Email sequence can be live in 2 weeks |
| Complexity | 4 | Simple SKU-level trigger; gift receiver email capture is harder |

**Priority Score: 192**

---

### Bet 7 — First-Time Buyer Sampler Bundle

**Description:** Create a curated entry bundle (e.g., First Flush 50g + Chai 50g + Green Tea 50g) priced as a discovery pack for first-time buyers. Purpose: reduce first-purchase risk, increase AOV, and expose buyers to multiple rungs of the product ladder in one order.

**Why it matters:** A buyer who tries three products is more likely to repeat on the one they love most. The sampler bundle also raises AOV past the free-shipping threshold for most first-time buyers.

**What it requires:** Bundle configuration in Shopify, dedicated landing page, entry-pack pricing decision, packaging configuration.

| Dimension | Score | Reasoning |
|---|---|---|
| Impact | 3 | Improves first-purchase CVR and AOV; may improve repeat rate via product discovery |
| Confidence | 3 | Sampler bundles work in premium consumables; Dorje's product mix supports it |
| Speed | 3 | Requires bundle setup in Shopify + landing page (3–4 weeks) |
| Complexity | 3 | Moderate — packaging and pricing configuration needed |

**Priority Score: 81**

---

### Bet 8 — Winback Campaign for 60+ Day Dormant Customers

**Description:** Identify customers who bought once and have not returned in 60+ days. Send a 2-email winback sequence: (1) "We noticed you haven't been back — here's what's new at Selim Hill" and (2) "Last chance — a small offer to bring you back."

**Why it matters:** Winback campaigns on customers who already know the brand convert at a higher rate than cold acquisition at a fraction of the CAC.

**What it requires:** Shopify customer export filtered by last order date, email sequence, small winback offer (free shipping or modest discount), segment exclusion for active subscribers.

| Dimension | Score | Reasoning |
|---|---|---|
| Impact | 3 | Recaptures revenue from already-acquired customers |
| Confidence | 4 | Winback email is standard and proven for premium consumables |
| Speed | 5 | Can be live in 1 week |
| Complexity | 5 | Simple Shopify filter + email sequence |

**Priority Score: 300**

---

### Bet 9 — Harvest Update Pre-Launch Email for Darjeeling Loyalist Segment

**Description:** Before First Flush availability, send a harvest anticipation email to past First Flush buyers and Tea Club subscribers. "2026 First Flush is being picked at Selim Hill — here is what to expect." Include a pre-order or early access option.

**Why it matters:** The Darjeeling Loyalist segment buys on anticipation, not just availability. Pre-launch communication creates demand before the product page goes live and converts the highest-intent segment first.

**What it requires:** Past First Flush buyer segment in Shopify/email platform, harvest update content (estate photo, picking timing, tasting note preview), early access landing page.

| Dimension | Score | Reasoning |
|---|---|---|
| Impact | 4 | Captures highest-LTV segment at their peak intent moment |
| Confidence | 5 | Harvest communication is proven for estate brands; the Darjeeling Loyalist segment responds strongly |
| Speed | 5 | Email to existing list; near-zero build time if content is ready |
| Complexity | 5 | Segment filter + email + early access page |

**Priority Score: 500** ← Do alongside CM dashboard in Week 1 if First Flush season is approaching.

---

### Bet 10 — Google Search Campaign Audit and Cleanup

**Description:** Audit existing Google Search campaigns for keyword intent match, landing page relevance, and wasted spend. Pause low-intent or broad keywords. Build tighter ad groups around high-intent queries (First Flush Darjeeling, buy Darjeeling tea online, estate Darjeeling tea).

**Why it matters:** Most early D2C Google Ads accounts have structural inefficiency — broad match keywords, generic landing pages, and untracked conversion paths. An audit often reveals 20–30% of spend that can be reallocated or eliminated.

**What it requires:** Google Ads account access, 30–60 day keyword and search term report, landing page CVR data by campaign, restructuring plan.

| Dimension | Score | Reasoning |
|---|---|---|
| Impact | 4 | Immediate CAC improvement with no additional spend |
| Confidence | 4 | Campaign audits reliably find inefficiency in early-stage Google Ads accounts |
| Speed | 4 | Audit in 1 week; changes live within 2 weeks |
| Complexity | 3 | Requires Google Ads access and analytical review |

**Priority Score: 192**

---

## Priority Ranking Summary

Priority scores are illustrative [SYNTHETIC] scoring outputs, not Dorje internal performance metrics.

| Rank | Growth Bet | Priority Score | When to Execute |
|---|---|---|---|
| 1 | Contribution Margin Dashboard | 500 | Week 1 — table stakes |
| 2 | Harvest Update Pre-Launch Email | 500 | Week 1 if First Flush season is approaching |
| 3 | Post-Purchase Retention Flows | 400 | Month 1 — highest ROI lever |
| 4 | Tea Club Subscription Push (post-2nd purchase) | 320 | Month 1–2 |
| 5 | Winback Campaign (60+ day dormant) | 300 | Month 1 — quick win |
| 6 | First Flush Darjeeling Landing Page + Campaign | 180 | Month 1–2 alongside retention |
| 7 | Gift Buyer to Self-Purchaser Flow | 192 | Month 2 |
| 8 | Google Search Campaign Audit | 192 | Month 1–2 |
| 9 | Product Page Conversion Testing | 108 | Month 2–3 (needs traffic baseline first) |
| 10 | First-Time Buyer Sampler Bundle | 81 | Month 3 (after conversion baseline is set) |

---

## Kill Conditions

A growth bet should be paused or killed if:

- CM dashboard shows it is contribution-margin-negative after 4 weeks
- CVR or repeat rate does not move in the expected direction after 2 test cycles
- The bet requires engineering or ops resources that delay higher-priority initiatives
- Data volume is too low to read results (pause and revisit at higher traffic)

---

## Recalibration Trigger

This prioritization should be reviewed and recalibrated at:
- End of Month 2 (after Phase 1 baseline is established)
- End of Month 4 (after retention and gifting tracks are running)
- End of Month 6 (full 6-month retrospective)

New internal data will change the scores. That is expected and good.
