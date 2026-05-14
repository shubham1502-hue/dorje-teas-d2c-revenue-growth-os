# Retention Dashboard Spec — Dorje Teas

> Defines the monthly retention dashboard used by the Retention / CRM operator.
> Covers repeat purchase, cohort behavior, subscription health, and lifecycle flow performance.
> All figures are synthetic and illustrative. No internal Dorje data used.

---

## Purpose

The retention dashboard answers: **are customers who bought from Dorje coming back, and are the lifecycle systems working to bring them back profitably?**

For a premium Darjeeling tea brand, retention is not optional — it is the business model. At a CAC typical of premium D2C brands, the first purchase often does not recover acquisition cost. The second and third purchases are where the economics work.

---

## Dashboard Structure (6 Views)

---

### View 1 — Retention Health Summary (Monthly Snapshot)

A single-page summary updated at the start of each month.

All example values and targets in this dashboard spec are illustrative [SYNTHETIC] placeholders.

| Metric | Current Month | Prior Month | Change | Target | Status |
|---|---|---|---|---|---|
| Repeat Purchase Rate (overall) | % | % | pp | >30% | Healthy / Watch / Act |
| Returning Customer Revenue % | % | % | pp | >35% | Healthy / Watch / Act |
| Time to Second Purchase (median) | days | days | days | <35 days | Healthy / Watch / Act |
| Active Subscribers | # | # | % | ↑ MoM | Healthy / Watch / Act |
| Subscription Renewal Rate | % | % | pp | >80% | Healthy / Watch / Act |
| Subscription Churn Rate | % | % | pp | <12% | Healthy / Watch / Act |
| Email Flow Revenue % of Total | % | % | pp | >12% | Healthy / Watch / Act |
| Winback Reactivation Rate | % | % | pp | >8% | Healthy / Watch / Act |

**Conditional formatting:**
- Healthy: at or above target
- Watch: within 20% of target — watch
- Act: more than 20% below target — act

**Operator annotation:**
> [What is the retention story this month? What is working? What needs attention?]

---

### View 2 — Monthly Cohort Table

Tracks repeat purchase behavior for each acquisition month's customer cohort.

| Acquisition Month | New Customers | Month 0 Revenue | Month 1 Repeat % | Month 1 Revenue | Month 2 Repeat % | Month 2 Revenue | Month 3 Repeat % | Month 3 Revenue | 3-Month LTV |
|---|---|---|---|---|---|---|---|---|---|
| Jan 2025 [SYNTHETIC] | 180 | ₹1,44,000 | 22% | ₹63,360 | 18% | ₹46,080 | 15% | ₹32,400 | ₹1,56,420 |
| Feb 2025 [SYNTHETIC] | 145 | ₹1,16,000 | 24% | ₹55,680 | 19% | ₹41,760 | 14% | ₹28,420 | ₹1,25,860 |
| Mar 2025 [SYNTHETIC] | 210 | ₹1,68,000 | 26% | ₹87,360 | 21% | ₹64,680 | — | — | — |
| Apr 2025 [SYNTHETIC] | 195 | ₹1,56,000 | 28% | ₹87,360 | — | — | — | — | — |
| May 2025 [SYNTHETIC] | 230 | ₹1,84,000 | — | — | — | — | — | — | — |

**How to read this table:**
- Month 0 = the acquisition month (first purchase revenue)
- Month 1 Repeat % = what % of that cohort made a second purchase in Month 1 after acquisition
- The repeat % should generally be stable or improving cohort-over-cohort
- A declining repeat % across cohorts is the earliest signal of retention system failure

**Signals to watch:**
- Is the Month 1 repeat % improving as lifecycle flows mature? It should, as flows improve.
- Is any cohort's LTV declining vs. prior cohorts? Investigate product mix and post-purchase experience changes for that period.
- Is the March cohort (First Flush season) showing higher 3-month LTV? First Flush buyers are hypothesized to have stronger retention — validate this with cohort data.

---

### View 3 — Time to Second Purchase Distribution

Shows how quickly first-time buyers return — by product purchased and by cohort month.

**Median time to second purchase by first product:**

| First Product Purchased | Median Days to 2nd Purchase | Target | Status |
|---|---|---|---|
| Original Darjeeling Chai | — days [SYNTHETIC] | <25 days | Healthy / Watch / Act |
| Pyramid Teabags | — days [SYNTHETIC] | <30 days | Healthy / Watch / Act |
| First Flush | — days [SYNTHETIC] | <45 days | Healthy / Watch / Act |
| Second Flush | — days [SYNTHETIC] | <35 days | Healthy / Watch / Act |
| Green Tea | — days [SYNTHETIC] | <40 days | Healthy / Watch / Act |
| Gift Box | — days [SYNTHETIC] | <60 days (to self-purchase) | Healthy / Watch / Act |

**Why targets differ by product:**
- Chai is consumed daily — 100g lasts ~20–25 days at daily use. A 25-day return cycle means the lifecycle flow is working.
- First Flush is a seasonal product — replenishment is limited by harvest availability. Target is a Second Flush or Tea Club conversion, not same-product repurchase.
- Gift boxes have a different target — the "second purchase" goal is a self-purchase, which requires a longer window and a different lifecycle message.

**Distribution histogram (for the Google Sheets build):**

Track the % of repeat customers who return in each time bucket:

| Time Bucket | % of Repeat Buyers |
|---|---|
| Day 0–14 | % |
| Day 15–21 | % |
| Day 22–30 | % |
| Day 31–45 | % |
| Day 46–60 | % |
| Day 61–90 | % |
| Day 90+ | % |

If the Day 22–30 bucket has the highest concentration, the Day 21 replenishment flow is working. If Day 31–45 dominates, the flow may be firing too late for faster-consuming products.

---

### View 4 — Subscription Health

Tracks Tea Club and product-level subscription performance.

**Overall subscription metrics:**

| Metric | This Month | Last Month | Change | Target |
|---|---|---|---|---|
| Total Active Subscribers | # | # | % | ↑ MoM |
| New Subscribers (MoM) | # | # | % | — |
| Subscribers Lost (churned) | # | # | % | <12% churn rate |
| Net Subscriber Change | # | # | % | Positive |
| Subscription Revenue | ₹ | ₹ | % | — |
| Subscription Renewal Rate | % | % | pp | >80% |
| Subscription AOV | ₹ | ₹ | % | ≥ one-time AOV |
| Subscription CM% | % | % | pp | > one-time CM% |

**Subscription attach rate by SKU:**

| SKU / Product | Eligible Buyers (post-2nd purchase) | Converted to Subscription | Attach Rate | Target |
|---|---|---|---|---|
| Original Darjeeling Chai | # | # | % | >12% |
| Tea Club | # | # | % | >8% |
| Tea Club | # | # | % | >8% |
| Second Flush | # | # | % | >6% |
| Pyramid Teabags | # | # | % | >6% |

**Churn reason breakdown (from cancel flow survey):**

| Reason | Count | % of Churns | Action |
|---|---|---|---|
| Over-supplied / too much tea | # | % | Offer delivery frequency change |
| Product quality concern | # | % | Escalate to ops; investigate |
| Price / value concern | # | % | Review subscription offer vs. one-time |
| Forgot / unexpected charge | # | % | Improve pre-renewal nudge copy |
| Switching to a different product | # | % | Offer SKU swap instead of cancel |
| Temporary — pausing | # | % | Offer pause option (reduce churn) |
| Other | # | % | Review individually |

**Operator action rule:** If any single churn reason exceeds 30% of monthly churns, it is a systemic issue — not a one-off. Fix the system before the next renewal cycle.

---

### View 5 — Lifecycle Flow Performance

Tracks email and WhatsApp flow performance across the customer lifecycle.

| Flow Name | Trigger | Recipients (MoM) | Open Rate | Click Rate | Click-to-Purchase | Revenue | Status |
|---|---|---|---|---|---|---|---|
| Day 7 Brewing Education | Post first purchase | # | % | % | % | ₹ | Healthy / Watch / Act |
| Day 21 Replenishment Nudge | Post first purchase | # | % | % | % | ₹ | Healthy / Watch / Act |
| Day 30 Cross-Sell | Post first purchase | # | % | % | % | ₹ | Healthy / Watch / Act |
| Day 45 Subscription Prompt | Post second purchase | # | % | % | % | ₹ | Healthy / Watch / Act |
| Gift Buyer — Day 14 Self-Purchase | Post gift box purchase | # | % | % | % | ₹ | Healthy / Watch / Act |
| Winback — Day 60 Dormant | 60+ days no purchase | # | % | % | % | ₹ | Healthy / Watch / Act |
| Pre-Renewal Nudge | 5 days before subscription renewal | # | % | % | % | ₹ | Healthy / Watch / Act |
| First Flush Harvest Update | Pre-season, past First Flush buyers | # | % | % | % | ₹ | Healthy / Watch / Act |

**Flow performance thresholds:**

| Metric | Healthy | Watch | Act |
|---|---|---|---|
| Email open rate | >30% | 20–30% | <20% |
| Email click rate | >5% | 2–5% | <2% |
| Click-to-purchase rate | >15% | 8–15% | <8% |
| WhatsApp click rate | >20% | 12–20% | <12% |

**Operator annotation:**
> [Which flow underperformed this month? Was it a delivery issue, copy issue, or timing issue? What is being changed?]

---

### View 6 — Segment-Level Retention Comparison

Compares repeat purchase rate across buyer segments to identify which segments retain well and which need work.

| Segment | New Customers (MoM) | Month 1 Repeat % | Month 3 Repeat % | Subscription Attach % | Avg LTV (3-month) |
|---|---|---|---|---|---|
| Daily Premium Tea Drinker (Chai buyers) | # | % | % | % | ₹ |
| Darjeeling Loyalist (First/Second Flush) | # | % | % | % | ₹ |
| Gift Buyer (Gift Box first purchase) | # | % (self-purchase) | % | % | ₹ |
| Health/Wellness Consumer (Green Tea first) | # | % | % | % | ₹ |
| Climate/Story-Led Buyer (via content) | # | % | % | % | ₹ |

**What to look for:**
- Darjeeling Loyalist segment should show the highest 3-month repeat % and Tea Club attach rate
- Daily Premium Tea Drinker segment should show the fastest time to second purchase and highest Chai subscription attach
- Gift Buyer segment will show the lowest same-product repeat % — track self-purchase conversion, not replenishment
- Health/Wellness Consumer segment may have slower repeat cycles — 45-day intervals are expected for Green Tea

---

## Retention Dashboard Operating Rules

1. **Cohort table is updated on the 1st of each month.** It requires the prior month's complete order data.
2. **Subscription churn reason analysis is reviewed monthly without exception.** Without this, churn reduction is guesswork.
3. **Any flow with open rate below 20% for 2 consecutive months gets a copy and timing review** before the next month.
4. **Time-to-second-purchase by product is the early warning system.** If it lengthens without a calendar reason, the replenishment flow or product page is likely failing.
5. **Segment retention comparison is reviewed quarterly.** Monthly is too noisy. Quarterly reveals structural differences.
