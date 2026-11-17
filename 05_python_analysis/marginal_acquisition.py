"""Run the synthetic marginal acquisition and payback scenarios."""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from math import isfinite
from pathlib import Path
from statistics import mean


DATA_DIR = Path(__file__).resolve().parents[1] / "04_data_model"
HORIZON_MONTHS = 6


@dataclass(frozen=True)
class Scenario:
    name: str
    cac_multiple: float
    repeat_probability: float
    subscription_attach: float
    monthly_subscription_retention: float


SCENARIOS = (
    Scenario("Downside", 1.65, 0.12, 0.03, 0.60),
    Scenario("Base", 1.35, 0.21, 0.06, 0.75),
    Scenario("Upside", 1.10, 0.28, 0.10, 0.85),
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def pre_media_contribution(order: dict[str, str]) -> float:
    revenue = float(order["net_revenue"]) + float(order["shipping_charged"])
    variable_cost = sum(float(order[field]) for field in ("cogs", "packaging_cost", "shipping_cost", "gateway_fee"))
    return revenue - variable_cost


def contribution_path(
    first_order: float,
    repeat_order: float,
    subscription_order: float,
    scenario: Scenario,
) -> list[float]:
    """Expected cumulative pre-media contribution per acquired buyer, from month zero."""
    cumulative = [first_order]
    for month in range(1, HORIZON_MONTHS + 1):
        subscription = (
            scenario.subscription_attach
            * scenario.monthly_subscription_retention ** (month - 1)
            * subscription_order
        )
        # The illustrative repeat purchase occurs in month two among non-subscribers.
        repeat = 0.0
        if month == 2:
            repeat = (1 - scenario.subscription_attach) * scenario.repeat_probability * repeat_order
        cumulative.append(cumulative[-1] + subscription + repeat)
    return cumulative


def marginal_scenarios(campaign_id: str, incremental_budget: float, data_dir: Path = DATA_DIR) -> list[dict]:
    if not isfinite(incremental_budget) or incremental_budget <= 0:
        raise ValueError("Incremental spend must be a finite positive amount.")
    campaigns = [
        row
        for row in read_csv(data_dir / "sample_ad_spend.csv")
        if row["campaign_id"] == campaign_id and row["campaign_objective"] == "acquisition"
    ]
    spend = sum(float(row["spend"]) for row in campaigns)
    new_customers = sum(int(row["new_customers"]) for row in campaigns)
    if not isfinite(spend) or spend <= 0 or new_customers <= 0:
        raise ValueError("The selected acquisition campaign needs positive spend and new-customer counts.")

    orders = read_csv(data_dir / "sample_orders.csv")
    first_orders = [
        row for row in orders
        if row["campaign_id"] == campaign_id and row["customer_type"] == "new"
    ]
    subscription_orders = [row for row in orders if row["is_subscription"].lower() == "true"]
    repeat_orders = [
        row for row in orders
        if row["customer_type"] == "returning" and row["is_subscription"].lower() == "false"
    ]
    if not all((first_orders, subscription_orders, repeat_orders)):
        raise ValueError("The example needs first, subscription, and non-subscription repeat orders.")

    baseline_cac = spend / new_customers
    first = mean(pre_media_contribution(row) for row in first_orders)
    repeat = mean(pre_media_contribution(row) for row in repeat_orders)
    subscription = mean(pre_media_contribution(row) for row in subscription_orders)
    results = []
    for scenario in SCENARIOS:
        marginal_cac = baseline_cac * scenario.cac_multiple
        buyers = incremental_budget / marginal_cac
        cumulative = contribution_path(first, repeat, subscription, scenario)
        payback = next((month for month, value in enumerate(cumulative) if value >= marginal_cac), None)
        net_contribution = cumulative[-1] - marginal_cac
        results.append({
            "campaign_id": campaign_id,
            "scenario": scenario.name,
            "synthetic_campaign_weeks": len(campaigns),
            "sample_first_orders": len(first_orders),
            "baseline_cac_inr": round(baseline_cac, 2),
            "assumed_cac_multiple": scenario.cac_multiple,
            "marginal_cac_inr": round(marginal_cac, 2),
            "repeat_purchase_probability": scenario.repeat_probability,
            "subscription_attach": scenario.subscription_attach,
            "monthly_subscription_retention": scenario.monthly_subscription_retention,
            "first_order_pre_media_contribution_inr": round(first, 2),
            "repeat_order_pre_media_contribution_inr": round(repeat, 2),
            "subscription_order_pre_media_contribution_inr": round(subscription, 2),
            "incremental_media_budget_inr": round(incremental_budget, 2),
            "expected_incremental_buyers": round(buyers, 2),
            "six_month_max_cac_inr": round(cumulative[-1], 2),
            "six_month_net_per_buyer_inr": round(net_contribution, 2),
            "six_month_net_for_increment_inr": round(net_contribution * buyers, 2),
            "payback_month": payback,
            "decision": "Test increment with a holdout" if net_contribution >= 0 else "Hold incremental paid spend",
        })
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--campaign-id", default="CMP-GS-001")
    parser.add_argument("--budget", type=float, default=10_000, help="Incremental media spending in INR.")
    parser.add_argument("--output", type=Path, help="Write the CSV to this path.")
    args = parser.parse_args()
    try:
        results = marginal_scenarios(args.campaign_id, args.budget)
    except ValueError as error:
        parser.error(str(error))

    if args.output:
        with args.output.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(results[0]), lineterminator="\n")
            writer.writeheader()
            writer.writerows(results)
        return
    writer = csv.DictWriter(sys.stdout, fieldnames=list(results[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(results)


if __name__ == "__main__":
    main()
