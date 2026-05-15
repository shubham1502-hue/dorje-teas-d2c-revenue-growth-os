# Decision Rules  -  Dorje Teas

> Converts metric movements into operator decisions.
> These are diagnostic frameworks, not algorithms. Every rule requires judgment before action.
> Specific to a premium Darjeeling D2C brand  -  not generic D2C advice.
> No internal Dorje data used.

---

## How to Use This File

A dashboard full of metrics is not useful unless it tells you what to do next. This file converts metric patterns into decision logic.

**Structure of each rule:**
1. The metric pattern (what you observe)
2. The diagnosis (what it likely means)
3. The question to ask before acting
4. The action options (scale / fix / pause / investigate)
5. What not to do

---

## Section 1  -  Acquisition and Campaign Decision Rules

---

### Rule A1  -  CTR Declining, CVR Stable

**What you observe:** CTR drops >15% week-over-week. CVR on the landing page holds steady. Sessions decline.

**Diagnosis:** The problem is likely in the ad creative or the audience  -  not the landing page or offer. Clicks that do arrive are converting at the same rate, which means the funnel is intact. Fewer people are engaging with the ad itself.

**Question before acting:** Is the audience new and less relevant, or has the existing audience seen this creative too many times?

**Action options:**
- If the audience is unchanged: creative fatigue. Refresh the creative with a new angle  -  estate story, First Flush harvest, price-per-cup framing, or social proof.
- If a new audience was recently added: audience-message mismatch. Review whether the new audience is the right fit for this creative.

**Do not:** Pause the campaign before testing a new creative. A campaign with strong CVR but weak CTR is fixable with creative. Pausing it loses the conversion infrastructure that is working.

---

### Rule A2  -  CTR Stable, CVR Declining

**What you observe:** CTR holds or improves. Sessions are healthy. But purchase conversion rate drops.

**Diagnosis:** The problem is on the landing page or in the offer  -  not the ad. People are clicking with intent but not buying. This is a trust, price, clarity, or offer friction problem.

**Question before acting:** Did anything change on the product page, offer, price, or shipping terms this week?

**Action options:**
- Review the landing page for trust signals: are reviews visible? Is the origin story clear? Is the price-per-cup framing present?
- Check if the offer changed: was a discount removed? Was free shipping threshold raised?
- Check if the landing page-ad message match broke: is a First Flush ad landing on a generic shop page?
- Run a Hotjar or session recording to see where users drop.

**Do not:** Increase spend on a campaign with declining CVR. You will acquire more sessions at the same conversion problem and increase CAC.

---

### Rule A3  -  ROAS Positive, Contribution Margin Negative

**What you observe:** ROAS appears healthy (e.g., 3x). But contribution margin calculation shows the channel is losing money after variable costs.

**Diagnosis:** ROAS does not account for COGS, packaging, shipping, and gateway fees. For a premium D2C tea brand shipping from Darjeeling, variable costs beyond product cost can consume 30–50% of revenue. A 3x ROAS on a product with 35% gross margin and high shipping cost may be contribution-margin-negative.

**Question before acting:** What is the actual CM% on orders from this channel? Which cost component is the biggest leak?

**Action options:**
- If COGS and packaging are the issue: review product pricing or bundle structure.
- If shipping cost is the issue: review free-shipping threshold  -  is it set too low? Is a specific region driving high shipping cost?
- If discounting is the issue: channel may be over-reliant on discount codes.
- If the math is marginal: hold spend at current level and fix the variable cost structure before scaling.

**Do not:** Scale spend on a ROAS-positive, CM-negative channel. Scaling accelerates the loss.

---

### Rule A4  -  CAC Exceeds Break-Even CAC

**What you observe:** CAC on a channel exceeds the gross margin per first order (the break-even CAC). The first purchase is not profitable.

**Diagnosis:** This is acceptable only if the LTV:CAC ratio is strong (>2x) and the repeat purchase data supports that assumption. For a premium tea brand with natural replenishment behavior, a first-order loss can be recovered on the second and third orders  -  but only if the repeat purchase rate is high enough and fast enough.

**Question before acting:** What is the repeat purchase rate for customers acquired from this channel? How many orders does it take to recover the CAC?

**Action options:**
- If repeat rate is strong (>30% at Day 60): hold CAC at current level, accept first-order economics, and build retention to recover faster.
- If repeat rate is weak (<15% at Day 60): the channel is producing one-time buyers, not compounding customers. Reduce spend or fix the retention experience for that channel's buyer profile.
- If repeat data is not yet available (channel is new): hold spend while retention data accumulates. Do not scale blind.

**Do not:** Use LTV as a rationalization for high CAC without actual cohort data to support the LTV estimate.

---

### Rule A5  -  One Channel Has Significantly Better Contribution ROAS Than Others

**What you observe:** One channel (e.g., Google Search branded + Darjeeling-specific terms) shows contribution ROAS of 2.5x. Other channels show contribution ROAS of 0.8–1.2x.

**Diagnosis:** The high-performing channel has better audience intent, better conversion, or better product-message fit. The underperforming channels are subsidizing the efficient channel in blended metrics.

**Question before acting:** Is the high-performing channel capacity-constrained (limited search volume, small audience)? Can it be scaled, or will scaling it increase CPC without proportional revenue?

**Action options:**
- Scale the high-performing channel until CPC or CVR signals diminishing returns.
- Pause or reduce spend on channels with contribution ROAS below 1.0.
- Redirect budget from underperforming channels to the efficient channel.
- Do not average the channels together and call the blended result acceptable.

**Do not:** Keep underperforming channels running at the same spend level because of sunk cost or channel diversity preference. Channel diversity is only valuable if each channel is contribution-margin-positive.

---

## Section 2  -  Conversion Decision Rules

---

### Rule C1  -  Add-to-Cart Rate Below Expected for High-Traffic Product Page

**What you observe:** A product page (e.g., First Flush, Chai) is receiving significant sessions but add-to-cart rate is below 4%.

**Diagnosis:** The product page is not convincing enough at the trust or value layer to trigger a cart action. For a premium Darjeeling tea brand, the most common causes are: price sticker shock without value framing, insufficient origin or product story, or unclear differentiation from cheaper alternatives.

**Question before acting:** What is the first thing a visitor sees on this page? Does it answer the question "why should I pay this price for this specific tea"?

**Action options:**
- Add price-per-cup framing near the price: "that is approximately ₹X per cup of exceptional Darjeeling."
- Move estate proof higher: Selim Hill, 1871, organic certification, direct from garden.
- Add a reviews module above the fold.
- Test a product-specific tasting note (muscatel, floral, fresh-mown hay) near the product description.
- Check if the page has a brewing guide  -  it reduces purchase anxiety for first-time buyers.

**Do not:** Discount the product to increase add-to-cart rate. This solves the symptom and destroys the premium positioning.

---

### Rule C2  -  High Add-to-Cart, Low Checkout Completion

**What you observe:** Add-to-cart rate is healthy (>5%), but checkout initiation-to-purchase rate is low (<50%).

**Diagnosis:** The visitor wanted the product but something at the checkout stage created friction or second-guessing. Common causes: unexpected shipping cost, limited payment options, delivery timeline concern, or price remorse at the payment screen.

**Question before acting:** At what point in checkout are most abandonments happening  -  shipping entry, payment page, or review page?

**Action options:**
- If shipping cost reveal is the friction: review the free-shipping threshold and whether it is communicated clearly before checkout.
- If payment options are limited: check that UPI, net banking, and COD (if applicable) are available.
- If delivery timeline is the concern: make the freshness and direct-from-Darjeeling delivery promise visible at checkout, not just on product pages.
- Run an abandoned cart recovery flow (email or WhatsApp within 1 hour of abandonment).

**Do not:** Assume all cart abandonment is price-related. A user who added a ₹800 item to the cart has already accepted the price  -  friction at checkout is usually process, not pricing.

---

### Rule C3  -  Conversion Rate Different Across Product Categories

**What you observe:** First Flush CVR is 2.8%. Chai CVR is 4.5%. Gift box CVR is 1.2%.

**Diagnosis:** Different products attract different buyer intent and require different conversion support. This is not a problem  -  it is expected. The question is whether each product is optimized for its own buyer, not whether all products have the same CVR.

**Question before acting:** Is each product's conversion rate appropriate for its segment? Is the gift box CVR low because the landing page is wrong for the Gift Buyer, or because gift buying is inherently lower-CVR (they want to explore before committing)?

**Action options:**
- Do not average CVR across products and make blanket decisions.
- Build segment-specific landing pages if campaign traffic for different products is going to a single page.
- For gift boxes: test a dedicated gift box landing page with packaging visual, estate story, and occasion framing.
- For First Flush: test a harvest-specific page with picking date, tasting notes, and batch framing.

**Do not:** Benchmark Chai CVR against gift box CVR and call one a failure.

---

## Section 3  -  Retention Decision Rules

---

### Rule R1  -  Repeat Purchase Rate Flat After First Purchase Cohort

**What you observe:** Month 1 cohort (customers who bought in Month 1) is not returning in Month 2 at an expected rate. Repeat purchase rate is below 20% at Day 60.

**Diagnosis:** Either the product did not deliver on expectations, the post-purchase experience did not reinforce the relationship, or the category's natural replenishment cycle is longer than assumed (more likely for premium whole-leaf tea than commodity tea bags).

**Question before acting:** Did the Day 7 brewing education and Day 21 replenishment reminder go out to this cohort? If not, the problem may be a flow failure, not a product or brand problem.

**Action options:**
- Audit the post-purchase email/WhatsApp flows: did they fire? Did they land in inbox?
- Check the replenishment cycle assumption: for 100g at 1–2 cups per day, the pack lasts 40–50 days. The Day 21 reminder may be too early for some SKUs.
- Segment the cohort by product purchased: Chai buyers should return faster than First Flush buyers (higher frequency vs. seasonal).
- Run a direct "how was your first order?" survey email  -  qualitative signal before scaling fix.

**Do not:** Assume low repeat rate means the product has a problem before ruling out flow failures or cycle timing.

---

### Rule R2  -  Subscription Churn Spike

**What you observe:** Subscription churn rate exceeds 15% in a given month, or a sudden spike appears from a previously stable base.

**Diagnosis:** Churn spikes usually have a specific cause rather than a broad one. Common causes for a premium tea subscription: over-supply (the customer has more tea than they can drink on the delivery frequency), product fatigue (same SKU every month), delivery problem, or the subscriber simply forgot they signed up.

**Question before acting:** What does the cancel-flow survey data say? What is the top reason for cancellation this month?

**Action options:**
- If over-supply: offer a pause option prominently before cancellation. Allow frequency adjustment (monthly → quarterly).
- If product fatigue: offer a rotation  -  subscriber gets a different SKU each cycle, curated by the estate.
- If delivery problem: cross-reference with logistics data and address fulfillment issue.
- If "forgot I subscribed": improve subscription confirmation and pre-renewal nudge copy.

**Do not:** Treat all churn as a pricing or discount problem. Offering a discount to a subscriber who is over-supplied just delays the churn and trains subscribers to cancel to get a deal.

---

### Rule R3  -  Gift Buyer Has Zero Repeat Purchase Signal at Day 45

**What you observe:** A customer who purchased a gift box has not made a self-purchase within 45 days of the gift purchase.

**Diagnosis:** Gift Buyer customers are a distinct segment. They may have no personal interest in Darjeeling tea  -  they bought it for someone else. Without a specific conversion attempt, they will never become self-purchasers by accident.

**Question before acting:** Did this customer receive the Day 14 "keep some for yourself" email? What was the click and conversion rate on that email?

**Action options:**
- If the email did not go out: fix the segment filter to identify gift box purchasers and trigger the flow.
- If the email went out with <1% conversion: test a different message angle  -  less "buy for yourself," more "discover what you gifted."
- At Day 45: trigger a final gift-buyer winback with a small first-self-purchase offer.
- If no conversion at Day 60: move to general re-engagement cadence.

**Do not:** Send Gift Buyer customers the same replenishment reminder as Daily Premium Tea Drinker customers. "Running low on your Darjeeling tea?" is irrelevant to a buyer who bought it for someone else.

---

## Section 4  -  Margin Decision Rules

---

### Rule M1  -  Discount Rate Rising Without a Campaign Explanation

**What you observe:** Discount rate on full-price products rises to >15% over 3 weeks without a planned promotional campaign.

**Diagnosis:** Discount codes from a previous campaign may still be in circulation. Or a third-party coupon site may be scraping and publishing Dorje promo codes. Or the team has started applying manual discounts at checkout to convert hesitant buyers  -  a bad habit that trains buyers to always ask.

**Question before acting:** Where are the discount codes being applied? Is there a specific code driving the spike?

**Action options:**
- Audit active discount codes and deactivate any with unintended expiry or unlimited use.
- Check if third-party coupon sites are publishing Dorje codes.
- Review whether customer service team is issuing manual discounts without a policy.
- Establish a discount policy: discounts only for first-purchase sampler, email subscriber welcome, and winback (with a cap and expiry date).

**Do not:** Allow rising discount rates to go undiagnosed. For a premium brand, each percentage point of discount rate is a signal of positioning erosion, not just a margin leak.

---

### Rule M2  -  Shipping Cost Per Order Rising

**What you observe:** Shipping cost per order increases week-over-week, reducing contribution margin even when revenue holds.

**Diagnosis:** Either volume is shifting toward regions with higher logistics costs (metro vs. Tier 2/3 cities), or the logistics provider has revised rates, or average order weight has increased without a proportional AOV increase.

**Question before acting:** What is the average shipping cost by region this week vs. last month? Has the logistics contract changed?

**Action options:**
- Map orders by region and compare shipping cost per region to prior periods.
- Review free-shipping threshold  -  if too low, a large number of orders may fall just below the threshold and ship at low AOV, squeezing margin.
- Evaluate whether raising the free-shipping threshold slightly would improve CM without significant CVR impact.
- Flag to finance if the logistics rate card has changed.

**Do not:** Absorb rising shipping costs as a fixed cost of doing business without understanding the driver. For a brand shipping premium tea direct from Darjeeling, logistics is one of the largest variable cost levers.

---

## Section 5  -  Experiment Decision Rules

---

### Rule E1  -  When to Scale an Experiment

Scale when all of the following are true:
- The primary metric moved in the expected direction
- The contribution margin on experiment-attributed orders is positive
- The sample size is sufficient to trust the result (not a 3-order test)
- The result has held for at least 2 weeks (not a one-week spike)

---

### Rule E2  -  When to Fix an Experiment

Fix (do not kill) when:
- There is clear intent signal (sessions, CTR, add-to-cart) but conversion did not complete
- The hypothesis was directionally correct but execution was off (wrong copy, wrong CTA, wrong timing)
- The metric moved, but not enough  -  the idea has potential but needs refinement

---

### Rule E3  -  When to Kill an Experiment

Kill when:
- The metric did not move after 3 weeks of adequate traffic
- The contribution margin on experiment orders was negative
- The hypothesis has been tested twice with different executions and both failed
- Operator bandwidth is being consumed without revenue signal

---

### Rule E4  -  When Not to Decide

Do not make a scale/fix/kill decision when:
- The experiment has been running less than 2 weeks
- Traffic volume to the test variant is below 200 sessions or 20 orders
- An external event (sale, campaign spike, platform issue) contaminated the test window
- Multiple experiments were running simultaneously (measurement noise)

In these cases: extend the test window, not the conclusion.

---

## Decision Rule Summary Table

| Rule | Pattern | Likely Diagnosis | Primary Action |
|---|---|---|---|
| A1 | CTR down, CVR stable | Creative fatigue | Refresh creative |
| A2 | CTR stable, CVR down | Landing page or offer friction | Fix page, not spend |
| A3 | ROAS positive, CM negative | Variable costs absorbing margin | Fix cost structure before scaling |
| A4 | CAC > break-even CAC | First order unprofitable | Hold spend; check repeat rate |
| A5 | One channel dominates CM | Audience intent advantage | Scale efficient channel; reduce weak ones |
| C1 | High sessions, low add-to-cart | Trust or value framing gap | Price-per-cup, estate proof, reviews |
| C2 | High ATC, low checkout completion | Checkout friction | Shipping, payment, or abandonment flow |
| C3 | CVR varies by product | Segment mismatch | Segment-specific landing pages |
| R1 | Repeat rate flat at Day 60 | Flow failure or cycle timing | Audit flows; check replenishment timing |
| R2 | Subscription churn spike | Over-supply, fatigue, or delivery | Diagnose cancel survey; offer pause |
| R3 | Gift Buyer not converting to self-purchaser | No conversion attempt made | Build Gift Buyer-specific follow-up flow |
| M1 | Discount rate rising unexplained | Stale codes or policy drift | Audit discount codes; set policy |
| M2 | Shipping cost per order rising | Regional mix or logistics rate change | Map by region; review threshold |
| E1–E4 | Experiment decisions | Various | Scale / Fix / Kill / Wait framework |
