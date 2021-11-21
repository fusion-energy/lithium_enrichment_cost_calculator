import math

import lithium_enrichment_cost_calculator as lecc


class TestFindCostOfEnrichment:
    def test_increasing_product_amount_increases_cost(self):
        small_product_amount = lecc.find_cost_of_enrichment(
            product_amount=100.0,
            product_enrichment_fraction=0.6,
            swu_cost=56,
            tails_cost=27,
            tails_enrichment_fraction=0.03,
            feed_cost=29,
            feed_enrichment_fraction=0.0759,
        )
        large_product_amount = lecc.find_cost_of_enrichment(
            product_amount=200.0,
            product_enrichment_fraction=0.6,
            swu_cost=56,
            tails_cost=27,
            tails_enrichment_fraction=0.03,
            feed_cost=29,
            feed_enrichment_fraction=0.0759,
        )
        assert small_product_amount > 0
        assert large_product_amount > 0
        assert large_product_amount > small_product_amount

    def test_increasing_product_enrichment_increases_cost(self):
        pass

    def test_increasing_swu_cost_increases_cost(self):
        pass

    def test_increasing_tails_cost_decreases_cost(self):
        pass

    def test_increasing_tails_enrichment_decreases_cost(self):
        pass

    def test_increasing_feed_cost_increases_cost(self):
        pass

    def test_increasing_feed_enrichment_decreases_cost(self):
        pass
