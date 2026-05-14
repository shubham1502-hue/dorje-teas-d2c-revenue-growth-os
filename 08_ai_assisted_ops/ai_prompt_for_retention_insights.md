# AI Prompts for Retention Insights - Dorje Teas D2C Revenue Growth OS

> These prompts support lifecycle diagnosis using pasted cohort, order, and subscription data only.

## Prompt 1: Cohort Diagnosis

**Required inputs:** Cohort month, new customers, M0-M6 retention, M0 revenue, cumulative LTV, CAC, LTV:CAC, acquisition source, primary product if available.

```text
Diagnose Dorje Teas cohort quality using the cohort table below.

Input:
[PASTE DATA HERE]

Analysis instructions:
1. Identify cohorts with strong M1 and M3 retention.
2. Separate First Flush Darjeeling seasonal cohorts from gifting cohorts.
3. Explain whether high M0 revenue is likely durable or gift-driven.
4. Connect LTV:CAC to acquisition scale decisions.

Output format:
1. Best cohort
2. Weakest cohort
3. Repeat purchase diagnosis
4. Acquisition implication
5. Lifecycle action

Decision implication:
State whether to Scale, Hold, Fix, or Pause acquisition into similar cohorts.

What real data would improve the diagnosis:
List the exact fields needed, such as SKU-level order history, channel attribution, and margin by order.
```

## Prompt 2: Subscription Health Check

**Required inputs:** Active subscribers, new subscribers, renewal rate, churn rate, pause rate, subscription revenue, subscription CM%, churn reasons, product split.

```text
Review Dorje Teas subscription health using the pasted data.

Input:
[PASTE DATA HERE]

Analysis instructions:
1. Evaluate whether subscription growth is healthy or churn-driven.
2. Compare subscription contribution margin to one-time order margin.
3. Diagnose churn reason mix: over-supply, product fatigue, price, delivery, forgot, wrong cadence.
4. Recommend lifecycle fixes.

Output format:
1. Subscription health read
2. Main churn risk
3. Margin read
4. Flow fixes
5. Founder decision needed, if any

Decision implication:
Say whether to Scale subscription acquisition, Fix onboarding, Fix cadence, or Pause subscription push.

What real data would improve the diagnosis:
Name the subscription app exports and Shopify order fields needed.
```

## Prompt 3: Lifecycle Experiment Prioritization

**Required inputs:** Segment list, product purchased, time since purchase, repeat rate, flow performance, CM per retained order, experiment backlog.

```text
Prioritize Dorje Teas lifecycle experiments for the next two weeks.

Input:
[PASTE DATA HERE]

Analysis instructions:
1. Rank experiments by expected repeat purchase impact and contribution margin.
2. Prioritize Original Darjeeling Chai replenishment, First Flush Darjeeling handoff, Gift Buyer self-purchase, and Tea Club timing when relevant.
3. Identify experiments that should not run simultaneously because they contaminate measurement.

Output format:
| Priority | Experiment | Segment | Why Now | Primary Metric | Decision Rule |

Decision implication:
Recommend the top three experiments to run, the ones to defer, and the one to kill if bandwidth is constrained.

What real data would improve the diagnosis:
List missing flow send, open, click, order, and contribution margin fields.
```
