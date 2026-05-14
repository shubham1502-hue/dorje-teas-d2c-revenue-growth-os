# Founder Dashboard Spec — Dorje Teas

> Specification for the top-level weekly dashboard reviewed by the founder every Monday.
> Designed for decision velocity, not data completeness.
> All figures in examples are synthetic and illustrative. No internal Dorje data used.

---

## Design Principle

The founder dashboard is not a reporting tool. It is a **decision instrument**.

Every block answers one of five questions:
1. Is revenue trending in the right direction?
2. Is acquisition efficient this week?
3. Where is the funnel leaking?
4. Are customers coming back?
5. Is the business profitable per order?

If a block does not answer one of these five questions, it does not belong on the founder dashboard. Detailed breakdowns live in the campaign, retention, or margin dashboards — not here.

---

## Dashboard Structure — 10 Blocks

Readable in under 10 minutes. Decisions in under 30.

---

### Block 1 — Revenue Snapshot

**Purpose:** One-line answer to "how did we do this week?"

| Metric | This Week | Last Week | 4-Week Avg | WoW Change |
|---|---|---|---|---|
| Total D2C Revenue | ₹ | ₹ | ₹ | ▲/▼ % |
| New Customer Revenue | ₹ | ₹ | ₹ | ▲/▼ % |
| Returning Customer Revenue | ₹ | ₹ | ₹ | ▲/▼ % |
| Returning Rev as % of Total | % | % | % | ▲/▼ pp |

**Founder reads this to answer:** Did we grow? Was growth from new customers or returning customers?

**Flag:** Returning revenue share declining two weeks in a row → retention layer review required before any acquisition spend increase.

---

### Block 2 — Orders and AOV

**Purpose:** Separate volume and value — they move for different reasons.

| Metric | This Week | Last Week | WoW Change |
|---|---|---|---|
| Total Orders | # | # | % |
| New Customer Orders | # | # | % |
| Returning Customer Orders | # | # | % |
| Blended AOV | ₹ | ₹ | % |
| New Customer AOV | ₹ | ₹ | % |
| Returning Customer AOV | ₹ | ₹ | % |
| Discount Rate | % | % | pp |

**Founder reads this to answer:** Is revenue growth from volume, AOV, or discounting?

**Flag:** Revenue grew but discount rate rose and AOV dropped → volume manufactured by promotion. Watch contribution margin in Block 8.

---

### Block 3 — Paid Acquisition Summary

**Purpose:** Channel efficiency at a glance. Details live in the campaign dashboard.

| Channel | Spend | Revenue | ROAS | CAC | Contribution ROAS | Status |
|---|---|---|---|---|---|---|
| Google Search | ₹ | ₹ | x | ₹ | x | Scale / Hold / Fix / Pause |
| Google Shopping | ₹ | ₹ | x | ₹ | x | Scale / Hold / Fix / Pause |
| Meta Prospecting | ₹ | ₹ | x | ₹ | x | Scale / Hold / Fix / Pause |
| Meta Retargeting | ₹ | ₹ | x | ₹ | x | Scale / Hold / Fix / Pause |
| **Total Paid** | **₹** | **₹** | **x** | **₹** | **x** | — |

**Founder reads this to answer:** Which channel gets more budget next week?

**Hard rule:** No channel with Contribution ROAS below 1.0 is scaled without a margin fix plan. ROAS alone is not sufficient to approve a budget increase.

---

### Block 4 — Funnel Conversion

**Purpose:** Locate the primary conversion leak this week.

| Funnel Stage | This Week | Last Week | Change | Flag? |
|---|---|---|---|---|
| Sessions → Add-to-Cart | % | % | pp | Y/N |
| Add-to-Cart → Checkout | % | % | pp | Y/N |
| Checkout → Purchase | % | % | pp | Y/N |
| Overall CVR | % | % | pp | Y/N |

**Operator diagnosis (required — not optional):**
> [Specific: which stage dropped, on which product page, likely cause, proposed test. Example: "ATC rate on Green Tea dropped 2pp this week. Wellness search traffic landing on estate-origin page rather than health-benefit page. Proposing segment-specific landing page variant test starting Tuesday."]

**Founder reads this to answer:** Is there a leak, and does the operator know where it is and what to do?

---

### Block 5 — Product and Offer Performance

**Purpose:** Revenue and order mix by product — reveals mix shifts and campaign-to-product mismatches.

| Product | Orders | Revenue | AOV | vs. Last Week |
|---|---|---|---|---|
| First Flush | # | ₹ | ₹ | ▲/▼ % |
| Second Flush | # | ₹ | ₹ | ▲/▼ % |
| Original Darjeeling Chai | # | ₹ | ₹ | ▲/▼ % |
| Darjeeling Green Tea / Cold Brew Darjeeling | # | ₹ | ₹ | ▲/▼ % |
| Pyramid Teabags | # | ₹ | ₹ | ▲/▼ % |
| Cold Brew | # | ₹ | ₹ | ▲/▼ % |
| Selim Hill Gift Box Classic and Selim Hill Gift Box Premium | # | ₹ | ₹ | ▲/▼ % |
| Tea Club / Subscription | # | ₹ | ₹ | ▲/▼ % |

**Founder reads this to answer:** Is any product category declining despite spend? Is the revenue mix shifting toward lower-margin products?

**Flag:** Any product receiving campaign spend with declining order volume → campaign-to-page mismatch. Check Block 3 and funnel together.

---

### Block 6 — Repeat Purchase and Retention

**Purpose:** Signal the health of Dorje's customer retention loop.

| Metric | This Week | Last Week | Change |
|---|---|---|---|
| Returning Customer Orders | # | # | % |
| Returning Customer Revenue | ₹ | ₹ | % |
| Email / WhatsApp Flow Revenue | ₹ | ₹ | % |
| Active Subscribers | # | # | % |
| New Subscribers This Week | # | # | |
| Subscription Renewals (completed / due) | # / # | # / # | % |
| Subscription Churn This Week | # | # | |

**Monthly cohort update (filled once per month):**
> Cohort: [Month] | Repeat Rate Day 30: % | Day 60: % | Day 90: %

**Founder reads this to answer:** Is the retention loop working? Are subscribers renewing faster than they are churning?

**Flag:** Subscription churn exceeds new subscribers in any week → active base is shrinking. Investigate immediately — churn reason audit before next renewal cycle.

---

### Block 7 — Active Experiments

**Purpose:** Keep the founder sighted on tests and pending decisions.

| Experiment | Hypothesis | Metric | Start Date | Status | Decision Needed? |
|---|---|---|---|---|---|
| [Name] | [If X → Y because Z] | [Metric] | [Date] | Running / Complete | Yes / No |

**Experiments closing this week:**

| Experiment | Result | Recommendation | Deadline |
|---|---|---|---|
| [Name] | [What happened] | Scale / Fix / Kill | [Date] |

**Flag:** More than 3 experiments running simultaneously → measurement noise risk. Any experiment running more than 4 weeks without a decision → close it.

---

### Block 8 — Contribution Margin Summary

**Purpose:** The single most important block. ROAS without CM is incomplete. This block is what prevents scaling a loss.

| Line Item | This Week | Last Week | Change |
|---|---|---|---|
| Gross Revenue | ₹ | ₹ | % |
| Less: Discounts | ₹ | ₹ | % |
| Less: Product COGS | ₹ | ₹ | % |
| Less: Packaging | ₹ | ₹ | % |
| Less: Shipping | ₹ | ₹ | % |
| Less: Payment Fees (~2%) | ₹ | ₹ | % |
| **= Gross Margin** | **₹** | **₹** | **%** |
| Less: Paid Media | ₹ | ₹ | % |
| **= Contribution Margin** | **₹** | **₹** | |
| **CM %** | **%** | **%** | **pp** |

**Conditional formatting:**
- CM% ≥ 20%: green
- CM% 10–19%: amber — watch
- CM% < 10% or negative: red — immediate diagnosis required

**Founder reads this to answer:** Are we making money per order this week, after every variable cost?

**Hard rule:** No budget increase approved in Block 3 without this block showing positive CM%. If CM% is declining, find the cost line that is moving before spending more.

---

### Block 9 — Top 3 Issues This Week

**Purpose:** Force prioritization. Only three. Stated specifically.

**Issue 1:**
> [Metric that flagged it → what it showed → proposed action]

**Issue 2:**
> [Metric that flagged it → what it showed → proposed action]

**Issue 3:**
> [Metric that flagged it → what it showed → proposed action]

**Quality bar:** "Traffic is soft" is not an issue. "Blended CVR dropped 1.8pp WoW, driven by Green Tea page, likely wellness search traffic seeing estate-origin framing. Proposed fix: wellness landing page variant test starting Tuesday" is an issue. Every issue must name a metric, describe what it showed, and specify the next action.

---

### Block 10 — Decisions Needed from Founder

**Purpose:** The most important block. Separates founder-level decisions from operator decisions.

| Decision | Context | Options | Operator Recommendation | Deadline |
|---|---|---|---|---|
| [Decision topic] | [Why this needs founder input] | [A / B / C] | [Recommended option + brief rationale] | [Date] |

**Examples of correct founder decisions:**
- Scale Google Search spend by ₹30,000/week — Contribution ROAS is 2.1x, CAC is within LTV threshold
- Launch corporate gifting campaign before Diwali window — requires budget and team prioritization call
- Raise free-shipping threshold from ₹500 to ₹700 — improves CM but may reduce CVR; founder judgment on trade-off
- Introduce quarterly subscription tier — product and pricing decision

**Examples of what should NOT be in Block 10:**
- Which creative to test next (operator decision)
- Which email to send this week (operator decision)
- How to fix a broken flow (operator decision)

**Rule:** If the founder does not have at least one decision in Block 10 in the first 3 months, either the system is running perfectly (unlikely), or the operator is not surfacing what needs founder judgment (likely). Default toward more transparency, not less.

---

## Dashboard Operating Rules

1. **Every red cell requires a written annotation.** A red number without an explanation is an unresolved alert, not a data point.
2. **Block 9 is written before the tables.** Synthesis comes before data retrieval — this prevents the operator from hiding behind the numbers.
3. **No metric appears without a comparison.** Every number shows vs. last week, vs. target, or vs. 4-week average.
4. **Dashboard is complete within 90 minutes.** If it takes longer, the data pipeline is broken — fix the source, not the dashboard.
5. **Block 10 is the final checkpoint before the founder meeting.** If there is nothing in Block 10, the meeting agenda should reflect that — shorter review, more focus on experiments and next week.

---

## Delivery Spec

| Item | Detail |
|---|---|
| Format | Google Sheets (live view) + weekly Markdown memo (async reading) |
| Delivery | Sunday evening, before Monday morning review |
| Meeting | 30-minute Monday revenue review using this as the agenda |
| Data reconciliation | All Shopify numbers reconciled before delivery; all ad spend pulled from platform |
| Owner | Founder's Office / Revenue Ops |

---

## What This Dashboard Deliberately Excludes

- Vanity metrics: follower count, raw impressions, total website traffic without conversion context
- Revenue without margin: GMV without CM is misleading for a premium D2C brand
- Creative-level performance: lives in the campaign dashboard
- Cohort LTV curves: lives in the retention dashboard
- Full P&L: lives in the monthly business review

The founder dashboard is a decision surface. Everything else is a supporting dashboard.
