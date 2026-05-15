# D2C Funnel Metrics Dictionary  -  Dorje Teas

> Every metric used in the Dorje revenue operating system, defined precisely.
> Formula, data source, weekly use case, decision trigger, and common misread.
> No internal Dorje data used. Formulas and benchmarks are category-standard.

---

## How to Use This Dictionary

Every metric in the weekly dashboard, every number in a founder review, and every experiment result should be interpretable using this file. If a metric appears in any report that is not defined here, add it before using it.

Rule: **no metric without a decision use case**.

---

## Section 1  -  Acquisition Metrics

---

### Sessions

**Definition:** Total visits to the Dorje website (or specific landing page) in a given period.

**Formula:** Counted by analytics platform (GA4 or equivalent). Unique sessions preferred for acquisition analysis.

**Source:** Google Analytics 4 / Shopify Analytics

**Weekly use case:** Baseline for all funnel calculations. Sessions is the denominator for CVR. A sudden session spike or drop is often an analytics issue before it is a business issue  -  check source before reacting.

**Decision trigger:** Sessions drop >20% week-over-week without a corresponding campaign pause or budget reduction → investigate tracking, campaign status, or organic signal.

**Common misread:** Sessions count is meaningless without channel breakout. 10,000 sessions from broad Google Display is not the same as 10,000 sessions from branded search. Always segment by source/medium.

---

### Click-Through Rate (CTR)

**Definition:** Percentage of ad impressions that result in a click to the website.

**Formula:** CTR = Clicks / Impressions × 100

**Source:** Google Ads, Meta Ads Manager

**Weekly use case:** CTR is a creative and audience relevance signal. It tells you whether the ad is resonating enough to earn a click. It does not tell you whether the click converts.

**Decision trigger:** CTR drops >20% week-over-week while spend holds constant → creative fatigue or audience saturation. Action: refresh creative before increasing spend.

**Common misread:** High CTR does not mean good performance. A sensational ad headline can drive high CTR with low purchase intent and low CVR. Always read CTR alongside CVR and CAC.

---

### Cost Per Click (CPC)

**Definition:** Average cost paid per click from an ad.

**Formula:** CPC = Total Spend / Total Clicks

**Source:** Google Ads, Meta Ads Manager

**Weekly use case:** CPC is an input to CAC. High CPC from a high-intent search query (e.g., "buy Darjeeling First Flush online") may be acceptable if CVR is strong. Low CPC from low-intent broad traffic may produce high CAC even with acceptable click volume.

**Decision trigger:** CPC rising week-over-week on a stable campaign → increased auction competition, audience saturation, or Quality Score degradation. Review keyword and audience health.

**Common misread:** CPC alone does not indicate efficiency. ₹25 CPC with 5% CVR produces a lower CAC than ₹10 CPC with 1% CVR.

---

### Cost Per Mille (CPM)

**Definition:** Cost per 1,000 ad impressions.

**Formula:** CPM = (Total Spend / Total Impressions) × 1,000

**Source:** Google Ads, Meta Ads Manager

**Weekly use case:** CPM is primarily relevant for awareness and upper-funnel campaigns. Rising CPM signals increasing competition for the same audience pool.

**Decision trigger:** CPM rising >30% week-over-week on a stable audience → audience saturation or platform auction pressure. Expand audience or test new creative.

**Common misread:** Low CPM in awareness campaigns is not equivalent to efficiency. If awareness traffic does not convert downstream, low CPM only means cheap irrelevant impressions.

---

### Customer Acquisition Cost (CAC)

**Definition:** Total cost to acquire one new paying customer from a specific channel or campaign.

**Formula:** CAC = Total Channel Spend / New Customers Acquired (from that channel, in that period)

**Source:** Ad platform spend data + Shopify new customer order data (requires channel attribution)

**Weekly use case:** CAC is the primary acquisition efficiency metric. It should be tracked by channel, not as a blended average. Blended CAC hides which channel is subsidizing which.

**Decision trigger:** CAC exceeds estimated LTV:3 ratio for 2 consecutive weeks → pause spend scaling, investigate CVR, offer, or audience match.

**Common misread:** CAC calculated as Total Spend / Total Orders (including returning customers) is incorrect. Returning customers should be excluded from the denominator. That metric is CPA, not CAC.

**Dorje-specific note:** CAC for First Flush seasonal campaigns will naturally be different from CAC for always-on Chai campaigns. Do not blend seasonal and always-on CAC into one number  -  they have different LTV and contribution margin profiles.

---

### Cost Per Acquisition (CPA)

**Definition:** Average cost per order, including orders from returning customers.

**Formula:** CPA = Total Spend / Total Orders

**Source:** Ad platform spend + Shopify orders

**Weekly use case:** CPA is useful for understanding overall spend efficiency including retention-driven orders. It should be tracked alongside CAC to understand the blended cost of driving all orders, not just new customer orders.

**Decision trigger:** CPA rising while CAC is stable → returning customer re-acquisition cost is rising, or retention campaigns are under-performing.

**Common misread:** CPA is not interchangeable with CAC. If a brand conflates the two, it will systematically underestimate true acquisition cost.

---

### Return on Ad Spend (ROAS)

**Definition:** Revenue generated per rupee of ad spend.

**Formula:** ROAS = Revenue Attributed to Channel / Channel Spend

**Source:** Ad platform reporting (note: attribution window matters  -  last-click ROAS differs from view-through or data-driven ROAS)

**Weekly use case:** ROAS is the most commonly used acquisition performance metric. It is also the most commonly misused. ROAS above 1.0 does not mean profitable  -  it means revenue exceeded spend, before product cost, packaging, shipping, and discounts.

**Decision trigger:** ROAS drops below a channel-specific floor for 2 consecutive weeks → review creative, audience, landing page, and offer before cutting spend.

**Common misread:** ROAS does not account for variable costs. A 3x ROAS with 30% gross margin and ₹150 average shipping cost per order may have negative contribution margin. Always pair ROAS with Contribution ROAS.

---

### Contribution ROAS

**Definition:** Revenue minus variable costs, per rupee of ad spend.

**Formula:** Contribution ROAS = (Revenue - Product COGS - Packaging - Shipping - Discounts - Gateway Fee) / Channel Spend

**Source:** Shopify order data + ad spend + ops cost inputs

**Weekly use case:** Contribution ROAS is the real efficiency metric. If contribution ROAS is below 1.0, the channel is losing money on every order acquired, regardless of reported ROAS.

**Decision trigger:** Contribution ROAS below 1.0 on any channel → do not scale. Diagnose whether the issue is COGS, shipping, discounting, or spend.

**Common misread:** Contribution ROAS can look worse than ROAS for high-AOV products with expensive packaging (gift boxes) or high-cost logistics (express shipping). This is expected  -  contribution ROAS should be tracked per product category, not only overall.

---

## Section 2  -  Conversion Metrics

---

### Conversion Rate (CVR)

**Definition:** Percentage of sessions that result in a completed purchase.

**Formula:** CVR = Orders / Sessions × 100

**Source:** Shopify + GA4

**Weekly use case:** CVR is the most important mid-funnel metric. It tells you how well the website and offer converts existing traffic before you spend more to acquire more.

**Decision trigger:** CVR drops >15% week-over-week → diagnose by stage (see funnel stage metrics below). Do not increase spend while CVR is declining.

**Common misread:** Overall CVR is a blended number. New visitor CVR is almost always lower than returning visitor CVR. If new customer mix increases (from acquisition campaigns), overall CVR will appear to fall even if nothing on the site changed.

---

### Add-to-Cart Rate

**Definition:** Percentage of product page views that result in adding a product to the cart.

**Formula:** Add-to-Cart Rate = Add-to-Cart Events / Product Page Views × 100

**Source:** GA4 (e-commerce events), Shopify Analytics

**Weekly use case:** Add-to-cart rate is the product page conversion signal. A low rate here means the product page is failing to convince  -  price, trust, clarity, or relevance is the likely issue.

**Decision trigger:** Add-to-cart rate drops while sessions hold → product page problem, not a traffic problem. Investigate page layout, price framing, trust signals, and reviews.

**Common misread:** Add-to-cart rate varies significantly by product. First Flush will have a different rate than Pyramid Teabags. Do not average across products without segmenting first.

---

### Checkout Initiation Rate

**Definition:** Percentage of cart initiations that result in starting the checkout process.

**Formula:** Checkout Rate = Checkout Initiations / Cart Initiations × 100

**Source:** Shopify / GA4

**Weekly use case:** A drop here suggests cart abandonment. Common causes: shipping cost surprise at checkout, payment friction, second-guessing on price, or account creation requirement.

**Decision trigger:** Checkout rate drops while add-to-cart rate holds → investigate checkout friction: is the shipping cost visible before checkout? Is there a guest checkout option? Are there too many steps?

---

### Purchase Completion Rate

**Definition:** Percentage of checkout initiations that result in a completed purchase.

**Formula:** Purchase Rate = Completed Orders / Checkout Initiations × 100

**Source:** Shopify

**Weekly use case:** A high checkout initiation rate but low purchase rate typically signals payment failure, last-minute price resistance, or distraction. This is the narrowest part of the funnel.

**Decision trigger:** Purchase completion rate drops without a corresponding traffic quality change → check payment gateway performance, checkout UX, and any recent price or shipping cost changes.

---

## Section 3  -  Order Economics Metrics

---

### Average Order Value (AOV)

**Definition:** Average revenue per completed order.

**Formula:** AOV = Total Revenue / Total Orders

**Source:** Shopify

**Weekly use case:** AOV is a pricing, bundling, and upsell signal. Rising AOV can mean customers are buying more per order (good) or that lower-AOV products are selling less (need to investigate). Always segment by product and customer type.

**Decision trigger:** AOV drops >10% week-over-week without a product mix explanation → investigate whether a discount campaign is shifting buyers to lower-price products, or whether bundle performance is declining.

**Common misread:** Blended AOV mixes Gift Buyer customers (high AOV, infrequent) with Daily Premium Tea Drinker customers (lower AOV, frequent). These should be tracked separately or gift box orders flagged distinctly.

---

### Discount Rate

**Definition:** Percentage of gross revenue that was discounted.

**Formula:** Discount Rate = Total Discount Amount / Gross Revenue × 100

**Source:** Shopify

**Weekly use case:** Discount rate tells you how much of the revenue is being earned at premium price vs. promotional price. Creeping discount rate is an early warning of margin compression.

**Decision trigger:** Discount rate above 15% on non-gift, non-bundle products → review whether discounting is being used as a sustainable acquisition lever or as a temporary fix for weak CVR.

**Common misread:** Discount rate should be calculated separately for gift bundles (where promotional pricing is intentional) and for daily products (where it should be minimal). A high overall discount rate driven entirely by gift bundles may not indicate a problem.

---

### Refund Rate

**Definition:** Percentage of orders that result in a refund or return.

**Formula:** Refund Rate = Refunded Orders / Total Orders × 100

**Source:** Shopify

**Weekly use case:** Refund rate is a product quality and expectation management signal. For premium whole-leaf tea, a refund typically indicates a delivery problem, product quality disappointment, or a mismatch between the product description and what arrived.

**Decision trigger:** Refund rate spikes above 3% → investigate by product and by channel. Is it a specific SKU, a specific fulfillment batch, or a specific acquisition channel sending mismatched buyers?

---

### Free-Shipping Threshold Completion Rate

**Definition:** Percentage of sessions where the cart reaches or exceeds the free-shipping threshold.

**Formula:** Threshold Completion Rate = Orders at or above free-shipping threshold / Total Orders × 100

**Source:** Shopify

**Weekly use case:** This metric tells you how well the cart is converting AOV nudges. If completion rate is low, the threshold may be set too high, or the add-on products are not compelling enough.

**Decision trigger:** Threshold completion rate declining → review threshold level relative to AOV distribution, and whether add-on products shown in cart are relevant to the buyer's primary product.

---

## Section 4  -  Margin Metrics

---

### Gross Margin

**Definition:** Revenue after direct product costs, before marketing and operating expenses.

**Formula:** Gross Margin = Net Revenue - Product COGS - Packaging Cost - Shipping Cost - Payment Gateway Fee

**Source:** Shopify orders + ops cost inputs [SYNTHETIC in this model]

**Weekly use case:** Gross margin is the ceiling for what can be spent on acquisition. A channel spending above gross margin per customer is structurally unprofitable regardless of revenue.

**Decision trigger:** Gross margin declining while revenue grows → COGS, packaging, or shipping costs are rising faster than revenue. Investigate cost structure before scaling.

---

### Contribution Margin (CM)

**Definition:** Gross margin after deducting paid media spend. The truest measure of D2C unit economics.

**Formula:** CM = Gross Margin - Paid Media Spend (attributed to those orders)

**Source:** Shopify + ad platform spend data

**Weekly use case:** CM is the north star operational metric. If CM is positive, the business can sustain growth. If CM is negative at scale, the business is burning cash on every order acquired.

**Decision trigger:** CM negative on any channel at current spend levels → do not increase spend on that channel. Fix margin or fix spend efficiency first.

**Common misread:** CM should be calculated per order and per channel  -  not just as a total. A positive total CM can hide a channel-level CM problem if a high-margin channel is subsidizing a low-margin one.

---

## Section 5  -  Retention Metrics

---

### Repeat Purchase Rate

**Definition:** Percentage of customers acquired in a given month who make at least one additional purchase within a defined window.

**Formula:** Repeat Purchase Rate = Customers who bought again in Month N+1 or N+2 / Customers acquired in Month N × 100

**Source:** Shopify customer order history

**Weekly use case:** Tracked monthly, by cohort. The most important long-term health signal in the retention layer.

**Decision trigger:** Repeat purchase rate declining for 2+ consecutive cohorts → retention flows are not working, product experience has an issue, or acquisition is pulling in lower-quality buyers.

**Common misread:** Blended repeat rate (all customers, all time) hides cohort-level deterioration. A brand can show a stable blended repeat rate while recent cohorts are worsening, because older loyal cohorts are masking the problem.

---

### Time to Second Purchase

**Definition:** Average number of days between a customer's first and second order.

**Formula:** Median days between Order 1 and Order 2, for customers who have placed at least 2 orders.

**Source:** Shopify order history

**Weekly use case:** Time to second purchase tells you how fast the repeat loop is working. For a 100g Chai pack consumed daily, the expected replenishment window is 21–30 days. If average time to second purchase is 60+ days, the replenishment reminder is not reaching buyers at the right moment.

**Decision trigger:** Time to second purchase lengthening → replenishment reminder is mistimed or missing. Check Day 21 flow trigger.

---

### Subscription Attach Rate

**Definition:** Percentage of buyers who convert to subscription (Tea Club or product-level subscription) within 60 days of their first purchase.

**Formula:** Subscription Attach Rate = Subscribers acquired in period / New customers acquired in same period × 100

**Source:** Shopify subscription app or Tea Club platform

**Weekly use case:** Subscription attach rate is the single most important lever for LTV. Track by SKU and by buyer cohort  -  not just overall.

**Decision trigger:** Subscription attach rate below 5% overall → subscription offer is either too early (push after second purchase), too prominent (triggering resistance), or poorly framed (benefit not clear).

---

### Subscription Renewal Rate

**Definition:** Percentage of subscribers who renew for the next period (monthly or quarterly).

**Formula:** Renewal Rate = Subscribers who renewed / Subscribers due for renewal × 100

**Source:** Shopify subscription app

**Weekly use case:** Renewal rate is more important than subscriber count. A high subscriber count with low renewal rate is a churn problem, not a growth story.

**Decision trigger:** Renewal rate below 70% monthly → diagnose by churn reason: product over-supply, delivery issue, pricing, or disengagement. Pause option before cancel is a structural fix.

---

### Subscription Churn Rate

**Definition:** Percentage of active subscribers who cancel in a given month.

**Formula:** Churn Rate = Subscribers who cancelled / Active subscribers at start of month × 100

**Source:** Shopify subscription app

**Weekly use case:** Complement to renewal rate. Churn above 15% monthly means the subscription is not delivering sustained value.

**Decision trigger:** Churn spiking → run exit survey to identify reason. Is it price, over-supply, delivery, or a product quality issue?

---

## Section 6  -  LTV Metrics

---

### Customer Lifetime Value (LTV)

**Definition:** Total estimated revenue (or margin) from a customer over a defined time period, typically 12 months.

**Formula (simplified):** LTV = AOV × Purchase Frequency × Retention Rate (12-month)

**Source:** Shopify cohort data

**Weekly use case:** LTV is a planning metric, not a weekly operating metric. Use it monthly to evaluate whether acquisition cost is justified and to prioritize which segments to invest in.

**Decision trigger:** 12-month LTV:CAC below 2x → acquisition is either too expensive or retention is too weak. Identify which before choosing the fix.

---

### LTV:CAC Ratio

**Definition:** Ratio of 12-month LTV to customer acquisition cost. Measures whether the cost to acquire a customer is justified by the revenue they generate.

**Formula:** LTV:CAC = 12-month LTV / CAC

**Source:** Shopify cohort LTV + channel CAC

**Weekly use case:** The primary channel investment decision metric. Allocate more budget to channels with LTV:CAC > 2x. Investigate channels below 1.5x before scaling.

**Decision trigger:** LTV:CAC below 1.5x → acquisition is not recovering cost within 12 months. Pause scaling, improve retention, or reduce CAC.

**Common misread:** LTV:CAC ratios improve over time as cohorts age. A 6-month LTV:CAC of 1.2x may become 2.5x at 18 months if retention is strong. Do not kill a channel based on early cohort LTV alone  -  but do not scale it aggressively either.

---

### Payback Period

**Definition:** Number of months required to recover CAC from contribution-margin-positive orders.

**Formula:** Payback Period = CAC / (Monthly CM per customer)

**Source:** Channel CAC + contribution margin per order

**Weekly use case:** Payback period tells you how long the business is cash-flow-negative per customer acquired. Shorter payback = more capital-efficient growth.

**Decision trigger:** Payback period above 6 months for a scaling channel → the business needs capital to fund the gap between acquisition cost and revenue recovery. This is a cash flow risk, not just a unit economics issue.

---

## Metric Glossary Quick Reference

| Metric | Formula | Source | Frequency |
|---|---|---|---|
| Sessions | Counted | GA4 | Weekly |
| CTR | Clicks / Impressions | Ad platform | Weekly |
| CPC | Spend / Clicks | Ad platform | Weekly |
| CPM | (Spend / Impressions) × 1,000 | Ad platform | Weekly |
| CAC | Channel Spend / New Customers | Ads + Shopify | Weekly |
| CPA | Total Spend / Total Orders | Ads + Shopify | Weekly |
| ROAS | Revenue / Spend | Ad platform | Weekly |
| Contribution ROAS | (Revenue - Variable Costs) / Spend | Ads + Shopify + Ops | Weekly |
| CVR | Orders / Sessions | Shopify + GA4 | Weekly |
| Add-to-Cart Rate | ATC Events / Product Views | GA4 | Weekly |
| Checkout Rate | Checkouts / Cart Initiations | Shopify | Weekly |
| AOV | Revenue / Orders | Shopify | Weekly |
| Discount Rate | Discounts / Gross Revenue | Shopify | Weekly |
| Refund Rate | Refunds / Orders | Shopify | Weekly |
| Gross Margin | Revenue - COGS - Packaging - Shipping - Fees | Shopify + Ops | Weekly |
| Contribution Margin | Gross Margin - Paid Media | Shopify + Ads + Ops | Weekly |
| Repeat Purchase Rate | Repeat Buyers / Original Cohort | Shopify | Monthly |
| Time to 2nd Purchase | Median days between Order 1 and 2 | Shopify | Monthly |
| Subscription Attach Rate | New Subscribers / New Customers | Subscription app | Monthly |
| Renewal Rate | Renewals / Due for Renewal | Subscription app | Monthly |
| Churn Rate | Cancellations / Active Subscribers | Subscription app | Monthly |
| LTV (12-month) | AOV × Frequency × Retention | Shopify cohort | Monthly |
| LTV:CAC | LTV / CAC | Shopify + Ads | Monthly |
| Payback Period | CAC / Monthly CM per customer | Shopify + Ads + Ops | Monthly |
