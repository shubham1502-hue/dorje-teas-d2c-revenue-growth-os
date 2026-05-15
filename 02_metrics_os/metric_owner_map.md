# Metric Owner Map  -  Dorje Teas

> Defines who owns each metric, where the data comes from, how often it is reviewed,
> and what triggers escalation to the founder.
> Designed for a small Founder's Office team operating across growth, ops, and finance.
> No internal Dorje org data used  -  this is a template for a typical early-stage D2C setup.

---

## Why Ownership Matters

In an early-stage D2C team, metrics without owners become reports without actions. The goal of this map is to ensure:

1. Every metric has exactly one owner  -  the person who pulls it, monitors it, and flags when it moves
2. Every owner knows where the data lives and how often to look at it
3. Every escalation trigger is defined in advance, not improvised

This map is not about hierarchy. It is about clarity.

---

## Ownership Roles (Typical Early-Stage D2C Team)

| Role | What They Own |
|---|---|
| **Founder's Office / Revenue Ops** | Weekly dashboard, contribution margin, experiment tracker, cross-functional flags |
| **Growth / Performance** | Paid acquisition, campaign dashboards, CAC, ROAS, CTR, CVR, landing page performance |
| **Retention / CRM** | Email and WhatsApp flows, repeat purchase rate, subscription, winback |
| **Finance / Ops** | COGS, packaging cost, shipping cost, payment fees, refund rate |
| **Founder** | Strategic decisions  -  budget allocation, pricing, channel scale/pause |

---

## Acquisition Metrics

Escalation thresholds are illustrative benchmarks for the synthetic operating model.

| Metric | Owner | Data Source | Review Frequency | Escalation Trigger [illustrative] |
|---|---|---|---|---|
| Total Sessions | Growth | GA4 / Shopify | Weekly | Drop >20% WoW without campaign change |
| CTR (by campaign) | Growth | Google Ads / Meta | Weekly | Drop >20% WoW  -  creative fatigue signal |
| CPC (by campaign) | Growth | Google Ads / Meta | Weekly | Rise >25% WoW on stable campaigns |
| CPM | Growth | Google Ads / Meta | Weekly | Rise >30% WoW  -  audience saturation |
| CAC (blended) | Founder's Office | Ads spend ÷ new customers | Weekly | CAC exceeds break-even CAC for 2 weeks |
| CAC (by channel) | Growth | Channel spend ÷ channel new customers | Weekly | Any channel CAC >2× blended average |
| New Customers Acquired | Founder's Office | Shopify | Weekly | New customer volume drops >25% WoW |
| ROAS (by channel) | Growth | Platform dashboards | Weekly | ROAS drops below 2x on any scaled channel |
| Contribution ROAS | Founder's Office | CM ÷ channel spend | Weekly | Contribution ROAS below 1.0 on any channel |
| Search Impression Share | Growth | Google Ads | Monthly | Impression share declining vs. prior month |

---

## Conversion Metrics

| Metric | Owner | Data Source | Review Frequency | Escalation Trigger |
|---|---|---|---|---|
| Sessions → Product Page View | Growth | GA4 / Shopify | Weekly | Drop >15% WoW  -  traffic quality or navigation issue |
| Product Page → Add-to-Cart | Growth | GA4 / Shopify / Hotjar | Weekly | Drop >15% WoW  -  trust, price, or content issue |
| Add-to-Cart → Checkout | Growth | Shopify | Weekly | Drop >10% WoW  -  checkout friction |
| Checkout → Purchase (CVR) | Growth | Shopify | Weekly | Drop >10% WoW  -  payment or last-mile friction |
| Overall CVR | Founder's Office | Shopify | Weekly | Drop >15% WoW blended  -  multi-stage audit required |
| CVR by product page | Growth | GA4 / Shopify | Weekly | Any product page CVR below 1% with >500 sessions |
| CVR by channel | Growth | GA4 + Shopify | Weekly | Any channel with >₹5K spend and CVR below 0.8% |
| Free-shipping threshold completion | Founder's Office | Shopify cart data | Monthly | Completion rate declining  -  threshold may need adjustment |

---

## Order Economics Metrics

| Metric | Owner | Data Source | Review Frequency | Escalation Trigger |
|---|---|---|---|---|
| AOV (blended) | Founder's Office | Shopify | Weekly | Drop >10% WoW without volume explanation |
| AOV by product category | Founder's Office | Shopify order export | Weekly | Gift box AOV declining  -  discount rate check |
| AOV by new vs. returning | Founder's Office | Shopify | Monthly | Returning customer AOV dropping  -  cross-sell failure signal |
| Discount rate | Founder's Office | Shopify | Weekly | Exceeds 15% on full-price products |
| Discount rate by SKU | Finance / Ops | Shopify | Monthly | Any SKU with >20% discount rate  -  margin risk |
| Refund rate | Finance / Ops | Shopify | Monthly | Exceeds 2%  -  product or logistics quality signal |
| Cart abandonment rate | Growth | Shopify / GA4 | Weekly | Rises >5pp WoW  -  checkout friction or offer issue |

---

## Margin Metrics

| Metric | Owner | Data Source | Review Frequency | Escalation Trigger |
|---|---|---|---|---|
| Product COGS per SKU | Finance / Ops | Internal sourcing records | Monthly (or on change) | COGS rises >10% on any SKU |
| Packaging cost per order | Finance / Ops | Procurement records | Monthly | Packaging cost per order rises >₹15 |
| Shipping cost per order | Finance / Ops | Logistics partner data | Weekly | Shipping cost per order rises >₹20 |
| Payment gateway fee | Finance / Ops | Gateway dashboard | Monthly | Rate change or unexpected fee spike |
| Gross margin by product | Founder's Office | Orders + COGS | Monthly | Gross margin below 40% on any SKU |
| Contribution margin (blended) | Founder's Office | Weekly dashboard | Weekly | CM negative on any channel for 2 consecutive weeks |
| CM by channel | Founder's Office | Weekly dashboard | Weekly | Any scaled channel with CM% below 10% |
| CM by product | Founder's Office | Monthly review | Monthly | Gift boxes or bundles with negative CM after packaging |
| Break-even CAC | Founder's Office | Gross margin per order | Monthly (or on COGS change) | CAC approaches break-even  -  acquisition health signal |
| LTV:CAC ratio | Founder's Office | Cohort data + channel CAC | Monthly | Any channel LTV:CAC below 1.5x at 3-month cohort |

---

## Retention Metrics

| Metric | Owner | Data Source | Review Frequency | Escalation Trigger |
|---|---|---|---|---|
| Repeat purchase rate | Retention / CRM | Shopify cohort export | Monthly | Drops >5pp vs. prior cohort at same month |
| Time to second purchase | Retention / CRM | Shopify order data | Monthly | Median rises >5 days vs. prior cohort |
| Returning customer revenue % | Founder's Office | Shopify | Weekly | Drops below 30% of total weekly revenue |
| Email open rate (flows) | Retention / CRM | Email platform | Weekly | Open rate drops below 20% on any automated flow |
| Email click-to-purchase rate | Retention / CRM | Email platform | Weekly | Click rate below 1% on replenishment flow |
| WhatsApp delivery and click rate | Retention / CRM | WhatsApp platform | Weekly | Delivery failures >5% or click rate below 10% |
| Winback reactivation rate | Retention / CRM | Shopify + email platform | Monthly | Below 5%  -  winback copy or offer needs revision |
| Flow revenue as % of total | Founder's Office | Email / WhatsApp platform | Monthly | Below 10%  -  retention infrastructure underdeveloped |

---

## Subscription Metrics

| Metric | Owner | Data Source | Review Frequency | Escalation Trigger |
|---|---|---|---|---|
| Active subscriber count | Retention / CRM | Shopify subscription app | Weekly | Drops two weeks in a row |
| New subscribers (weekly) | Retention / CRM | Subscription app | Weekly | Zero or near-zero for 2 weeks |
| Subscription attach rate (overall) | Founder's Office | Subscription app + Shopify | Monthly | Below 5% of eligible buyers (post-2nd purchase) |
| Subscription attach rate by SKU | Retention / CRM | Subscription app | Monthly | Chai or Second Flush attach below 8% |
| Subscription renewal rate | Retention / CRM | Subscription app | Monthly | Below 75% in any month |
| Subscription churn rate | Retention / CRM | Subscription app | Monthly | Exceeds 15% in any month |
| Churn reason breakdown | Retention / CRM | Cancel flow survey | Monthly | Any reason category >30% of churns |
| Subscription AOV | Founder's Office | Subscription app | Monthly | Drops vs. one-time AOV  -  offer or SKU mix issue |
| Subscription CM vs. one-time CM | Founder's Office | Weekly dashboard | Monthly | Subscription CM below one-time CM  -  pricing or discount issue |

---

## Experiment Metrics

| Metric | Owner | Data Source | Review Frequency | Escalation Trigger |
|---|---|---|---|---|
| Active experiments count | Founder's Office | Experiment tracker | Weekly | More than 3 experiments running simultaneously  -  measurement noise |
| Experiment completion rate | Founder's Office | Experiment tracker | Weekly | Any experiment running >4 weeks without a decision |
| Experiments with clear decisions | Founder's Office | Experiment tracker | Monthly | Decision rate below 80%  -  experiments not being closed |
| Revenue from experiments | Founder's Office | Shopify + experiment tracker | Monthly | Experiment pipeline producing less than 1 scaling decision per month |

---

## Summary: Who Reviews What on Monday Morning

| Reviewer | What They Bring to Monday Review |
|---|---|
| Founder's Office | Weekly dashboard with revenue, acquisition, margin, retention summary; top 3 issues; founder decisions needed |
| Growth | Campaign-level ROAS, CTR, CVR, CAC, and channel status (scale / hold / fix / pause) |
| Retention / CRM | Flow performance, repeat purchase rate update, subscription active count, churn flags |
| Finance / Ops | Shipping cost per order (weekly), any COGS or packaging cost changes, refund rate |
| Founder | Reviews memo prepared by Founder's Office; makes decisions flagged in Section 9 |

---

## Ownership Rules

1. **One owner per metric.** If two people own the same metric, no one owns it.
2. **Owner is responsible for the data, not just the number.** If the data is wrong, the owner flags it before it enters a report.
3. **Escalation triggers are standing instructions.** The owner does not wait for a meeting to flag an escalation trigger  -  they flag it in Slack or the weekly memo the moment it fires.
4. **Metrics without decisions are noise.** If a metric is reviewed weekly but has never produced a decision, question whether it belongs in the weekly review.
