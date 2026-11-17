import unittest

from marginal_acquisition import Scenario, contribution_path, marginal_scenarios, pre_media_contribution


class MarginalAcquisitionTests(unittest.TestCase):
    def test_contribution_includes_shipping_collected_and_variable_costs(self):
        row = {
            "net_revenue": "100", "shipping_charged": "15", "cogs": "30",
            "packaging_cost": "10", "shipping_cost": "20", "gateway_fee": "2",
        }
        self.assertEqual(pre_media_contribution(row), 53)

    def test_repeat_orders_and_subscribers_have_distinct_contributions(self):
        scenario = Scenario("Fixture", 1.0, 1.0, 0.5, 0.5)
        path = contribution_path(100, 20, 50, scenario)
        self.assertEqual(path[:3], [100, 125, 147.5])
        self.assertEqual(len(path), 7)

    def test_sample_scenarios_change_the_payback_decision(self):
        downside, base, upside = marginal_scenarios("CMP-GS-001", 10_000)
        self.assertIsNone(downside["payback_month"])
        self.assertLess(downside["six_month_net_per_buyer_inr"], 0)
        self.assertEqual(base["payback_month"], 2)
        self.assertEqual(upside["payback_month"], 0)
        self.assertGreater(base["six_month_max_cac_inr"], base["marginal_cac_inr"])

    def test_missing_campaign_has_a_clear_error(self):
        with self.assertRaisesRegex(ValueError, "positive spend and new-customer counts"):
            marginal_scenarios("unknown", 10_000)


if __name__ == "__main__":
    unittest.main()
