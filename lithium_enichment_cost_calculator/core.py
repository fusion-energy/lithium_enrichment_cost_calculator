

import math

def find_feed_amount(
    product_amount,
    product_enrichment,
    tails_enrichment,
    feed_enrichment=0.079,
):

    numerator = product_enrichment - tails_enrichment
    denominator = feed_enrichment - tails_enrichment

    feed_amount = product_amount*(numerator/denominator)

    return feed_amount


def find_swu(
    product_amount,
    product_enrichment,
    tails_amount,
    tails_enrichment,
    feed_amount,
    feed_enrichment,
):
    product_term = product_amount*(2*(product_enrichment-1.))
    waste_term = product_amount*(2*(product_enrichment-1.))
    product_term = product_amount*(2*(product_enrichment-1.))


def find_cost_of_enrichment(
    product_amount,
    product_enrichment,
    feed_cost,
    swu_cost,
    tails_cost,
    tails_enrichment
):
    pass

def find_minimal_cost_of_enrichment(
    product_amount,
    product_enrichment,
    feed_cost,
    swu_cost,
    tails_cost,
):
    pass

if __name__ == '__main__':
    feed_amount = find_feed_amount(
        product_amount=100,
        product_enrichment=60,
        tails_enrichment=4.,
        feed_enrichment=7.9,
    )
    print(feed_amount)
