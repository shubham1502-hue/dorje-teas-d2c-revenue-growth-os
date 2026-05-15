# How to Fork and Use This Repo

This guide is for founders, Founder's Office operators, Growth Ops, RevOps, BizOps, and Strategy operators who want to adapt the Dorje Teas D2C Revenue Growth OS to their own D2C business.

This is not a plug-and-play performance audit. It is a public-safe operating system template built with public information, assumptions, and synthetic data. Replace the sample context before using it for real company decisions.

## Who Should Use This Repo

Use this repo if you need to create a weekly revenue review for a D2C business where the founder needs to see:

- what changed in revenue this week
- whether acquisition is profitable after variable costs
- where the funnel is leaking
- whether first-time buyers are returning
- whether subscription, gifting, or replenishment is improving revenue quality
- what should be scaled, fixed, killed, investigated, or unblocked

This is most useful for premium, repeat-purchase, subscription, gifting, or margin-sensitive D2C businesses.

## What To Edit First

Start with the smallest credible adoption path.

| Step | File | What to change |
|---|---|---|
| 1 | `ASSUMPTIONS_AND_BOUNDARIES.md` | Replace the Dorje-specific boundary with your own data boundary. Say exactly what data you do and do not have. |
| 2 | `04_data_model/sample_orders.csv` | Replace with a real or clearly labeled sample order export structure. Do not mix real and sample rows without labels. |
| 3 | `04_data_model/sample_ad_spend.csv` | Replace campaign rows with your channel structure, or remove channels you do not use. |
| 4 | `04_data_model/sample_product_catalog.csv` | Replace product names, SKUs, pricing, COGS, packaging, and shipping assumptions. |
| 5 | `02_metrics_os/decision_rules.md` | Adjust decision thresholds to your margin profile, replenishment cycle, and acquisition model. |
| 6 | `07_founder_review_system/weekly_revenue_review_memo.md` | Rewrite as this week's founder memo using your own labeled data. |

Do not start by rewriting every strategy file. The first working version should be one founder memo, one dashboard view, one decision log, and one data boundary.

## Minimum Data Needed

You can run a useful first review with:

- order date
- order ID
- customer ID or anonymized customer key
- product or SKU
- gross revenue
- discount amount
- shipping charged
- channel or source
- campaign name, if available
- new or returning customer flag
- estimated COGS
- estimated packaging cost
- estimated shipping cost
- payment fee assumption

If campaign data exists, add:

- spend
- impressions
- clicks
- sessions
- orders
- revenue
- CAC
- ROAS

If retention data exists, add:

- first order date
- second order date
- repeat purchase flag
- subscription flag
- subscription renewal status
- churn or cancellation reason, if available

## How To Adapt The Weekly Revenue Review

Use `templates/weekly-revenue-review-template.md` as the operating shell.

Each week, complete the memo in this order:

1. Write the one-paragraph founder summary first.
2. Fill revenue, acquisition, funnel, retention, and margin sections.
3. Identify the top three issues.
4. Separate founder decisions from operator actions.
5. Log every decision in `templates/founder-decision-log.md`.
6. Carry unresolved risks into the next weekly review.

Every section should end with a decision, risk, blocker, or action. If a metric does not change a decision, remove it from the founder review.

## How To Use The Templates

| Template | Use it for |
|---|---|
| `templates/weekly-revenue-review-template.md` | Weekly founder meeting prep and decision review |
| `templates/founder-decision-log.md` | Recording decisions, expected impact, follow-up date, actual result, and learning |
| `templates/day-1-data-request-checklist.md` | Requesting the minimum data needed to replace sample assumptions |

Keep the templates short. A founder should not need a full analytics handoff to understand the weekly operating decision.

## What Not To Copy Blindly

Do not copy these from the Dorje version without adapting:

- product names and buyer segments
- replenishment timing
- subscription prompts
- gifting logic
- contribution margin assumptions
- campaign channels
- discount thresholds
- seasonal windows
- risk register entries
- sample memo figures

Dorje is a premium Darjeeling tea example. Your category may have different repeat behavior, AOV, margin structure, purchase frequency, and founder decision cadence.

## Data Boundary And Credibility Note

This repo does not prove Dorje performance or claim access to internal Dorje systems. It demonstrates an operating approach.

When adapting this repo, label every data source:

- real internal data
- exported platform data
- public information
- sample data
- synthetic data
- assumption-based estimate

Do not present sample or synthetic data as actual company performance. If a number is not from an authorized company source, label it before using it in a founder-facing memo.
