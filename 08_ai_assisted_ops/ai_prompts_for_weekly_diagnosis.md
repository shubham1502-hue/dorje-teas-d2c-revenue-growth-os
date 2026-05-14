# AI Prompts for Weekly Diagnosis - Dorje Teas D2C Revenue Growth OS

> These prompts are for AI-assisted documentation and diagnosis using user-provided data.
> They must not be used to imply access to internal Dorje data. Paste only data the operator is authorised to use.

## Prompt 1: Weekly Revenue Diagnosis

**Input data required:** Weekly revenue table, channel table, product category table, contribution margin summary, retention summary.

```text
You are helping prepare a weekly Founder Revenue Review for Dorje Teas using public-information based operating logic and the data pasted below.

Data boundary:
- Treat all pasted numbers as operator-provided.
- Do not infer access to Shopify, ad accounts, or internal Dorje systems.
- Do not claim actual Dorje performance unless the pasted data explicitly says it is actual authorised data.

Task:
Diagnose what changed this week in D2C revenue. Separate activity from revenue progress. Evaluate revenue, returning customer share, contribution margin, CAC, ROAS, product mix, and retention signals.

Input:
[PASTE DATA HERE]

Output format:
1. One-paragraph founder summary
2. Top 3 movements
3. Top 3 risks
4. Decisions needed from founder
5. Operator actions this week

What not to overinterpret:
- Do not treat traffic growth as revenue progress.
- Do not treat ROAS as profitability without contribution margin.
- Do not assume a cohort is healthy without repeat purchase or LTV:CAC evidence.
```

## Prompt 2: Funnel Leak Identification

**Input data required:** Sessions, product page views, add-to-cart, checkout starts, purchases, CVR by channel, product-level CVR.

```text
Analyze the Dorje Teas D2C funnel using only the data below.

Task:
Find the largest funnel leak and explain the most likely operational cause. Connect the diagnosis to premium Darjeeling tea buying behavior, not generic ecommerce advice.

Input:
[PASTE DATA HERE]

Output format:
1. Biggest leak
2. Product or channel affected
3. Likely cause
4. Fix to test
5. Metric that decides scale, fix, or kill

What not to overinterpret:
- Do not assume low CVR means price is wrong.
- Do not recommend discounts unless contribution margin impact is checked.
- Do not blend Gift Buyer behavior with Daily Premium Tea Drinker behavior.
```

## Prompt 3: Channel Efficiency Audit

**Input data required:** Channel spend, revenue, CAC, ROAS, contribution ROAS, CVR, AOV, new customers, repeat signal if available.

```text
You are auditing Dorje Teas acquisition channels for profitable repeat D2C revenue.

Task:
Classify each channel as SCALE, HOLD, FIX, or PAUSE using contribution ROAS, CAC, CVR, and repeat purchase logic.

Input:
[PASTE DATA HERE]

Output format:
| Channel | Decision | Reason | Metric to watch next | Risk |

Decision rules:
- SCALE only if contribution ROAS and CVR are both strong.
- HOLD if economics are acceptable but not proven enough for more spend.
- FIX if intent exists but conversion or margin is weak.
- PAUSE if contribution economics are broken.

What not to overinterpret:
- Do not call a channel efficient because ROAS is high.
- Do not scale broad traffic without contribution margin and repeat logic.
```

## Prompt 4: Weekly Anomaly Check

**Input data required:** Week-over-week metrics, stock status, campaign status, fulfillment issues, tracking notes.

```text
Review the weekly Dorje Teas metrics below for anomalies that require operator attention.

Input:
[PASTE DATA HERE]

Task:
Identify anomalies in revenue, CVR, CAC, contribution margin, repeat purchase, stock, fulfillment, and subscription behavior.

Output format:
1. Anomaly
2. Severity
3. Likely cause
4. Data needed to confirm
5. Immediate action

What not to overinterpret:
- Do not assume causality from one-week movement.
- Do not attribute performance changes to a campaign unless the data supports it.
- Do not ignore operational causes such as stockout, shipping, or tracking breaks.
```

## Prompt 5: Monday Memo Draft

**Input data required:** Weekly dashboard export, experiment tracker, risk register updates, founder decisions needed.

```text
Draft a founder-readable Monday Revenue Review memo for Dorje Teas.

Use only the pasted data. Label any sample or synthetic figures clearly.

Input:
[PASTE DATA HERE]

Output format:
1. Week Summary
2. Revenue Performance
3. Acquisition Performance
4. Funnel Conversion
5. Product and Offer Performance
6. Repeat Purchase and Retention
7. Contribution Margin Summary
8. Top 3 Issues
9. Decisions Needed from Founder
10. Experiments Next Week

Writing rules:
- Be concise and decision-oriented.
- Explain what action follows from each metric.
- Do not use generic growth advice.
- Do not imply internal Dorje access unless provided data explicitly supports it.
```
