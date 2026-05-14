# Google Sheets Dashboard Layout — Dorje Teas

> Exact tab structure, column layout, and formula logic for implementing the Dorje revenue OS in Google Sheets.
> This file makes the dashboard specs in `03_dashboard_blueprints/` executable.
> All sample values are synthetic. No internal Dorje data used.

---

## Why Google Sheets

Google Sheets is the right stack for a small D2C Founder's Office team because:
- No engineering dependency — the operator builds and maintains it
- Real-time sharing with founder and team
- Native import from Shopify CSV exports and Google Ads reports
- Flexible enough for weekly manual updates, structured enough for consistent reporting
- Formulas are auditable and explainable — no black-box dashboards

The goal is a dashboard a founder can open on Monday morning and understand in 10 minutes.

---

## Workbook Structure

The workbook has 13 tabs, organized in three layers:

**Layer 1 — Raw Data (inputs, updated weekly):**
`RAW_Orders` · `RAW_AdSpend` · `RAW_Products` · `RAW_Cohorts`

**Layer 2 — Calculated Views (operator-built, formula-driven):**
`CALC_MetricDictionary` · `CALC_CM_Model`

**Layer 3 — Dashboard Outputs (founder-facing):**
`DASH_Founder` · `DASH_Campaign` · `DASH_Retention` · `DASH_ContributionMargin` · `DASH_Experiments`

**Layer 4 — Operating Documents:**
`OPS_WeeklyReview` · `OPS_Assumptions`

---

## Tab 1: OPS_Assumptions

**Purpose:** Single source of truth for all cost assumptions. Every formula in the workbook references this tab — not hardcoded values.

**Why this matters:** When COGS changes, packaging cost changes, or the logistics rate card updates, the operator changes one cell here and every dashboard recalculates automatically.

**Column layout:**

| Col A | Col B | Col C | Col D |
|---|---|---|---|
| Assumption Name | Value | Unit | Notes |
| Product COGS — First Flush 100g | 180 | ₹ per order | [SYNTHETIC] estimated from premium whole-leaf Darjeeling category |
| Product COGS — Second Flush 100g | 160 | ₹ per order | [SYNTHETIC] |
| Product COGS — Chai 100g | 120 | ₹ per order | [SYNTHETIC] |
| Product COGS — Green Tea 100g | 150 | ₹ per order | [SYNTHETIC] |
| Product COGS — Pyramid Teabags (25 bags) | 90 | ₹ per order | [SYNTHETIC] |
| Product COGS — Gift Box (standard) | 280 | ₹ per order | [SYNTHETIC] |
| Packaging — Standard | 55 | ₹ per order | [SYNTHETIC] branded box + inner foil + label |
| Packaging — Premium (Gift Box) | 130 | ₹ per order | [SYNTHETIC] gift box + ribbon + card |
| Shipping Cost — Metro | 90 | ₹ per order | [SYNTHETIC] |
| Shipping Cost — Tier 2/3 | 130 | ₹ per order | [SYNTHETIC] |
| Shipping Cost — Blended (default) | 110 | ₹ per order | [SYNTHETIC] |
| Payment Gateway Fee | 2% | % of net revenue | Standard Indian gateway rate |
| Free Shipping Threshold | 699 | ₹ | Assumed from public cart observation |
| Break-Even CAC — Standard Order | =B_GrossMargin_Standard | ₹ | Auto-calculated from CM model |
| Target LTV:CAC Ratio | 2.0 | x | Minimum acceptable |
| Target Repeat Purchase Rate (M2) | 25% | % | Hypothesis — recalibrate with data |
| Target Subscription Attach Rate | 10% | % | Post-second-purchase target |
| Target CM% (blended) | 20% | % | Minimum sustainable |

**Named ranges to define:**
- `COGS_FirstFlush` → B2
- `COGS_Chai` → B4
- `PKG_Standard` → B8
- `PKG_Gift` → B9
- `SHIP_Blended` → B12
- `GW_Fee` → B13
- `Target_LTV_CAC` → B16

---

## Tab 2: RAW_Orders

**Purpose:** Weekly Shopify order export. One row per order. This is the primary input for revenue, AOV, repeat purchase, product mix, and contribution margin calculations.

**Source:** Shopify → Orders → Export (filtered to D2C channel, last 90 days rolling)

**Column layout:**

| Col | Field | Format | Notes |
|---|---|---|---|
| A | order_id | Text | Shopify order number |
| B | order_date | Date (DD/MM/YYYY) | |
| C | customer_id | Text | Shopify customer ID |
| D | customer_type | Text | "new" or "returning" |
| E | product_id | Text | SKU |
| F | product_name | Text | As listed in Shopify |
| G | product_category | Text | First Flush / Chai / Gift Box / etc. |
| H | quantity | Number | Units per order |
| I | gross_revenue | Currency ₹ | Before discount |
| J | discount_amount | Currency ₹ | 0 if no discount applied |
| K | net_revenue | Currency ₹ | =I-J |
| L | shipping_charged | Currency ₹ | What customer paid for shipping |
| M | gateway_fee | Currency ₹ | =K*OPS_Assumptions.GW_Fee |
| N | shipping_cost | Currency ₹ | =OPS_Assumptions.SHIP_Blended (or region-adjusted) |
| O | packaging_cost | Currency ₹ | =IF(G="Gift Box", OPS_Assumptions.PKG_Gift, OPS_Assumptions.PKG_Standard) |
| P | cogs | Currency ₹ | VLOOKUP on product_id to COGS table in OPS_Assumptions |
| Q | gross_margin | Currency ₹ | =K-M-N-O-P |
| R | gross_margin_pct | Percentage | =Q/K |
| S | channel | Text | google_search / meta / email / organic / direct |
| T | campaign_id | Text | Links to RAW_AdSpend |
| U | attributed_spend | Currency ₹ | From CALC_CM_Model channel attribution |
| V | contribution_margin | Currency ₹ | =Q-U |
| W | cm_pct | Percentage | =V/K |
| X | city | Text | For regional shipping cost analysis |
| Y | is_subscription | Boolean | TRUE / FALSE |
| Z | discount_code | Text | For discount source audit |

**Key derived columns (operator-built):**

```
Col K (net_revenue):    =I2-J2
Col M (gateway_fee):    =K2*VLOOKUP("Payment Gateway Fee", OPS_Assumptions!A:B, 2, FALSE)
Col O (packaging_cost): =IF(G2="Gift Box",
                           VLOOKUP("Packaging - Premium", OPS_Assumptions!A:B, 2, FALSE),
                           VLOOKUP("Packaging - Standard", OPS_Assumptions!A:B, 2, FALSE))
Col P (cogs):           =VLOOKUP(F2, CALC_ProductCOGS, 2, FALSE)
Col Q (gross_margin):   =K2-M2-N2-O2-P2
Col R (gm_pct):         =Q2/K2
```

**Weekly update process:**
1. Export Shopify orders for last 7 days as CSV
2. Paste into RAW_Orders below last row
3. Verify formula columns auto-populate (spot-check 3 rows)
4. Confirm no duplicate order_ids

---

## Tab 3: RAW_AdSpend

**Purpose:** Weekly ad platform export. One row per campaign per day (or per week, depending on export format).

**Source:** Google Ads → Reports → Campaign performance export. Meta Ads Manager → Ads Reporting (if active).

**Column layout:**

| Col | Field | Format | Notes |
|---|---|---|---|
| A | date | Date | |
| B | platform | Text | "google" / "meta" |
| C | campaign_id | Text | |
| D | campaign_name | Text | |
| E | campaign_objective | Text | Conversion / Awareness / Retargeting |
| F | spend | Currency ₹ | |
| G | impressions | Number | |
| H | clicks | Number | |
| I | ctr | Percentage | =H/G |
| J | cpc | Currency ₹ | =F/H |
| K | sessions | Number | From GA4 utm source/medium match |
| L | add_to_cart | Number | From GA4 or Shopify |
| M | checkouts | Number | From GA4 or Shopify |
| N | orders | Number | Platform-reported conversions |
| O | revenue | Currency ₹ | Platform-reported conversion value |
| P | roas | Number | =O/F |
| Q | cac | Currency ₹ | =F/N |
| R | cm_from_orders | Currency ₹ | SUMIF on RAW_Orders[campaign_id] for CM |
| S | contribution_roas | Number | =R/F |
| T | new_customers | Number | From Shopify customer type filter |
| U | new_customer_cac | Currency ₹ | =F/T |

**Key derived columns:**

```
Col I (CTR):               =H2/G2
Col J (CPC):               =F2/H2
Col P (ROAS):              =O2/F2
Col Q (CAC):               =F2/N2
Col S (Contribution ROAS): =R2/F2
```

**Weekly update process:**
1. Export Google Ads campaign report (last 7 days): Date, Campaign, Spend, Impressions, Clicks, Conversions, Conv. Value
2. Export Meta Ads Manager report with same fields (if running)
3. Paste into RAW_AdSpend below last row
4. Update Col R (cm_from_orders) by running SUMIF against RAW_Orders[campaign_id] for the same date range
5. Verify ROAS and Contribution ROAS auto-calculate

---

## Tab 4: RAW_Products

**Purpose:** Product catalog with COGS assumptions. Used as a VLOOKUP reference by RAW_Orders.

**Column layout:**

| Col | Field | Notes |
|---|---|---|
| A | product_id | SKU |
| B | product_name | Full name |
| C | category | First Flush / Chai / Gift Box / etc. |
| D | pack_size_gm | Weight in grams |
| E | price_inr | Listed price |
| F | cogs_inr | [SYNTHETIC] from OPS_Assumptions |
| G | packaging_cost | [SYNTHETIC] standard or premium |
| H | gross_margin_pct | =(E-F-G)/E |
| I | product_ladder_rung | 1–6 (from product_ladder_and_offer_architecture.md) |
| J | subscription_eligible | TRUE / FALSE |
| K | replenishment_days | Estimated days per 100g at 1–2 cups/day |

---

## Tab 5: RAW_Cohorts

**Purpose:** Monthly cohort table tracking repeat purchase behavior. Updated once per month.

**Source:** Shopify → Customers → Cohort analysis export (or manual COUNTIFS on RAW_Orders).

**Column layout:**

| Col | Field | Notes |
|---|---|---|
| A | cohort_month | e.g., "Jan 2025" |
| B | new_customers | New buyers acquired in that month |
| C | month_0_revenue | Revenue from these customers in acquisition month |
| D | month_1_customers | How many of cohort B returned in Month 1 |
| E | month_1_revenue | Revenue from returning cohort in Month 1 |
| F | month_2_customers | |
| G | month_2_revenue | |
| H | month_3_customers | |
| I | month_3_revenue | |
| J | repeat_rate_m1 | =D/B |
| K | repeat_rate_m2 | =F/B |
| L | repeat_rate_m3 | =H/B |
| M | cumulative_ltv_m3 | =C+E+G+I / B |
| N | cac_this_cohort | Total spend to acquire B customers ÷ B |
| O | ltv_cac_ratio_m3 | =M/N |

**Formula examples:**

```
Col J (repeat_rate_m1): =D2/B2
Col M (cumulative_ltv):  =(C2+E2+G2+I2)/B2
Col O (ltv:cac ratio):   =M2/N2
```

---

## Tab 6: CALC_CM_Model

**Purpose:** Contribution margin calculation engine. Feeds the DASH_ContributionMargin tab.

**Structure:**

**Section A — Weekly Order-Level Summary:**

| Metric | Formula |
|---|---|
| Total Orders | =COUNTA(RAW_Orders[order_id]) |
| Total Gross Revenue | =SUM(RAW_Orders[gross_revenue]) |
| Total Discounts | =SUM(RAW_Orders[discount_amount]) |
| Total Net Revenue | =SUM(RAW_Orders[net_revenue]) |
| Total COGS | =SUM(RAW_Orders[cogs]) |
| Total Packaging | =SUM(RAW_Orders[packaging_cost]) |
| Total Shipping | =SUM(RAW_Orders[shipping_cost]) |
| Total Gateway Fees | =SUM(RAW_Orders[gateway_fee]) |
| Total Gross Margin | =SUM(RAW_Orders[gross_margin]) |
| Total Paid Media | =SUM(RAW_AdSpend[spend]) |
| Total Contribution Margin | =Total_Gross_Margin - Total_Paid_Media |
| CM% | =Total_CM / Total_Net_Revenue |
| Blended ROAS | =Total_Net_Revenue / Total_Paid_Media |
| Break-Even CAC | =Total_Gross_Margin / Total_New_Customers |

**Section B — CM by Channel:**

```
Google Search CM:   =SUMIF(RAW_Orders[channel], "google_search", RAW_Orders[contribution_margin])
Google Search Rev:  =SUMIF(RAW_Orders[channel], "google_search", RAW_Orders[net_revenue])
Google Search CM%:  =Google_Search_CM / Google_Search_Rev

Meta CM:            =SUMIF(RAW_Orders[channel], "meta", RAW_Orders[contribution_margin])
Email / WA CM:      =SUMIF(RAW_Orders[channel], "email", RAW_Orders[contribution_margin])
Organic CM:         =SUMIF(RAW_Orders[channel], "organic", RAW_Orders[contribution_margin])
```

**Section C — CM by Product Category:**

```
First Flush CM:     =SUMIF(RAW_Orders[product_category], "First Flush", RAW_Orders[contribution_margin])
Chai CM:            =SUMIF(RAW_Orders[product_category], "Chai", RAW_Orders[contribution_margin])
Gift Box CM:        =SUMIF(RAW_Orders[product_category], "Gift Box", RAW_Orders[contribution_margin])
[repeat for all categories]
```

**Section D — CM by Customer Type:**

```
New Customer CM:        =SUMIF(RAW_Orders[customer_type], "new", RAW_Orders[contribution_margin])
Returning Customer CM:  =SUMIF(RAW_Orders[customer_type], "returning", RAW_Orders[contribution_margin])
Subscription CM:        =SUMIF(RAW_Orders[is_subscription], TRUE, RAW_Orders[contribution_margin])
```

---

## Tab 7: DASH_Founder

**Purpose:** Founder-facing weekly dashboard. Pulls from CALC_CM_Model and RAW tabs via reference formulas. No data should be hardcoded in this tab.

**Layout by block (rows):**

| Rows | Block |
|---|---|
| 1–3 | Header: Week date, prepared by, reviewed with |
| 5–6 | Week Summary text (operator-written) |
| 8–16 | Block 1: Revenue Snapshot table |
| 18–24 | Block 2: Acquisition Performance table |
| 26–32 | Block 3: Funnel Conversion table |
| 34–42 | Block 4: Product Performance table |
| 44–52 | Block 5: Retention and Repeat Purchase |
| 54–60 | Block 6: Subscription Health |
| 62–72 | Block 7: Contribution Margin Summary |
| 74–80 | Block 8: Experiment Status |
| 82–86 | Block 9: Top 3 Issues (text fields) |
| 88–94 | Block 10: Founder Decisions Needed |

**Cell reference example (Revenue Snapshot):**

```
B10 (This Week Revenue):    =SUMIFS(RAW_Orders[net_revenue], RAW_Orders[order_date], ">="&ThisWeekStart, RAW_Orders[order_date], "<="&ThisWeekEnd)
C10 (Last Week Revenue):    =SUMIFS(RAW_Orders[net_revenue], RAW_Orders[order_date], ">="&LastWeekStart, RAW_Orders[order_date], "<="&LastWeekEnd)
D10 (4W Avg):               =(B10+C10+PriorWeek2Rev+PriorWeek3Rev)/4
E10 (WoW %):                =(B10-C10)/C10
```

**Conditional formatting rules:**

```
Revenue WoW Change:
  Green if >5%
  Yellow if 0% to 5%
  Red if negative

Returning Revenue %:
  Green if >=35%
  Yellow if 25% to 35%
  Red if <25%

CM%:
  Green if >20%
  Yellow if 10% to 20%
  Red if <10% or negative

Discount Rate:
  Green if <10%
  Yellow if 10% to 15%
  Red if >15%
```

---

## Tab 8: DASH_Campaign

**Purpose:** Campaign-level performance view for Growth operator. Pulls from RAW_AdSpend.

**Primary view — Campaign Efficiency Table:**

```
Columns: Campaign Name | Spend | Impressions | CTR | CPC | Sessions | CVR | Orders | Revenue | CAC | ROAS | CM | Contribution ROAS | Status

Sort: by Contribution ROAS descending

Status formula:
=IF(S2>1.5, "Scale",
  IF(S2>=1.0, "Hold",
    IF(S2>=0.5, "Fix",
      "Pause")))
```

**Secondary views (separate sections on same tab):**
- Creative fatigue view: CTR trend over 4 weeks by campaign
- Search term performance: top 20 converting search queries (manual paste from Google Ads)
- Landing page performance: sessions by landing page + CVR by landing page (from GA4)

---

## Tab 9: DASH_Retention

**Purpose:** Retention and cohort view. Updated monthly.

**Cohort table (pulls from RAW_Cohorts):**

```
Rows: one per cohort month
Columns: Cohort | New Customers | M0 Rev | M1 Repeat Rate | M1 Rev | M2 Repeat Rate | M2 Rev | M3 Repeat Rate | M3 Rev | LTV:CAC
```

**Repeat rate heatmap:**
- Use conditional formatting on repeat rate columns
- Dark green = >30% repeat rate, light green = 20–30%, yellow = 10–20%, red = <10%

**Flow performance section:**

```
Columns: Flow Name | Segment | Sends | Opens | Clicks | Purchases | Revenue | CM
Rows: Day 7 education | Day 21 replenishment | Day 30 cross-sell | Day 45 subscription prompt | Winback (60+ day)
```

---

## Tab 10: DASH_ContributionMargin

**Purpose:** Full contribution margin breakdown. Pulls from CALC_CM_Model.

**Weekly CM waterfall (text layout, formula-driven):**

```
Gross Revenue:         ₹ [formula]
Less: Discounts:      -₹ [formula]
Net Revenue:           ₹ [formula]
Less: COGS:           -₹ [formula]
Less: Packaging:      -₹ [formula]
Less: Shipping:       -₹ [formula]
Less: Gateway Fees:   -₹ [formula]
                      ─────────────
Gross Margin:          ₹ [formula]    [GM%]
Less: Paid Media:     -₹ [formula]
                      ─────────────
Contribution Margin:   ₹ [formula]    [CM%]
```

**CM by channel table, CM by product table, CM by customer type table** — each pulled via SUMIF from CALC_CM_Model.

---

## Tab 11: DASH_Experiments

**Purpose:** Single source of truth for all running and closed experiments.

**Column layout:**

| Col | Field |
|---|---|
| A | experiment_name |
| B | hypothesis |
| C | primary_metric |
| D | secondary_metric |
| E | owner |
| F | start_date |
| G | end_date |
| H | segment |
| I | expected_lift |
| J | actual_result |
| K | sample_size |
| L | decision |
| M | learning |
| N | next_action |
| O | status |

**Status values:** `Planning` / `Running` / `Inconclusive — extend` / `Complete — Scale` / `Complete — Fix` / `Complete — Kill`

---

## Tab 12: OPS_WeeklyReview

**Purpose:** The Monday morning operator memo. Sections 1–10 from `weekly_revenue_review_template.md`. Text entry tab — no formulas here. The operator writes the narrative; numbers come from DASH tabs.

---

## Tab 13: CALC_MetricDictionary

**Purpose:** In-sheet reference. Paste the metric definitions from `d2c_funnel_metrics_dictionary.md` here so any operator can look up a formula without leaving the workbook.

---

## Implementation Checklist

**Week 1 (setup):**
- [ ] Create workbook with all 13 tabs
- [ ] Build OPS_Assumptions with cost inputs from finance/ops
- [ ] Define named ranges for all assumption values
- [ ] Set up RAW_Orders column structure and formula columns
- [ ] Set up RAW_AdSpend column structure
- [ ] Import first Shopify order export (last 30 days)
- [ ] Import first Google Ads export (last 30 days)
- [ ] Build CALC_CM_Model with SUMIF formulas
- [ ] Build DASH_Founder skeleton with cell references (not hardcoded values)
- [ ] Apply conditional formatting to DASH_Founder

**Week 2 (calibrate):**
- [ ] Complete first full weekly dashboard update
- [ ] Verify all SUMIF formulas return expected values
- [ ] Spot-check 5 random orders: manual CM calculation vs. sheet calculation
- [ ] Share DASH_Founder with founder for first review
- [ ] Collect feedback on what is missing or unclear
- [ ] Begin populating RAW_Cohorts with last 3 months of cohort data

**Week 3+ (operate):**
- [ ] Weekly Monday update: paste new orders + ad spend exports
- [ ] 15 minutes to update → 45 minutes to review and write memo
- [ ] Monthly: update RAW_Cohorts, refresh DASH_Retention
- [ ] Quarterly: review OPS_Assumptions for COGS or cost changes

---

## Common Formula Errors to Watch

Examples below are illustrative QA cases, not Dorje internal performance metrics.

| Error | Likely Cause | Fix |
|---|---|---|
| CM% shows >100% | COGS or shipping not populating — VLOOKUP returning 0 | Check product_id match in RAW_Products |
| ROAS shows #DIV/0! | Zero spend in that period | Wrap in IFERROR: `=IFERROR(O2/F2, "-")` |
| Cohort repeat rate >100% | Customer ID mismatch or duplicate orders | Audit customer_id field in Shopify export |
| Week-on-week % shows large spike | Date filter pulling wrong week | Verify ThisWeekStart / ThisWeekEnd named range values |
| CM negative on all channels | Attributed spend > gross margin | Check that paid media is not being double-counted in attribution |
