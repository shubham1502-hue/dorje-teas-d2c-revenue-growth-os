# Dorje Teas D2C Revenue Growth OS

> Weekly D2C revenue operating system for a premium Darjeeling tea brand.
> Public-information and synthetic-data proof of work.
> No internal Dorje data was used at any point.

## 30-Second Read

I built this as a public-information and synthetic-data proof of work for a Founder's Office / Revenue Ops role at Dorje Teas.

The repo shows the weekly revenue system I would use to help a founder decide what to scale, fix, kill, investigate, or unblock across acquisition, CAC/ROAS, product page conversion, first purchase, repeat purchase, gifting, subscription/replenishment, and contribution margin.

This is not a claim of internal Dorje data, actual Shopify data, actual ad account data, live ad account access, media buying ownership, D2C P&L ownership, or actual Dorje performance improvement. It is a demonstration of how I think, diagnose, and operate.

If you are reviewing quickly, start here:

1. `EXECUTIVE_SUMMARY.md` - one-page founder thesis.
2. `07_founder_review_system/weekly_revenue_review_memo.md` - sample weekly founder memo.
3. `03_dashboard_blueprints/founder_dashboard_spec.md` - weekly revenue dashboard blueprint.
4. `07_founder_review_system/operating_cadence.md` - how the founder review runs.
5. `02_metrics_os/decision_rules.md` - scale, fix, kill, investigate, or unblock logic.
6. `05_python_analysis/campaign_efficiency_analysis.ipynb` - analytical proof against synthetic data.

A founder does not need to read every file. These are the first-click paths.

## Core Operating Question

What should Dorje track, diagnose, and improve every week to grow D2C revenue without confusing campaign activity with revenue progress?

## North Star Metric

**contribution-margin-positive repeat D2C revenue**

## What This Helps a Founder Decide

This system is designed to help a founder answer:

- Which channel is creating contribution-margin-positive customers?
- Where is the D2C funnel leaking?
- Which product, bundle, or landing page deserves more traffic?
- Are first-time buyers coming back?
- Is gifting creating healthy revenue or only seasonal spikes?
- Is subscription/replenishment improving LTV?
- Are CAC and ROAS improving without hiding margin leakage?
- What should be scaled, fixed, killed, investigated, or unblocked this week?

## Why This Is Not Over-Engineering

The repo is modular because a founder does not need every file every week.

The weekly operating layer is simple:

1. Founder revenue dashboard
2. Funnel diagnosis
3. Campaign and channel scorecard
4. Retention and repeat purchase review
5. Experiment tracker
6. Scale, fix, kill, investigate, or unblock decisions

The deeper files exist to make the system auditable, reproducible, and usable once real internal data is available.

The point is faster founder decisions, not more documentation.

## How to Review This Repo in 5 Minutes

1. `README.md` - understand the operating question and data boundary.
2. `EXECUTIVE_SUMMARY.md` - read the 6-month revenue thesis.
3. `07_founder_review_system/weekly_revenue_review_memo.md` - see the founder-facing output.
4. `03_dashboard_blueprints/founder_dashboard_spec.md` - inspect the weekly dashboard logic.
5. `02_metrics_os/decision_rules.md` - check how metrics become decisions.
6. `02_metrics_os/d2c_funnel_metrics_dictionary.md` - review the funnel teardown.
7. `05_python_analysis/campaign_efficiency_analysis.ipynb` - verify campaign economics logic.
8. `ASSUMPTIONS_AND_BOUNDARIES.md` - confirm the honesty boundary.

Do not start with the notebooks. They prove the analysis runs, but the founder path starts with the memo, dashboard, and decisions.

## What This Operating System Covers

| Operating function | What it contains | Decision it supports |
|---|---|---|
| Strategy and public research | Category scan, customer segments, product ladder, growth thesis | Where Dorje should focus first |
| Funnel and metrics system | North star tree, funnel dictionary, owner map, decision rules | Which metric needs action this week |
| Dashboard and founder review cadence | Founder dashboard spec, weekly memo, monthly memo, risk register, operating cadence | What the founder should review and unblock |
| Synthetic data and Python analysis | Synthetic CSVs, data dictionary, funnel, retention, margin, and campaign notebooks | Whether the logic works before real internal data is available |
| Growth playbooks | Acquisition, repeat purchase, subscription, gifting, experiments, winback | What to scale, fix, kill, or test next |
| AI-assisted operating prompts | Weekly diagnosis, campaign postmortem, retention insight, documentation SOP | How to keep the operating system clean and decision-oriented |

## Data Boundary

This project does not use:

- internal Dorje data
- actual Shopify data
- actual ad account data
- actual revenue data
- actual customer cohort data
- actual contribution margin data

It is:

- public-information based
- synthetic-data based
- a proof of thinking and operating style

All revenue, CAC, ROAS, CVR, retention, and margin figures in this repo are synthetic model values created to demonstrate operating logic. Public website observations are labeled as public. Everything else is labeled as assumed or synthetic.

See `ASSUMPTIONS_AND_BOUNDARIES.md` for full scope.

## Repo Structure

```
dorje-teas-d2c-revenue-growth-os/
│
├── README.md                          # Start here
├── EXECUTIVE_SUMMARY.md               # One-page founder memo
├── ASSUMPTIONS_AND_BOUNDARIES.md      # Data honesty and project scope
├── PUBLIC_RESEARCH_NOTES.md           # Brand, category, and funnel observations
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

## Why Dorje Specifically

Dorje Teas represents a category of D2C brand where generic growth advice fails quickly:

- Premium pricing requires trust and education before conversion
- Darjeeling harvest seasonality creates natural campaign windows
- Repeat purchase is driven by taste familiarity and brewing habit, not discounts
- Subscription economics depend on education, not just offer mechanics
- Contribution margin is squeezed by premium packaging, logistics, and small order sizes
- Brand narrative, Selim Hill, Darjeeling revival, and Alt Carbon context, is a growth lever, not just marketing copy

A revenue OS for Dorje needs to hold all of this together in a weekly operating rhythm. That is what this project attempts to show.

---

## Skills Demonstrated

`D2C funnel analysis`, `CAC / ROAS / LTV modeling`, `Retention cohort analysis`, `Contribution margin modeling`, `Campaign efficiency analysis`, `Python notebooks (pandas, numpy, matplotlib, seaborn)`, `Founder-facing reporting`, `Growth playbook design`, `Revenue experiment design`, `Google Sheets-style operating logic`, `AI-assisted documentation`, `Consumer and category research`, `Cross-functional owner/action tracking`, `GitHub / Markdown`

---

## Built by

**Shubham Singh**
Founder's Office & Revenue Ops | Built operating systems from zero at a founder-led startup
[github.com/shubham1502-hue](https://github.com/shubham1502-hue)
