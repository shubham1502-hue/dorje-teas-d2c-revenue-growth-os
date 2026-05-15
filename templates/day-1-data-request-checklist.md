# Day 1 Data Request Checklist

Use this checklist before replacing the public-safe sample structure with authorized company exports.

The goal is not perfect data on day one. The goal is enough clean data to run one credible founder revenue review without pretending sample assumptions are actual performance.

## Revenue Data Needed

- order ID
- order date
- order status
- gross revenue
- discount amount
- net revenue
- taxes, if relevant to reporting
- shipping charged to customer
- refund amount
- currency
- sales channel

## Customer Data Needed

- anonymized customer ID
- first order date
- new or returning customer flag
- customer city or region
- customer segment, if available
- email or phone opt-in status, if needed for lifecycle analysis
- acquisition source, if available

Do not request personal data unless it is required for the operating review. Use anonymized IDs wherever possible.

## Product And SKU Data Needed

- SKU
- product name
- product category
- product price
- product size or pack type
- COGS by SKU
- packaging type
- active or discontinued status
- subscription eligibility
- gift eligibility

## Channel Data Needed

- source or medium
- channel grouping
- campaign name
- campaign ID
- landing page, if available
- sessions
- add-to-cart events
- checkout starts
- purchases
- revenue by channel

## Campaign Data Needed

- platform
- campaign ID
- campaign name
- spend
- impressions
- clicks
- CPC
- CTR
- conversions
- attributed revenue
- campaign objective
- start and end date
- status

## Retention And Subscription Data Needed

- customer ID
- first order date
- second order date
- repeat order count
- repeat revenue
- subscription start date
- subscription plan
- renewal status
- cancellation date
- churn reason, if available
- winback or lifecycle flow exposure, if available

## Margin And Cost Data Needed

- COGS by SKU
- packaging cost by SKU or order type
- shipping cost by order
- payment gateway fee rate
- discount amount by order
- refund rate
- paid media spend by campaign
- fulfillment or replacement cost, if material

## Data Quality Checks

Before using the data in a founder memo, check:

- Do order totals reconcile with the ecommerce platform?
- Are canceled and refunded orders handled consistently?
- Are dates in one timezone?
- Are duplicate orders removed?
- Are gift orders identified?
- Are subscription orders separated from one-time orders?
- Are discounts split from gross revenue?
- Is shipping charged to the customer separated from shipping cost paid by the company?
- Are campaign IDs consistent across spend and order data?
- Are synthetic, sample, public, and actual fields clearly labeled?

## What To Do If Data Is Missing

| Missing data | Practical fallback | Credibility note |
|---|---|---|
| COGS by SKU | Use a clearly labeled temporary COGS assumption by category | Do not present margin as final |
| Campaign attribution | Use channel-level reporting first | Do not make campaign-level scale decisions |
| Customer ID | Review revenue and product mix only | Do not claim repeat purchase behavior |
| Subscription renewal data | Track active subscription count and known cancellations | Do not infer churn quality |
| Shipping cost | Use a labeled average shipping cost assumption | Flag margin as provisional |
| Product-level funnel data | Start with overall funnel stages | Do not diagnose product-page issues too precisely |

If a metric cannot support a decision, leave it out of the founder review and list the missing data as a blocker.
