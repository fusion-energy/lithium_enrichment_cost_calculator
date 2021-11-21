
import math

import lithium_enrichment_cost_calculator as lecc

class TestFindSwuAmount():

    def test_increasing_product_amount_increases_swu(self):

        swu_amount_small = lecc.find_swu_amount(
            product_amount=100,
            product_enrichment_fraction=0.5,
            tails_enrichment_fraction=0.03,
            feed_enrichment_fraction=0.0759,
        )

        swu_amount_large = lecc.find_swu_amount(
            product_amount=100,
            product_enrichment_fraction=0.6,
            tails_enrichment_fraction=0.03,
            feed_enrichment_fraction=0.0759,
        )

        assert swu_amount_small > 0
        assert swu_amount_large > 0
        assert swu_amount_small < swu_amount_large

    
    def test_increasing_product_increases_swu(self):
    
        swu_amount_small = lecc.find_swu_amount(
            product_amount=100,
            product_enrichment_fraction=0.6,
            tails_enrichment_fraction=0.03,
            feed_enrichment_fraction=0.0759,
        )

        swu_amount_large = lecc.find_swu_amount(
            product_amount=150,
            product_enrichment_fraction=0.6,
            tails_enrichment_fraction=0.03,
            feed_enrichment_fraction=0.0759,
        )

        assert swu_amount_small > 0
        assert swu_amount_large > 0
        assert swu_amount_small < swu_amount_large
    
    def test_increasing_tails_amount_decreases_swu(self):
        pass

    def test_increasing_tails_enrichment_decreases_swu(self):
        pass

    def test_increasing_feed_amount_increases_swu(self):
        pass

    def test_increasing_feed_enrichment_increases_swu(self):
        pass
