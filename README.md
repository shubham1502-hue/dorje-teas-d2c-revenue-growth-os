# Dorje Teas — D2C Revenue Growth OS

> A founder-facing revenue operating system for a premium Darjeeling tea brand.
> Built using public information, clearly labeled assumptions, and synthetic data.
> No internal Dorje data was used at any point.

---

## What This Is

Dorje Teas sells estate-grown Darjeeling tea from Selim Hill — a heritage garden in Darjeeling, connected to Alt Carbon's broader Darjeeling revival thesis. It is not a commodity tea brand. It operates in a category where origin, trust, product education, harvest seasonality, gifting, and repeat purchase behavior matter as much as paid acquisition efficiency.

This project builds the revenue operating system a Founder's Office operator would install to track, diagnose, and improve Dorje's D2C performance weekly — without waiting for perfect data or a fully instrumented stack.

---

## The Core Question

> What should Dorje track, diagnose, and improve every week to grow D2C revenue without confusing campaign activity with actual revenue progress?

---

## North Star Metric

> **contribution-margin-positive repeat D2C revenue**

---

## What This Includes

| Area | What It Answers |
|---|---|
| Brand and category research | Who buys premium Darjeeling tea, and why would they choose Dorje? |
| 6-month growth thesis | What should the revenue system prioritize, in what sequence? |
| D2C funnel teardown | Where does revenue leak, and what decision does each metric trigger? |
| CAC / ROAS / LTV / Contribution margin model | Which channels create profitable, repeatable customers? |
| Weekly founder dashboard | What does the founder review every Monday? |
| Retention and repeat purchase | How does a premium tea brand build a replenishment loop? |
| Subscription operating logic | How should Tea Club behave as a revenue line? |
| Python analysis notebooks | What do the synthetic CSVs suggest about funnel, retention, CM, and campaigns? |
| Growth playbooks | What should acquisition, repeat purchase, subscription, gifting, experiments, and winback do next? |
| Founder review system | How are weekly decisions, monthly reviews, risks, experiments, and cadence documented? |
| AI-assisted operating docs | How does the system stay clean, documented, and decision-oriented? |

---

## Repo Structure

```
dorje-teas-d2c-revenue-growth-os/
│
├── README.md                          ← Start here
├── EXECUTIVE_SUMMARY.md               ← One-page founder memo
├── ASSUMPTIONS_AND_BOUNDARIES.md      ← Data honesty and project scope
├── PUBLIC_RESEARCH_NOTES.md           ← Brand, category, and funnel observations
│
├── 01_strategy/
│   ├── dorje_6_month_growth_thesis.md
│   ├── customer_segments_and_use_cases.md
│   ├── category_and_competitor_scan.md
│   ├── product_ladder_and_offer_architecture.md
│   └── growth_bets_prioritization.md
│
├── 02_metrics_os/
│   ├── north_star_metrics_tree.md
│   ├── d2c_funnel_metrics_dictionary.md
│   ├── weekly_revenue_review_template.md
│   ├── metric_owner_map.md
│   └── decision_rules.md
│
├── 03_dashboard_blueprints/
│   ├── founder_dashboard_spec.md
│   ├── campaign_dashboard_spec.md
│   ├── retention_dashboard_spec.md
│   ├── contribution_margin_dashboard_spec.md
│   └── google_sheets_dashboard_layout.md
│
├── 04_data_model/
│   ├── synthetic_data_schema.md
│   ├── data_dictionary.md
│   ├── generate_synthetic_data.py
│   ├── sample_orders.csv
│   ├── sample_ad_spend.csv
│   ├── sample_product_catalog.csv
│   └── sample_customer_cohorts.csv
│
├── 05_python_analysis/
│   ├── requirements.txt
│   ├── revenue_funnel_analysis.ipynb
│   ├── retention_cohort_analysis.ipynb
│   ├── contribution_margin_model.ipynb
│   └── campaign_efficiency_analysis.ipynb
│
├── 06_growth_playbooks/
│   ├── acquisition_playbook.md
│   ├── repeat_purchase_playbook.md
│   ├── subscription_growth_playbook.md
│   ├── gifting_and_seasonal_campaigns.md
│   ├── landing_page_experiment_backlog.md
│   └── winback_and_reactivation_playbook.md
│
├── 07_founder_review_system/
│   ├── weekly_revenue_review_memo.md
│   ├── monthly_business_review_memo.md
│   ├── revenue_risk_register.md
│   ├── experiment_tracker.md
│   └── operating_cadence.md
│
└── 08_ai_assisted_ops/
    ├── ai_prompts_for_weekly_diagnosis.md
    ├── ai_prompt_for_campaign_postmortem.md
    ├── ai_prompt_for_retention_insights.md
    └── documentation_sop.md
```

---

## How to Review This Repo in 5 Minutes

**If you are a founder or hiring manager reviewing this:**

1. **`EXECUTIVE_SUMMARY.md`** — Read this first. One-page memo on the 6-month revenue thesis.
2. **`07_founder_review_system/weekly_revenue_review_memo.md`** — See the founder-facing operating output.
3. **`05_python_analysis/campaign_efficiency_analysis.ipynb`** — Inspect how ROAS is checked against contribution ROAS.
4. **`06_growth_playbooks/repeat_purchase_playbook.md`** — Review the retention logic by product and segment.
5. **`02_metrics_os/decision_rules.md`** — Check that metrics connect to actions.
6. **`ASSUMPTIONS_AND_BOUNDARIES.md`** — Confirm the data honesty boundary.

---

## What This Is Not

This project does not use internal Dorje data. It is not:

- An audit of Dorje's actual D2C performance
- A claim of Shopify ownership or access
- A claim of media buying or ad account management
- A claim of live profit-and-loss ownership
- Based on any private revenue, order, or customer data from Dorje

All revenue, CAC, ROAS, CVR, retention, and margin figures in this repo are **synthetic model values** created to demonstrate operating logic. Public website observations are labeled as public. Everything else is labeled as assumed or synthetic.

See `ASSUMPTIONS_AND_BOUNDARIES.md` for full scope.

---

## Why Dorje Specifically

Dorje Teas represents a category of D2C brand where generic growth advice fails quickly:

- Premium pricing requires trust and education before conversion
- Darjeeling harvest seasonality creates natural campaign windows
- Repeat purchase is driven by taste familiarity and brewing habit, not discounts
- Subscription economics depend on education, not just offer mechanics
- Contribution margin is squeezed by premium packaging, logistics, and small order sizes
- Brand narrative — Selim Hill, Darjeeling revival, Alt Carbon — is a growth lever, not just marketing copy

A revenue OS for Dorje needs to hold all of this together in a weekly operating rhythm. That is what this project attempts to show.

---

## Skills Demonstrated

`D2C funnel analysis` · `CAC / ROAS / LTV modeling` · `Retention cohort analysis` · `Contribution margin modeling` · `Campaign efficiency analysis` · `Python notebooks (pandas, numpy, matplotlib, seaborn)` · `Founder-facing reporting` · `Growth playbook design` · `Revenue experiment design` · `Google Sheets-style operating logic` · `AI-assisted documentation` · `Consumer and category research` · `Cross-functional owner/action tracking` · `GitHub / Markdown`

---

## Built by

**Shubham Singh**
Founder's Office & Revenue Ops | Built operating systems from zero at a founder-led startup
[github.com/shubham1502-hue](https://github.com/shubham1502-hue)
