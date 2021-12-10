import unittest
import lithium_enrichment_cost_calculator as lecc


class TestFindCostOfEnrichment(unittest.TestCase):
    def setUp(self):
        self.default_scenario_cost = lecc.find_cost_of_enrichment(
            product_amount=100.0,
            product_enrichment_fraction=0.6,
            swu_cost=56,
            tails_cost=27,
            tails_enrichment_fraction=0.03,
            feed_cost=29,
            feed_enrichment_fraction=0.0759,
        )

    def test_default_cost_is_positive(self):
        assert self.default_scenario_cost > 0

    def test_increasing_product_amount_increases_cost(self):

        test_scenario_cost = lecc.find_cost_of_enrichment(
            product_amount=100.0 * 1.1,
            product_enrichment_fraction=0.6,
            swu_cost=56,
            tails_cost=27,
            tails_enrichment_fraction=0.03,
            feed_cost=29,
            feed_enrichment_fraction=0.0759,
        )

        assert test_scenario_cost > self.default_scenario_cost

    def test_increasing_product_enrichment_increases_cost(self):
        test_scenario_cost = lecc.find_cost_of_enrichment(
            product_amount=100.0,
            product_enrichment_fraction=0.6 * 1.1,
            swu_cost=56,
            tails_cost=27,
            tails_enrichment_fraction=0.03,
            feed_cost=29,
            feed_enrichment_fraction=0.0759,
        )

        assert test_scenario_cost > self.default_scenario_cost

    def test_increasing_swu_cost_increases_cost(self):
        test_scenario_cost = lecc.find_cost_of_enrichment(
            product_amount=100.0,
            product_enrichment_fraction=0.6,
            swu_cost=56 * 1.1,
            tails_cost=27,
            tails_enrichment_fraction=0.03,
            feed_cost=29,
            feed_enrichment_fraction=0.0759,
        )

        assert test_scenario_cost > self.default_scenario_cost

    def test_increasing_tails_cost_decreases_cost(self):
        test_scenario_cost = lecc.find_cost_of_enrichment(
            product_amount=100.0,
            product_enrichment_fraction=0.6,
            swu_cost=56,
            tails_cost=27 * 1.1,
            tails_enrichment_fraction=0.03,
            feed_cost=29,
            feed_enrichment_fraction=0.0759,
        )

        assert test_scenario_cost < self.default_scenario_cost

    def test_increasing_feed_cost_increases_cost(self):
        test_scenario_cost = lecc.find_cost_of_enrichment(
            product_amount=100.0,
            product_enrichment_fraction=0.6,
            swu_cost=56,
            tails_cost=27,
            tails_enrichment_fraction=0.03,
            feed_cost=29 * 1.1,
            feed_enrichment_fraction=0.0759,
        )

        assert test_scenario_cost > self.default_scenario_cost

    def test_increasing_feed_enrichment_decreases_cost(self):
        test_scenario_cost = lecc.find_cost_of_enrichment(
            product_amount=100.0,
            product_enrichment_fraction=0.6,
            swu_cost=56,
            tails_cost=27,
            tails_enrichment_fraction=0.03,
            feed_cost=29,
            feed_enrichment_fraction=0.0759 * 1.1,
        )

        assert test_scenario_cost < self.default_scenario_cost

    def test_increasing_tails_enrichment_decreases_cost(self):
        pass
