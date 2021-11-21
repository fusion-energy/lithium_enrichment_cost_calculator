
import math

import lithium_enrichment_cost_calculator as lecc

class TestFindFeedAmount():

    def test_increased_product_amount_increases_feed_amount(self):

        feed_amount_small = lecc.find_feed_amount(
            product_amount=100,
            product_enrichment_fraction=0.5,
            tails_enrichment_fraction=0.3,
            feed_enrichment_fraction=0.0759,
        )

        feed_amount_large = lecc.find_feed_amount(
            product_amount=200,
            product_enrichment_fraction=0.5,
            tails_enrichment_fraction=0.3,
            feed_enrichment_fraction=0.0759,
        )

        assert feed_amount_small * 2 == feed_amount_large

    # def test_increased_product_enrichment_increases_feed_amount(self):

    # def test_increased_tails_enrichment_increases_feed_amount(self):

    # def test_increased_feed_enrichment_decreases_feed_amount(self):

