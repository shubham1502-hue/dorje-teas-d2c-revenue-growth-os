# Synthetic Data Schema  -  Dorje Teas

> Documents every table in the synthetic dataset powering the Dorje revenue OS.
> All data is synthetic and clearly labeled [SYNTHETIC].
> No internal Dorje data, Shopify data, or ad account data was used.
> Schema mirrors what a real Dorje data stack would produce.

---

## Why Synthetic Data

This project cannot use internal Dorje data. But without data, the Python analysis
notebooks and Google Sheets dashboard would be theoretical documents.

Synthetic data solves this by:
1. Making the analysis executable  -  real Python code against realistic values
2. Demonstrating data modeling judgment  -  schema design shows operator thinking
3. Being fully auditable  -  every assumption is labeled, sourced, or explained
4. Replacing itself cleanly  -  on Day 1 with real internal access, each CSV is
   replaced with a Shopify/Ads export and every downstream formula updates

The generator script (`generate_synthetic_data.py`) is included so any reviewer
can audit, re-run, and trace every value back to its assumption.

---

## Data Design Principles

1. Reflect real Dorje products  -  names and categories match the public catalog
2. Use realistic Indian D2C economics  -  ₹ pricing, Indian cities, Indian logistics benchmarks
3. Include commercial complexity  -  discounts, returning customers, subscription orders,
   gift orders, seasonal patterns, channel mix
4. Be analysis-ready  -  enough rows and variance for cohort, funnel, and margin analysis
5. Label every synthetic assumption  -  any number from internal systems is marked [SYNTHETIC]

---

## Seasonal Design

The dataset covers April 2024 – April 2025 (13 months).

Key seasonal patterns baked in [SYNTHETIC]:

The timing and demand signals below are synthetic operating assumptions.

| Period | Pattern | Driver |
|---|---|---|
| Mar–Apr 2025 | First Flush volume spike | Harvest season; highest-intent acquisition |
| May–Jun 2024 | Second Flush uplift | Second harvest; Darjeeling Loyalist segment |
| Oct–Nov 2024 | Gift Box and overall volume spike | Diwali gifting season |
| Dec 2024 | Elevated gift and chai orders | Christmas gifting + winter chai demand |
| Jan–Feb 2025 | Volume dip | Post-festive seasonality |

---

## Table 1: sample_orders.csv

**What it is:** Order-level transaction data. One row per order.
**Real-world source:** Shopify Orders export (D2C channel, last 90–365 days)
**Row count:** ~437 orders [SYNTHETIC  -  illustrative volume for 13-month period]

**Why it exists:** Powers revenue analysis, AOV, product mix, contribution margin,
new vs. returning split, channel attribution, discount rate, and repeat purchase.

**Key design choices:**
- Includes new and returning customers for cohort analysis
- Subscription orders flagged separately to show subscription economics
- Gift orders flagged separately with premium packaging cost
- Discounted and full-price orders mixed to show discount rate impact on margin
- Cities drawn from realistic Indian D2C geography (metro and Tier 2/3)
- Channel attribution uses last-click logic (Google Search, Meta, Email, Organic, Direct)
- Seasonal product mix weighted by month (First Flush peaks Apr, Gift Box peaks Oct–Nov)

**Field reference:**

| Field | Type | Source | Notes |
|---|---|---|---|
| order_id | String | Shopify | ORD-YYYY-#### format |
| order_date | Date | Shopify | DD/MM/YYYY |
| week | String | Derived | ISO week for weekly aggregation |
| month | String | Derived | YYYY-MM for cohort grouping |
| customer_id | String | Shopify | CUST-#### format |
| customer_type | String | Derived | "new" or "returning" |
| product_id | String | Shopify | SKU-### format |
| product_name | String | Shopify | As per public catalog |
| product_category | String | Shopify | First Flush / Chai / Gift Box / etc. |
| quantity | Integer | Shopify | Units per order line |
| gross_revenue | Float ₹ | Shopify | Full price before discount |
| discount_amount | Float ₹ | Shopify | 0.0 if no discount applied |
| discount_code | String | Shopify | Code used or "none" |
| net_revenue | Float ₹ | Derived | gross_revenue − discount_amount |
| shipping_charged | Float ₹ | Shopify | What customer paid (0 if above free threshold) |
| cogs | Float ₹ | [SYNTHETIC] | Product cost  -  see OPS_Assumptions |
| packaging_cost | Float ₹ | [SYNTHETIC] | Standard ₹55 or Premium Gift ₹130 |
| shipping_cost | Float ₹ | [SYNTHETIC] | Blended ₹85–130 Dorje bears |
| gateway_fee | Float ₹ | Derived | net_revenue × 2% |
| gross_margin | Float ₹ | Derived | net_rev − cogs − pkg − ship − gateway |
| gross_margin_pct | Float % | Derived | gross_margin ÷ net_revenue × 100 |
| attributed_ad_spend | Float ₹ | [SYNTHETIC] | Estimated spend attributed to this order's channel |
| contribution_margin | Float ₹ | Derived | gross_margin − attributed_ad_spend |
| cm_pct | Float % | Derived | contribution_margin ÷ net_revenue × 100 |
| channel | String | GA4 + Shopify | google_search / meta / email / organic / direct |
| campaign_id | String | GA4 | CMP-XX-### or "none" |
| city | String | Shopify | Customer delivery city |
| is_subscription | Boolean | Shopify/App | TRUE if subscription order |
| is_gift | Boolean | Derived | TRUE if gift box SKU |

---

## Table 2: sample_ad_spend.csv

**What it is:** Weekly campaign performance data. One row per campaign per week.
**Real-world source:** Google Ads report + Meta Ads Manager export
**Row count:** ~456 rows (8 campaigns × ~57 weeks) [SYNTHETIC]

**Why it exists:** Powers CAC, ROAS, Contribution ROAS, CTR, CVR, and channel
efficiency analysis. The campaign dashboard and Python campaign analysis notebook
both pull from this table.

**Key design choices:**
- 8 paid campaigns across Google and Meta (5 Google, 3 Meta)
- Seasonal spend multipliers applied  -  First Flush campaigns scaled in Mar–Apr,
  gift campaigns scaled in Oct–Dec
- Contribution ROAS calculated after estimated variable costs (~38–52% of revenue)
- Email campaigns tracked separately with near-zero attributed spend (platform cost only)

**Field reference:**

| Field | Type | Source | Notes |
|---|---|---|---|
| week | String | Derived | ISO week |
| week_start | Date | Derived | DD/MM/YYYY |
| week_end | Date | Derived | DD/MM/YYYY |
| month | String | Derived | YYYY-MM |
| platform | String | Platform | "google" or "meta" |
| campaign_id | String | Platform | CMP-GS-### or CMP-MT-### |
| campaign_name | String | Platform | Descriptive name |
| campaign_objective | String | Platform | acquisition / retargeting / retention |
| spend | Float ₹ | [SYNTHETIC] | Weekly spend on this campaign |
| impressions | Integer | [SYNTHETIC] | Total ad impressions |
| clicks | Integer | [SYNTHETIC] | Total clicks |
| ctr_pct | Float % | Derived | clicks ÷ impressions × 100 |
| cpc | Float ₹ | Derived | spend ÷ clicks |
| cpm | Float ₹ | [SYNTHETIC] | Cost per 1,000 impressions |
| sessions | Integer | [SYNTHETIC] | Landing page sessions from this campaign |
| add_to_cart | Integer | [SYNTHETIC] | Add-to-cart events attributed to campaign |
| atc_rate_pct | Float % | [SYNTHETIC] | add_to_cart ÷ sessions × 100 |
| checkouts | Integer | [SYNTHETIC] | Checkout initiations |
| checkout_rate_pct | Float % | [SYNTHETIC] | checkouts ÷ add_to_cart × 100 |
| orders | Integer | [SYNTHETIC] | Purchases attributed to campaign |
| cvr_pct | Float % | [SYNTHETIC] | orders ÷ sessions × 100 |
| revenue | Float ₹ | [SYNTHETIC] | Revenue attributed to campaign |
| new_customers | Integer | [SYNTHETIC] | New buyers from this campaign |
| cac | Float ₹ | Derived | spend ÷ new_customers |
| roas | Float | Derived | revenue ÷ spend |
| contribution_roas | Float | [SYNTHETIC] | (revenue − est. variable costs) ÷ spend |
| status | String | Manual | active / paused / ended |

---

## Table 3: sample_product_catalog.csv

**What it is:** Product-level reference with pricing and margin assumptions.
**Real-world source:** Shopify product catalog + internal finance/ops inputs
**Row count:** 12 products [SYNTHETIC economics; product names from public catalog]

**Why it exists:** Reference table for COGS, packaging, and margin calculations.
Every contribution margin formula in the orders table and dashboard references this.

**Key design choices:**
- Product names match Dorje's public catalog
- COGS, packaging, shipping are [SYNTHETIC] benchmarks from premium Indian D2C category
- price_per_cup_est included as a conversion framing reference
- ladder_rung and primary_segment align with the product ladder framework

---

## Table 4: sample_customer_cohorts.csv

**What it is:** Monthly cohort retention table, M0 through M6.
**Real-world source:** Shopify order export + cohort analysis (Python or Sheets)
**Row count:** 13 cohorts (Apr 2024 – Apr 2025) [SYNTHETIC]

**Why it exists:** Powers retention cohort analysis, LTV:CAC calculation, and the
retention dashboard. The Python retention notebook reads directly from this table.

**Key design choices:**
- 13 months of cohorts  -  enough for meaningful retention curves
- M0 through M6 retention tracked  -  shows long-term compounding behavior
- Seasonal patterns baked in: Oct–Nov cohorts have higher M0 AOV (Gift Buyer segment)
  but lower repeat rates; First Flush cohorts (Apr) have higher repeat rates
- subscription_attach_m2 column shows subscription conversion after demonstrated repeat
- ltv_cac_ratio_m6 allows LTV:CAC analysis per cohort

---

## How to Replace Synthetic Data with Real Data (Day 1 Checklist)

On Day 1 with internal access, replace each [SYNTHETIC] file:

| File | Replace with |
|---|---|
| sample_orders.csv | Shopify Orders export → filter to D2C channel, last 365 days |
| sample_ad_spend.csv | Google Ads weekly report + Meta Ads Manager export |
| sample_product_catalog.csv | Shopify product export + COGS and packaging from finance/ops |
| sample_customer_cohorts.csv | Python cohort script run against real Shopify order export |

After replacement, every downstream formula in the Google Sheets dashboard and
every Python notebook recalculates automatically against real data.
