# Dorje Teas Public-Safe Revenue OS Case Study

This case study explains the proof-of-work value of the Dorje Teas D2C Revenue Growth OS without implying access to Dorje's internal systems, private data, or actual performance results.

## Context

Dorje Teas is a premium Darjeeling tea brand with public positioning around estate-grown tea, Selim Hill, harvest seasonality, and a direct D2C customer relationship.

Premium D2C tea is not a simple traffic problem. A founder has to understand acquisition quality, product education, repeat purchase, subscription timing, gifting, fulfillment, and contribution margin together.

## Public-Safe Boundary

This project uses:

- public website and category observations
- clearly labeled assumptions
- synthetic data
- sample operating artifacts

This project does not claim:

- internal Dorje data access
- Shopify backend access
- ad account access
- private customer-level data
- actual revenue or margin results
- live media buying ownership
- implemented company outcomes

The purpose is to show operating judgment, not to audit Dorje's actual business performance.

## Operating Problem

The operating problem is:

How should a founder review D2C revenue every week so the team does not confuse campaign activity with profitable revenue progress?

That means the system must connect:

- new and returning customer revenue
- CAC, ROAS, and contribution margin
- product and landing page performance
- repeat purchase and replenishment behavior
- subscription timing and churn risk
- gifting seasonality
- founder decisions and operator actions

## System Designed

The repo designs a weekly D2C revenue operating system with:

- a founder-readable executive summary
- a weekly revenue review memo
- dashboard blueprints for founder, campaign, retention, and margin views
- decision rules for scale, fix, pause, investigate, and kill calls
- synthetic datasets and data dictionaries
- growth playbooks by acquisition, retention, subscription, gifting, winback, and experiments
- AI-assisted prompts with explicit data-boundary rules
- templates for adoption by another D2C company

## Key Artifacts

| Artifact | Why it matters |
|---|---|
| `EXECUTIVE_SUMMARY.md` | Gives the founder the thesis and operating priority |
| `07_founder_review_system/weekly_revenue_review_memo.md` | Shows what a weekly founder memo can look like |
| `03_dashboard_blueprints/founder_dashboard_spec.md` | Defines the dashboard as a decision instrument |
| `02_metrics_os/decision_rules.md` | Converts metric movements into operating choices |
| `04_data_model/synthetic_data_schema.md` | Shows how real Shopify, campaign, product, and cohort data would replace sample data |
| `ASSUMPTIONS_AND_BOUNDARIES.md` | Protects credibility by stating what is public, synthetic, assumed, and not claimed |
| `templates/` | Makes the system easier to adapt without copying the Dorje example blindly |

## Example Founder Decisions This System Supports

These are decision types, not claims about actual Dorje decisions:

- Should paid spend scale, hold, or pause based on contribution margin, not ROAS alone?
- Which product page needs a conversion fix before more traffic is sent to it?
- Should subscription be shown before first purchase or after trust is built?
- Which gifting motion should be prepared before a seasonal window?
- Which retention flow is late, weak, or mapped to the wrong buyer segment?
- Which margin input blocks confident scaling?
- Which experiment should be scaled, fixed, killed, or allowed to run longer?

## What This Demonstrates About Operator Judgment

This project demonstrates:

- ability to structure ambiguity into a weekly operating cadence
- founder-first communication, not dashboard dumping
- revenue quality thinking beyond top-line sales
- margin-aware growth judgment
- practical D2C lifecycle thinking
- clear separation between public observation, synthetic data, and authorized internal exports
- ability to create templates and operating assets a team could adapt

## Limitations

The repo is not an implementation inside Dorje.

It does not prove Dorje performance, customer behavior, channel efficiency, or contribution margin. Any deployment would require authorized internal data, platform exports, finance inputs, and founder/team validation.

The synthetic data exists only to make the operating logic executable and reviewable.

## Role Mapping

| Role path | What this repo signals |
|---|---|
| Founder's Office | Can turn messy founder questions into weekly decisions, owner actions, and operating cadence |
| BizOps | Can connect strategy, metrics, workflows, risks, and follow-up loops |
| RevOps | Can reason through CAC, ROAS, contribution margin, funnel stages, and revenue quality |
| Growth Ops | Can design experiments, campaign checks, lifecycle flows, and landing page decision rules |
| Strategy | Can build a category-specific growth thesis with assumptions and decision points |
| Startup operator | Can communicate clearly, protect credibility boundaries, and produce usable operating artifacts |
