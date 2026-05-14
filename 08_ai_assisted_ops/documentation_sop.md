# Documentation SOP - Dorje Teas D2C Revenue Growth OS

> Operating documentation standards for this proof-of-work repo.

## Five Standing Rules

1. Every metric has one owner.
2. Every assumption is labeled [SYNTHETIC] or has a named source.
3. Every experiment has a decision before it is archived.
4. No metric appears in a dashboard without a decision trigger.
5. Weekly memo is written before the weekly meeting.

## File Update Cadence

| Cadence | Files | Trigger |
|---|---|---|
| Weekly | `07_founder_review_system/weekly_revenue_review_memo.md`, `07_founder_review_system/experiment_tracker.md` | Monday review and Friday experiment close |
| Monthly | `07_founder_review_system/monthly_business_review_memo.md`, `07_founder_review_system/revenue_risk_register.md` | Month-end business review |
| On-change | `04_data_model/data_dictionary.md`, `03_dashboard_blueprints/google_sheets_dashboard_layout.md` | Field, metric, formula, or source changes |
| On experiment close | `06_growth_playbooks/landing_page_experiment_backlog.md`, `07_founder_review_system/experiment_tracker.md` | Scale, fix, kill, or wait decision |

## Version Control Conventions

- Keep commits small and tied to a visible operating output.
- Do not mix data model changes with playbook copy changes unless one requires the other.
- Never commit generated notebook execution output unless intentionally needed.
- Use plain commit messages that state the operating change.

## Commit Message Format

Use one of these prefixes:

- `[WEEKLY]` for weekly memo and cadence updates.
- `[EXPERIMENT]` for experiment tracker or backlog updates.
- `[PLAYBOOK]` for acquisition, retention, gifting, subscription, or winback playbooks.
- `[DATA]` for synthetic data, data dictionary, schema, or notebook changes.
- `[FIX]` for validation, overclaiming, product naming, or broken-link fixes.

Examples:

```text
[DATA] add contribution margin notebook
[PLAYBOOK] add repeat purchase operating rules
[FIX] clarify synthetic data boundary
```

## Zombie Metrics Definition and Removal Process

A zombie metric is a number that appears in a dashboard but does not change a decision.

Removal process:

1. Ask what decision the metric supports.
2. If no owner can answer, remove it from weekly review.
3. If it is useful monthly but not weekly, move it to monthly review.
4. If it is a diagnostic drill-down, keep it in the source dashboard but not the founder memo.

## Quality Bar for a Complete File

A file is complete when it:

- States its data boundary.
- Uses [SYNTHETIC] labels for sample numbers.
- Names the owner or decision user.
- Connects metrics to actions.
- Avoids generic D2C advice.
- Uses canonical Dorje product names and segment names.
- Can be understood by a busy founder in one pass.
