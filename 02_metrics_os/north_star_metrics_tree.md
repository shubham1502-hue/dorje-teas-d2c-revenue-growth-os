# North Star Metrics Tree — Dorje Teas

> Revenue metric hierarchy for a premium Darjeeling D2C brand.
> Every metric in this tree connects upward to the north star and downward to a specific decision.
> All figures are synthetic and illustrative. No internal Dorje data used.

---

## The North Star Metric

> **contribution-margin-positive repeat D2C revenue**

Not GMV. Not ROAS. Not new customer count.

The metric that matters: **are we acquiring customers who come back profitably?**

This north star has three components that must be true simultaneously:

| Component | What It Means |
|---|---|
| Contribution-margin-positive | Revenue after product cost, packaging, shipping, discounts, payment fees, and paid media spend is positive |
| Repeat | A growing share of revenue comes from returning customers, not just first-time buyers |
| D2C | Revenue generated on the owned channel — not marketplace, not distributor — where Dorje controls the data, the experience, and the margin |

If any one component is missing, the growth model has a structural problem:
- High revenue, negative contribution margin → scaling a loss
- Positive margin, no repeat → paying full CAC for every order indefinitely
- Strong repeat, but only on marketplace → no owned data, margin leakage to platform fees

---

## The Metrics Tree

Data sources for this tree are Shopify/order exports, ad platform reporting, subscription app exports, and ops cost inputs; synthetic files in `04_data_model/` stand in for those sources in this repo.

```
NORTH STAR
contribution-margin-positive repeat D2C revenue
│
├── REVENUE LAYER
│   ├── Total D2C Revenue
│   │   ├── New Customer Revenue
│   │   └── Returning Customer Revenue  ← primary growth indicator
│   │
│   ├── Revenue by Product Category
│   │   ├── First Flush / Second Flush
│   │   ├── Daily Replenishment (Chai, Teabags)
│   │   ├── Darjeeling Green Tea / Cold Brew Darjeeling
│   │   ├── Selim Hill Gift Box Classic and Selim Hill Gift Box Premium
│   │   └── Cold Brew
│   │
│   └── Revenue by Channel
│       ├── Google Search
│       ├── Meta (Prospecting)
│       ├── Meta (Retargeting)
│       ├── Email / WhatsApp (Retention)
│       ├── Organic / Direct
│       └── Other (Marketplace, Referral)
│
├── ACQUISITION LAYER
│   ├── Sessions (by channel)
│   ├── Click-Through Rate (CTR)
│   ├── Cost Per Click (CPC)
│   ├── Cost Per Mille (CPM)
│   ├── Customer Acquisition Cost (CAC)
│   │   └── CAC = Total Channel Spend ÷ New Customers Acquired
│   └── Return on Ad Spend (ROAS)
│       └── ROAS = Revenue ÷ Spend
│           └── Contribution ROAS = (Revenue − Variable Costs) ÷ Spend
│               ← the number ROAS alone misses
│
├── CONVERSION LAYER
│   ├── Sessions → Product Page View Rate
│   ├── Product Page View → Add-to-Cart Rate
│   ├── Add-to-Cart → Checkout Initiation Rate
│   ├── Checkout Initiation → Purchase Rate
│   └── Overall CVR = Orders ÷ Sessions
│       ├── CVR by channel
│       ├── CVR by product category
│       └── CVR by new vs. returning visitor
│
├── ORDER ECONOMICS LAYER
│   ├── Average Order Value (AOV)
│   │   ├── AOV by product category
│   │   ├── AOV by new vs. returning
│   │   └── AOV by channel
│   ├── Discount Rate = Discounted Revenue ÷ Gross Revenue
│   ├── Refund Rate = Refunds ÷ Orders
│   └── Free-Shipping Threshold Completion Rate
│
├── MARGIN LAYER
│   ├── Gross Revenue
│   │   − Discounts
│   │   − Product COGS
│   │   − Packaging Cost
│   │   − Shipping Cost
│   │   − Payment Gateway Fee (~2%)
│   │   = Gross Margin
│   │   − Paid Media Spend (attributed)
│   │   = Contribution Margin
│   │
│   ├── CM by product
│   ├── CM by channel
│   ├── CM by new vs. returning order
│   └── CM by subscription vs. one-time
│
├── RETENTION LAYER
│   ├── Repeat Purchase Rate
│   │   └── % of Month N buyers who purchase again in Month N+1, N+2, N+3
│   ├── Time to Second Purchase (days)
│   ├── Purchase Frequency (orders per customer per 90 days)
│   ├── Revenue from Returning Customers ÷ Total Revenue
│   └── Winback Rate (% of 60+ day dormant customers who reactivate)
│
├── SUBSCRIPTION LAYER
│   ├── Subscription Attach Rate (by SKU and overall)
│   │   └── % of eligible buyers who convert to subscription
│   ├── Trial to Active Subscription Rate
│   ├── Monthly Renewal Rate
│   ├── Subscription Churn Rate
│   ├── Subscription AOV
│   ├── Subscription CM (vs. one-time CM)
│   └── Active Subscriber Count (trend)
│
└── LTV LAYER
    ├── LTV (90-day and 12-month, cohort-based)
    │   └── LTV = AOV × Purchase Frequency × Retention Rate
    ├── LTV:CAC Ratio (by channel)
    │   └── Target: >2x at 12 months
    └── Payback Period
        └── Months to recover CAC from CM-positive orders
```

---

## Four Questions the Tree Answers Every Week

### Q1 — Is revenue growing from the right source?

Check: **Returning Customer Revenue ÷ Total Revenue (weekly trend)**

If new customer revenue grows but returning customer revenue is flat, Dorje is on a treadmill — constantly re-acquiring at full CAC without building a compounding customer base.

A premium brand with strong repeat behavior should trend toward returning customers representing 40–50%+ of revenue within 6–12 months of a cohort's first purchase.

---

### Q2 — Is acquisition efficient?

Check: **CAC by channel → Contribution ROAS by channel**

ROAS alone does not confirm acquisition efficiency. A 3x ROAS with 40% gross margin and high Darjeeling-to-door shipping costs may be contribution-margin-negative after variable costs.

**Contribution ROAS = (Revenue − Variable Costs) ÷ Spend**

If contribution ROAS is below 1.0, the channel is losing money on every order, regardless of what the reported ROAS shows.

---

### Q3 — Where is the funnel leaking?

Check: **Sessions → Add-to-Cart → Checkout → Purchase** (by stage, by product, by channel)

A drop at the product page (high sessions, low add-to-cart) signals a trust, price perception, or clarity problem — often fixable with asset sequencing or price-per-cup framing.

A drop at checkout (high add-to-cart, low purchase completion) signals friction — payment options, delivery concern, or second-guessing on price. Different diagnosis, different fix.

Do not treat all CVR problems as the same problem.

---

### Q4 — Is the business building compounding revenue?

Check: **Repeat Purchase Rate → Subscription Attach Rate → LTV:CAC**

A compounding brand has:
- Repeat purchase rate increasing cohort-over-cohort
- Subscription attach rate above 10–15% for daily replenishment SKUs
- LTV:CAC above 2x at 12 months

A non-compounding brand has flat repeat rate, low subscription attach, and an LTV:CAC below 1.5x — meaning it costs more than 8 months of margin to recover each customer acquired.

---

## Metric Review Frequency

Review thresholds below are illustrative benchmarks for the synthetic operating model.

| Layer | Metric | Review Frequency | Decision Trigger |
|---|---|---|---|
| Revenue | Total D2C revenue, new vs. returning split | Weekly | Revenue flat or declining vs. prior week |
| Acquisition | CAC, ROAS, Contribution ROAS by channel | Weekly | CAC above break-even for 2 consecutive weeks |
| Conversion | CVR by stage, CTR, CPC | Weekly | CVR drops >15% week-over-week |
| Order Economics | AOV, discount rate, refund rate | Weekly | AOV drops or discount rate rises unexpectedly |
| Margin | CM by channel and product | Weekly | CM negative on any scaled channel |
| Retention | Repeat purchase rate, time to second purchase | Monthly (cohort) | Repeat rate declining for 2+ cohorts |
| Subscription | Active count, renewal rate, churn | Monthly | Churn above 10% in any single month |
| LTV | LTV:CAC, payback period | Monthly | LTV:CAC below 2x at 6-month cohort mark [illustrative benchmark] |

---

## Metric Pairs That Must Be Read Together

| Metric | Never Read Without |
|---|---|
| ROAS | Contribution margin |
| New customer count | Repeat purchase rate |
| Revenue | Discount rate |
| Subscription count | Renewal rate and churn |
| AOV | CM % (high AOV can still be low-margin on gift boxes) |
| CAC | LTV:CAC and payback period |
| CTR | CVR (high CTR + low CVR = wrong audience or wrong landing page) |

---

## Escalation Triggers (Operator → Founder)

Escalation thresholds below are illustrative benchmarks for the synthetic operating model.

| Condition | Action |
|---|---|
| CAC exceeds gross margin per first order for 2 consecutive weeks | Pause spend increase; escalate |
| Contribution margin goes negative on a scaled channel | Immediate flag; pause scaling |
| Repeat purchase rate drops >5pp month-over-month | Retention layer diagnosis; escalate |
| Subscription churn exceeds renewal rate for 2 consecutive weeks | Subscription experience review |
| AOV drops >10% without a promotional explanation | Offer or discount rate review |
| Discount rate on full-price products exceeds 15% | Premium positioning risk flag |
| Delivery complaint rate spikes alongside repeat purchase drop | Logistics review alongside retention review |
