# Data Dictionary  -  Dorje Teas Revenue OS

> Defines every field used across the four synthetic data tables.
> Every field has: definition, formula or source, example value, business use case.
> Fields marked [SYNTHETIC] would be replaced with real internal data on Day 1.
> No internal Dorje data used anywhere in this dataset.

---

## Rule

**No metric enters a dashboard or analysis without being defined here first.**

If a field appears in a report that is not in this dictionary, add it before using it.
If a field is in this dictionary but has never produced a decision, question whether it belongs.

---

## Section 1  -  Order-Level Fields (sample_orders.csv)

---

**order_id**
Definition: Unique identifier for each order transaction.
Source: Shopify order number.
Example: `ORD-2024-0142`
Business use: Primary key for joining order data to customer and campaign tables.

---

**order_date**
Definition: Date the order was placed and confirmed by Shopify.
Source: Shopify.
Format: DD/MM/YYYY
Business use: Used for weekly and monthly revenue aggregation, cohort assignment, and seasonal analysis.

---

**week / month**
Definition: ISO week string and YYYY-MM string derived from order_date.
Source: Derived.
Example week: `2025-W14` | Example month: `2025-04`
Business use: Week is the primary grouping unit for the founder dashboard. Month is the primary grouping unit for cohort analysis.

---

**customer_id**
Definition: Unique identifier for the customer who placed the order.
Source: Shopify customer record.
Example: `CUST-0087`
Business use: Links multiple orders to the same customer for repeat purchase rate, LTV, and cohort analysis. A customer_id appearing in more than one order_date = a returning customer.

---

**customer_type**
Definition: Whether the customer was placing their first-ever order ("new") or had ordered before ("returning").
Source: Derived from Shopify customer order count at time of purchase.
Values: `new` | `returning`
Business use: Splits revenue into new customer revenue and returning customer revenue  -  the primary indicator of retention health. Never blend these in a weekly revenue review without showing the split.

---

**product_id**
Definition: Stock-keeping unit (SKU) identifier for the product ordered.
Source: Shopify product variant ID.
Example: `SKU-005`
Business use: Links orders to the product catalog for COGS, packaging cost, margin, and replenishment cycle lookups.

---

**product_category**
Definition: The commercial category of the product ordered, mapped to Dorje's product ladder.
Source: Shopify product tag or metafield.
Values: `First Flush` | `Second Flush` | `Chai` | `Green Tea` | `Pyramid Teabags` | `Cold Brew` | `Gift Box` | `Subscription`
Business use: Revenue and margin analysis by product ladder rung. Critical for identifying category mix shifts and seasonal patterns.

---

**gross_revenue**
Definition: The listed price of the product before any discounts are applied.
Source: Shopify line item price.
Example: ₹750
Business use: Starting point for the contribution margin waterfall. Gross revenue is never the right number to use for profitability analysis  -  always use net_revenue.

---

**discount_amount**
Definition: The rupee value of any discount applied to this order.
Source: Shopify discount record.
Example: ₹75 (10% welcome discount on ₹750 order)
Business use: Used to calculate net_revenue and discount rate. Rising discount_amount without a planned campaign is a flag for premium positioning risk.

---

**discount_code**
Definition: The discount code applied to the order, or "none" if no discount.
Source: Shopify discount code field.
Example: `WELCOME10` | `DIWALI15` | `REPLEN10` | `none`
Business use: Audit which codes are driving discounted revenue. Codes in circulation beyond their campaign window are a margin leak.

---

**net_revenue**
Definition: Revenue after discounts. The correct revenue figure for all profitability calculations.
Formula: `gross_revenue − discount_amount`
Example: ₹675 (₹750 − ₹75)
Business use: Denominator for gross margin %, CM%, and all per-order economics.

---

**shipping_charged**
Definition: Shipping fee paid by the customer. Zero if order is above the free-shipping threshold.
Source: Shopify shipping line.
Example: ₹99 (below threshold) | ₹0 (above threshold)
Business use: AOV and threshold analysis. If most orders are just below the threshold, a threshold adjustment could improve both AOV and CM.

---

**cogs** [SYNTHETIC]
Definition: Product cost of goods sold  -  the cost of producing or sourcing the tea in this order.
Source: [SYNTHETIC]  -  would come from finance/ops COGS records in real implementation.
Example: ₹180 for First Flush 100g
Business use: Primary input to gross margin calculation. COGS change on any SKU should trigger a margin review.

---

**packaging_cost** [SYNTHETIC]
Definition: Cost of packaging materials for this order  -  box, inner foil, label, and for gift orders, gift box and ribbon.
Source: [SYNTHETIC]  -  would come from procurement records.
Example: ₹55 (standard) | ₹130 (premium gift box)
Business use: Often underestimated in D2C premium brands. Gift box packaging cost can be 2–3× standard and must be covered by gift box AOV premium.

---

**shipping_cost** [SYNTHETIC]
Definition: The actual shipping cost Dorje pays to the logistics provider for this order, regardless of what the customer paid.
Source: [SYNTHETIC]  -  would come from logistics provider rate card.
Example: ₹90 (metro) | ₹130 (Tier 2/3 city)
Business use: Real cost of fulfillment. The gap between shipping_charged (what customer paid) and shipping_cost (what Dorje paid) is a direct CM impact. For orders above the free-shipping threshold, Dorje absorbs the full shipping cost.

---

**gateway_fee**
Definition: Payment processing fee charged by the payment gateway (UPI, card, net banking).
Formula: `net_revenue × 0.02` (2% blended rate)
Example: ₹13.50 on a ₹675 net order
Business use: A small but consistent cost that compounds at volume. If gateway rates change, this field updates automatically via the OPS_Assumptions tab.

---

**gross_margin**
Definition: Revenue remaining after all direct product costs  -  COGS, packaging, shipping, and gateway fee  -  but before paid media spend.
Formula: `net_revenue − cogs − packaging_cost − shipping_cost − gateway_fee`
Example: ₹326.50 on a ₹675 net First Flush order
Business use: The starting point for contribution margin. Gross margin tells you the product economics before any acquisition cost is applied.

---

**gross_margin_pct**
Definition: Gross margin expressed as a percentage of net revenue.
Formula: `gross_margin ÷ net_revenue × 100`
Example: 48.4%
Business use: Useful for comparing margin health across products. A product with <30% gross margin has very little room for paid acquisition before becoming CM-negative.

---

**attributed_ad_spend** [SYNTHETIC]
Definition: Estimated paid media cost attributed to this specific order, based on the channel that drove the session.
Source: [SYNTHETIC]  -  in real implementation, would come from last-click attribution or modeled attribution from Google Ads / Meta Ads Manager.
Example: ₹280 for a Google Search order | ₹8 for an email-attributed order | ₹0 for organic
Business use: The key variable that converts gross margin into contribution margin. If attributed_ad_spend exceeds gross_margin, the order is CM-negative regardless of ROAS.

---

**contribution_margin**
Definition: Revenue remaining after all variable costs including paid media. The truest measure of per-order profitability.
Formula: `gross_margin − attributed_ad_spend`
Example: ₹46.50 (positive but thin for a paid acquisition order)
Business use: The north star metric at the order level. A channel or campaign producing negative CM orders is losing money even if ROAS appears acceptable. Always check CM before scaling any paid channel.

---

**cm_pct**
Definition: Contribution margin as a percentage of net revenue.
Formula: `contribution_margin ÷ net_revenue × 100`
Example: 6.9%
Business use: Normalizes CM for comparison across products and channels. Target: >20% blended CM% for sustainable D2C operations. <10% is a warning; negative is an immediate flag.

---

**channel**
Definition: The last-click marketing channel that brought the customer to the Dorje website for this order.
Source: GA4 source/medium attribution, mapped to Shopify order.
Values: `google_search` | `meta` | `email` | `organic` | `direct`
Business use: Channel-level revenue, CAC, ROAS, and CM analysis. The most important field for acquisition efficiency diagnosis.

---

**campaign_id**
Definition: The specific campaign within the channel that drove this order.
Source: UTM campaign parameter from GA4, linked to Shopify order.
Example: `CMP-GS-002` (Google Search  -  First Flush Seasonal)
Business use: Campaign-level performance drill-down within a channel. When a channel's metrics shift, campaign_id tells you which specific campaign is driving the change.

---

**is_subscription**
Definition: Whether this order was placed as part of a Tea Club or product-level subscription, rather than a one-time purchase.
Source: Shopify subscription app tag on order.
Values: `TRUE` | `FALSE`
Business use: Separates subscription economics from one-time purchase economics. Subscription orders should have lower attributed_ad_spend and higher CM% than one-time orders.

---

**is_gift**
Definition: Whether this order contains a gift box SKU.
Source: Derived from product_id (Gift Box SKUs = SKU-009, SKU-010).
Values: `TRUE` | `FALSE`
Business use: Separate Gift Buyer lifecycle from Daily Premium Tea Drinker lifecycle. Gift orders have different post-purchase flows, different margin profiles, and different repeat purchase behavior.

---

## Section 2  -  Campaign-Level Fields (sample_ad_spend.csv)

---

**spend**
Definition: Total money paid to the ad platform (Google Ads or Meta) for this campaign in this week.
Source: [SYNTHETIC]  -  would come from platform billing export.
Example: ₹3,200 (weekly Google Search brand campaign spend)
Business use: The denominator for ROAS and CAC. All efficiency metrics start here.

---

**ctr_pct (Click-Through Rate)**
Definition: Percentage of ad impressions that resulted in a click.
Formula: `clicks ÷ impressions × 100`
Example: 4.8%
Business use: Creative and audience relevance signal. CTR dropping without CVR dropping = creative fatigue. CTR high but CVR low = wrong audience or wrong landing page.

---

**cpc (Cost Per Click)**
Definition: Average cost paid per click on the ad.
Formula: `spend ÷ clicks`
Example: ₹28.50
Business use: Input to CAC. High CPC from high-intent queries (Darjeeling First Flush) can be acceptable if CVR is strong. Always read CPC alongside CVR, not in isolation.

---

**cpm (Cost Per Mille)** [SYNTHETIC / DERIVED]
Definition: Average cost paid per 1,000 ad impressions.
Formula: `spend ÷ impressions × 1,000`
Example: ₹240.00
Business use: Auction-cost and audience-saturation signal. CPM is synthetic in this dataset and would be replaced by ad platform reporting in a live implementation.

---

**cvr_pct (Session-to-Purchase Conversion Rate)**
Definition: Percentage of campaign sessions that resulted in a completed purchase.
Formula: `orders ÷ sessions × 100`
Example: 2.1%
Business use: The most important funnel metric at the campaign level. CVR dropping = landing page, offer, or product-page problem. Never increase spend on a campaign with declining CVR.

---

**revenue** [SYNTHETIC / DERIVED]
Definition: Campaign-attributed revenue generated during the week.
Formula: `orders × modeled average order value`
Example: ₹8,400
Business use: Numerator for ROAS and contribution_roas. In the synthetic data it is modeled; in live use it should be reconciled against Shopify and ad platform attribution.

---

**cac (Customer Acquisition Cost)**
Definition: Average cost to acquire one new paying customer from this campaign.
Formula: `spend ÷ new_customers`
Example: ₹520
Business use: The primary acquisition efficiency metric. Must be compared against break-even CAC (gross margin per first order) and tracked against LTV:CAC. ROAS without CAC is incomplete.

---

**roas (Return on Ad Spend)**
Definition: Revenue generated per rupee of ad spend.
Formula: `revenue ÷ spend`
Example: 2.8x
Business use: Common campaign efficiency metric. Misleading in isolation for premium D2C  -  does not account for COGS, packaging, or shipping. Always pair with contribution_roas.

---

**contribution_roas**
Definition: Contribution margin generated per rupee of ad spend. Accounts for variable costs beyond just the ad spend.
Formula: `(revenue − estimated variable costs) ÷ spend`
Example: 1.4x
Business use: The honest ROAS. A campaign with 3x ROAS but 0.8x contribution ROAS is losing money on every order. Scale only campaigns with contribution_roas above 1.0.

---

## Section 3  -  Cohort Fields (sample_customer_cohorts.csv)

---

**cohort_month**
Definition: The month in which the customers in this cohort made their first purchase.
Format: YYYY-MM
Example: `2025-04`
Business use: Groups customers by acquisition month for retention curve analysis. Allows comparison of how different cohorts behave over time  -  the core of LTV analysis.

---

**m0_revenue / m0_avg_order_value**
Definition: Total revenue and average order value from the cohort's first purchase month.
Source: [SYNTHETIC]
Business use: Baseline for the cohort. Higher M0 AOV does not always mean better cohort quality  -  festive Gift Buyer cohorts often have high M0 AOV but low repeat rates.

---

**m1_retained / m1_retention_rate_pct / m1_revenue**
Definition: Number of M0 customers who made at least one purchase in Month 1 after their first purchase, and the revenue they generated.
Source: [SYNTHETIC]
Business use: The most important single retention metric. M1 retention rate tells you how many first-time buyers came back in the following month. A premium tea brand should target >20% M1 retention for daily-consumption products.

---

**m2 through m6 (retained / retention_rate_pct / revenue)**
Definition: Same structure as m1, extended through Month 6 after first purchase.
Source: [SYNTHETIC]
Business use: Builds the full retention curve. Flat retention from M3 onward suggests a loyal core segment has been identified. Declining retention all the way to M6 suggests no real loyalty is forming.

---

**subscription_attach_m2_pct**
Definition: Percentage of M2 returning customers who converted to a Tea Club or product-level subscription.
Source: [SYNTHETIC]
Business use: Key signal of subscription health. Subscription attach should be measured after the second purchase, not after the first. Target: >10% of M2 returning customers converting to subscription.

---

**cumulative_ltv_m6**
Definition: Total revenue per customer from M0 through M6, averaged across the cohort.
Formula: `(m0_rev + m1_rev + ... + m6_rev) ÷ new_customers`
Example: ₹1,104
Business use: The LTV input for LTV:CAC calculation. A 6-month LTV of ₹1,100 with a CAC of ₹480 = LTV:CAC of 2.3x  -  above the minimum 2.0x threshold for sustainable growth.

---

**ltv_cac_ratio_m6**
Definition: Cumulative 6-month LTV divided by the cohort's average CAC.
Formula: `cumulative_ltv_m6 ÷ cac_cohort`
Example: 2.3x
Business use: The single most important metric for evaluating acquisition channel health over time. Below 1.5x = losing money. 1.5–2.0x = marginal. Above 2.0x = sustainable. Above 3.0x = scale with confidence.

---

## Section 4  -  Product Catalog Financial Fields (sample_product_catalog.csv)

---

**price** [SYNTHETIC]
Definition: Public-facing SKU price used in the model.
Source: [SYNTHETIC]  -  modeled from public catalog observations and category price bands.
Business use: Input to product ladder, AOV, and gross margin estimates.

---

**cogs / packaging_cost / shipping_cost_blended** [SYNTHETIC]
Definition: Estimated SKU-level variable costs used for catalog economics.
Source: [SYNTHETIC]  -  would come from finance, procurement, and logistics records in a live implementation.
Business use: Inputs to gross_margin_est and break-even CAC estimates.

---

**gateway_fee_est** [SYNTHETIC / DERIVED]
Definition: Estimated payment gateway fee for the SKU.
Formula: `price × 0.02`
Business use: Keeps product-level margin estimates consistent with the order-level gateway fee assumption.

---

**gross_margin_est / gross_margin_pct** [SYNTHETIC / DERIVED]
Definition: Estimated product gross margin before paid media.
Formula: `(price − cogs − packaging_cost − shipping_cost_blended − gateway_fee_est)` and that value divided by `price`.
Business use: Identifies which SKUs can support paid acquisition, discounting, and bundling.

---

**price_per_cup_est** [SYNTHETIC / DERIVED]
Definition: Estimated per-cup price using an assumed serving size.
Formula: `price ÷ estimated cups per pack`
Business use: Supports price-per-cup framing in acquisition and landing page tests.
