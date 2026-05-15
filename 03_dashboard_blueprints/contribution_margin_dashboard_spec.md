# Contribution Margin Dashboard Spec  -  Dorje Teas

> Defines the weekly contribution margin view for the Founder's Office operator.
> Purpose: ensure revenue growth is margin-positive before scaling any channel.
> All cost assumptions are synthetic. No internal Dorje COGS or financial data used.

---

## Why Contribution Margin, Not Just ROAS

ROAS tells you the ratio of revenue to ad spend. It does not tell you whether the business made money on that order.

For a premium D2C tea brand shipping direct from Darjeeling, the gap between ROAS and realized unit economics can be wide:

```
Gross Revenue:          ₹800 (a typical 100g First Flush order)
Less: Discount applied  ₹0   (no discount this order)
Net Revenue:            ₹800

Less: Product COGS      ₹180 (estimated  -  synthetic)
Less: Packaging         ₹80  (premium box + inner foil + label  -  synthetic)
Less: Shipping          ₹120 (direct from Darjeeling  -  synthetic)
Less: Gateway fee       ₹16  (2% of net revenue  -  synthetic)
                       ──────
Gross Margin:           ₹404 (50.5% gross margin)

Less: Paid media (attributed) ₹220 (CAC on this channel  -  synthetic)
                       ──────
Contribution Margin:    ₹184 (23% CM  -  this order is profitable)
```

A 3.6x ROAS (₹800 revenue ÷ ₹220 spend) looks strong. But without CM visibility, you cannot see that shipping and packaging are consuming 25% of revenue before margin is calculated. At scale, this matters enormously.

---

## Cost Assumption Inputs (Required Before Building)

These inputs power every CM calculation. They must be provided by finance / ops and updated when they change.

| Cost Component | Input Required | Example [SYNTHETIC] | Update Frequency |
|---|---|---|---|
| Product COGS per SKU | ₹ per 100g (by SKU) | ₹150–₹220 depending on flush | Monthly or on change |
| Packaging cost per order | ₹ per order (standard vs. gift) | ₹60–₹120 | Monthly or on change |
| Outbound shipping cost | ₹ per order (by region or flat) | ₹100–₹160 | Monthly or on change |
| Payment gateway fee | % of net revenue | 2% | Monthly or on change |
| Average discount applied | ₹ or % (from Shopify) | Dynamic  -  pulled from orders | Weekly |
| Refund / replacement cost | % of orders | 1–2% estimated [SYNTHETIC] | Monthly |

---

## Dashboard Structure (5 Views)

---

### View 1  -  Weekly CM Summary

The primary weekly view. Built in the Google Sheets dashboard.

| Revenue Source | Orders | Gross Revenue | Discounts | Net Revenue | COGS | Packaging | Shipping | Gateway Fee | Gross Margin | Paid Media | Contribution Margin | CM% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Google Search | # | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | % |
| Meta Prospecting | # | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | % |
| Meta Retargeting | # | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | % |
| Email / WhatsApp | # | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | % |
| Organic / Direct | # | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | % |
| **Total** | **#** | **₹** | **₹** | **₹** | **₹** | **₹** | **₹** | **₹** | **₹** | **₹** | **₹** | **%** |

**Key formula (in Google Sheets):**
```
Contribution Margin = Net Revenue - COGS - Packaging - Shipping - Gateway Fee - Paid Media
CM% = Contribution Margin / Net Revenue
```

**Conditional formatting:**
- CM%: green if >20%, yellow if 10–20%, red if <10%, bold red if negative

**Operator annotation:**
> [Is any channel margin-negative this week? What is driving it  -  shipping, COGS, discounts, or media spend? What is the action?]

---

### View 2  -  CM by Product Type

Cuts margin by product to identify which SKUs are driving profitable revenue.

| Product Category | Orders | Net Revenue | Avg COGS | Avg Packaging | Avg Shipping | Avg Gateway | Gross Margin | Gross Margin% | CM (before media) | CM% |
|---|---|---|---|---|---|---|---|---|---|---|
| First Flush | # | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | % | ₹ | % |
| Second Flush | # | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | % | ₹ | % |
| Darjeeling Green Tea | # | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | % | ₹ | % |
| Original Darjeeling Chai | # | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | % | ₹ | % |
| Pyramid Teabags | # | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | % | ₹ | % |
| Cold Brew | # | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | % | ₹ | % |
| Selim Hill Gift Box Classic and Selim Hill Gift Box Premium | # | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | % | ₹ | % |
| Subscription Orders | # | ₹ | ₹ | ₹ | ₹ | ₹ | ₹ | % | ₹ | % |

**What to look for:**
- Gift boxes should have the highest AOV but may have the lowest CM% due to premium packaging  -  track both the ₹ amount and the %.
- Subscription orders should show better CM% than one-time orders at the same SKU (no CAC on renewal).
- Chai should have the highest volume and fastest replenishment cycle  -  even moderate CM% compounds well with high frequency.
- Any SKU with gross margin below 35% before media is a pricing or COGS problem, not a marketing problem.

---

### View 3  -  CM by New vs. Returning Customer

Shows whether the economics of acquiring new customers are justified by the lifetime value signal.

| Customer Type | Orders | Net Revenue | Variable Costs (ex-media) | Gross Margin | Paid Media Allocated | Contribution Margin | CM% |
|---|---|---|---|---|---|---|---|
| New Customer (first order) | # | ₹ | ₹ | ₹ | ₹ (full CAC allocated) | ₹ | % |
| Returning Customer (2nd+ order) | # | ₹ | ₹ | ₹ | ₹ (minimal / zero) | ₹ | % |
| Subscriber Renewal | # | ₹ | ₹ | ₹ | ₹ (near zero) | ₹ | % |

**Expected pattern [SYNTHETIC logic]:**
- New customer CM% is lowest  -  carries full CAC weight. May be negative on first order.
- Returning customer CM% is significantly higher  -  no CAC, just variable product costs.
- Subscriber renewal CM% is highest  -  no CAC, and packaging may be lighter for subscription format.

**The business case for retention in one number:**
> If new customer CM% is −5% and returning customer CM% is +32%, then every repeat purchase more than compensates for the first-order loss  -  provided the repeat rate is high enough and fast enough.

**Break-even analysis [SYNTHETIC example]:**

| Scenario | First Order CM | Repeat Order CM | Break-Even at |
|---|---|---|---|
| CAC = ₹600, GM per order = ₹400 | −₹200 | +₹380 | 1.5 repeat orders |
| CAC = ₹800, GM per order = ₹400 | −₹400 | +₹380 | 2.1 repeat orders |
| CAC = ₹400, GM per order = ₹400 | ₹0 | +₹380 | First repeat order is pure profit |

This table should be recalculated with real COGS and CAC data once internal access is available.

---

### View 4  -  Discount Sensitivity Analysis

Shows how different discount levels affect contribution margin.

| Discount Level | Example AOV | Net Revenue | COGS | Packaging | Shipping | Gateway | Gross Margin | GM% | With Media (avg CAC) | CM% |
|---|---|---|---|---|---|---|---|---|---|---|
| No discount | ₹800 | ₹800 | ₹180 | ₹80 | ₹120 | ₹16 | ₹404 | 50.5% | ₹184 | 23% |
| 10% discount | ₹720 | ₹720 | ₹180 | ₹80 | ₹120 | ₹14 | ₹326 | 45.3% | ₹106 | 14.7% |
| 15% discount | ₹680 | ₹680 | ₹180 | ₹80 | ₹120 | ₹14 | ₹286 | 42.1% | ₹66 | 9.7% |
| 20% discount | ₹640 | ₹640 | ₹180 | ₹80 | ₹120 | ₹13 | ₹247 | 38.6% | ₹27 | 4.2% |

*All figures are [SYNTHETIC]  -  for illustrative logic only.*

**What this table shows:**
- A 10% discount reduces CM% by ~8 percentage points on a typical order
- A 20% discount leaves almost no contribution margin after media
- For a premium tea brand, discounts above 10% require careful justification  -  they are not free

**Use case for this view:** Any time a discount campaign is being proposed, run the scenario through this table first. If the campaign discount brings CM% below 10%, the revenue volume must compensate  -  and it often does not.

---

### View 5  -  Monthly CM Trend

Tracks contribution margin over time to see whether the business is improving or degrading on margin.

| Month | Net Revenue | Total Variable Costs | Gross Margin | Gross Margin % | Paid Media | Contribution Margin | CM% | WoW / MoM Trend |
|---|---|---|---|---|---|---|---|---|
| Jan 2025 [SYNTHETIC] | ₹4,80,000 | ₹2,16,000 | ₹2,64,000 | 55% | ₹96,000 | ₹1,68,000 | 35% |  -  |
| Feb 2025 [SYNTHETIC] | ₹5,20,000 | ₹2,28,800 | ₹2,91,200 | 56% | ₹1,04,000 | ₹1,87,200 | 36% | +1pp |
| Mar 2025 [SYNTHETIC] | ₹6,80,000 | ₹2,99,200 | ₹3,80,800 | 56% | ₹1,76,800 | ₹2,04,000 | 30% | −6pp |
| Apr 2025 [SYNTHETIC] | ₹8,40,000 | ₹3,78,000 | ₹4,62,000 | 55% | ₹2,52,000 | ₹2,10,000 | 25% | −5pp |

**How to read March and April:**
Revenue grew, but CM% dropped because paid media spend scaled faster than gross margin improved. This is a common D2C pattern  -  early revenue growth looks like success until CM% compression becomes visible at scale.

**Operator alert trigger:**
- CM% declining more than 3pp month-over-month for 2 consecutive months → media spend scaling review required

---

## Contribution Margin Dashboard Operating Rules

1. **CM dashboard is built before any spend increase is approved.** Spend decisions without CM data are made blind.
2. **Gift box CM is tracked separately from daily product CM.** Premium packaging makes gift boxes structurally different  -  blending them masks the difference.
3. **Subscription CM is tracked separately from one-time CM.** Subscriptions should show superior economics over time  -  if they do not, the subscription offer structure needs review.
4. **Discount rate is reviewed alongside CM every week.** Discounts are the fastest way to compress margin without appearing to do so in a ROAS report.
5. **Any channel with CM% below 10% for 2 consecutive weeks is flagged to the founder** regardless of ROAS performance.

---

## What This Dashboard Does Not Claim

This dashboard spec defines the structure and logic of a contribution margin view. It does not:
- Claim to have access to Dorje's actual COGS, packaging, or shipping contracts
- Claim to have modeled Dorje's actual P&L
- Make any assertion about the brand's realized margin performance

All cost inputs labeled [SYNTHETIC] are illustrative estimates used to demonstrate operating logic. Real implementation requires actual cost data from Dorje's finance and operations team.
