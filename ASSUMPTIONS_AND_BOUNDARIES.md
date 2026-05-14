# Assumptions and Boundaries

> This file defines the exact scope, data sources, and credibility boundaries of this project.
> Read this before interpreting any figure, metric, or recommendation in this repo.

---

## What This Project Is

This is a **public-information and synthetic-data revenue operating system simulation** for Dorje Teas.

It is designed to show how a Founder's Office / Revenue Ops operator would structure, track, diagnose, and improve D2C revenue for a premium Darjeeling tea brand — using the frameworks, metrics, and operating cadences appropriate for this category.

It is **not** a performance audit of Dorje Teas. It is not based on any internal Dorje data.

---

## What Data Was Used

### Public Information (Used Directly)
The following were observed from publicly available sources and used to inform the brand framing, product ladder, and category analysis:

| Observation | Source |
|---|---|
| Brand positioning around estate-grown Darjeeling tea | Dorje Teas public website |
| Selim Hill Tea Garden as origin estate | Dorje Teas public website |
| Product categories: First Flush, Second Flush, Green Tea, Chai, Cold Brew | Dorje Teas public product catalog |
| Tea Club / subscription offering | Dorje Teas public website |
| Alt Carbon's Darjeeling revival thesis | Alt Carbon public website and positioning |
| Premium pricing tier and pack size observations | Dorje Teas public shop pages |
| General D2C tea category dynamics | Publicly available market research and brand comparisons |

### Synthetic Data (Clearly Labeled)
The following figures were **created for this project** to demonstrate operating logic. They are not real Dorje figures:

- Monthly D2C revenue
- Order volume and AOV
- New customer vs. returning customer revenue split
- CAC by channel
- ROAS by campaign
- CTR, CPC, CVR by campaign
- Add-to-cart rate, checkout rate
- Repeat purchase rate and time to second purchase
- Subscription attach rate and renewal rate
- Cohort revenue and cumulative LTV
- Product COGS, packaging cost, shipping cost
- Payment gateway fee assumptions
- Contribution margin by channel, product, and campaign
- Break-even CAC estimates

All synthetic data is labeled `[SYNTHETIC]` in the relevant files and CSVs.

---

## What I Have Not Done

| Claim | Status |
|---|---|
| Accessed Dorje's Shopify store or backend | Not done |
| Accessed Dorje's Google Ads or Meta account | Not done |
| Accessed private revenue or P&L exports from Dorje | Not done |
| Managed a live D2C media buying budget | Not claimed |
| Owned a live D2C P&L | Not claimed |
| Owned or operated a live Shopify store | Not claimed |
| Audited Dorje's actual performance | Not done |

---

## What I Have Done

| Skill | Evidence in This Repo |
|---|---|
| D2C funnel analysis | `02_metrics_os/`, `03_dashboard_blueprints/` |
| CAC / ROAS / LTV / contribution margin modeling | `02_metrics_os/`, `03_dashboard_blueprints/`, `04_data_model/` |
| Retention cohort analysis | `03_dashboard_blueprints/retention_dashboard_spec.md`, `04_data_model/sample_customer_cohorts.csv` |
| Revenue experiment design | `01_strategy/growth_bets_prioritization.md`, `02_metrics_os/decision_rules.md` |
| Founder-facing weekly reporting | `02_metrics_os/weekly_revenue_review_template.md` |
| Consumer and category research | `01_strategy/`, `PUBLIC_RESEARCH_NOTES.md` |
| Synthetic dataset design | `04_data_model/` |
| Operating documentation and scope control | `README.md`, `ASSUMPTIONS_AND_BOUNDARIES.md` |
| Google Ads campaign dashboard logic | `03_dashboard_blueprints/campaign_dashboard_spec.md` |
| Markdown, GitHub, Python, Google Sheets operating logic | Throughout repo |

---

## Margin and Cost Assumptions

The contribution margin model uses these assumptions. All are synthetic and labeled as such:

| Cost Component | Assumption Basis |
|---|---|
| Product COGS | Estimated from premium whole-leaf Darjeeling category benchmarks |
| Packaging | Estimated for premium D2C tea (branded box, inner foil, label) |
| Shipping cost | Estimated for average Indian D2C delivery cost per order |
| Payment gateway fee | 2% of order value (common Indian gateway benchmark) |
| Discounts | Modeled at 0%, 10%, 15% scenarios |
| Refund/return rate | Estimated at 1–2% for premium consumables |

These are starting assumptions only. A real implementation would use Dorje's actual COGS, packaging quotes, logistics contracts, and gateway agreements.

---

## How to Use This Project

**For a founder reviewing this:**
- Treat every figure as illustrative, not descriptive of your actual business
- Use the frameworks, templates, and decision rules — they are designed to work with your real data once plugged in
- The weekly review template, experiment tracker, and decision rules are immediately usable

**For a hiring manager reviewing this:**
- This project demonstrates operating thinking, not internal Dorje data access
- The strength of this repo is the systems design, not the specific numbers

---

## Day 1 Data Requests

If this operating system were being deployed at Dorje, the following data would be requested on Day 1:

1. Shopify order export (last 12 months): order date, SKU, revenue, discount, customer ID, new/returning flag, city
2. Google Ads campaign export: spend, impressions, clicks, conversions by campaign
3. Meta campaign export (if applicable): same fields
4. Email/WhatsApp platform data: subscriber count, open rate, click rate, list by segment
5. Product COGS by SKU: from finance or sourcing team
6. Actual packaging cost per product
7. Actual shipping cost per order (from logistics provider)
8. Payment gateway fee rate
9. Subscription/Tea Club active count, renewal rate, churn (from Shopify or subscription app)
10. Refund rate by product or channel

This is the data that would replace every `[SYNTHETIC]` label in this repo.
