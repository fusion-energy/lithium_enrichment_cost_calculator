
import math


def find_feed_amount(
    product_amount,
    product_enrichment_fraction,
    tails_enrichment_fraction,
    feed_enrichment_fraction=0.0759,
):

    numerator = product_enrichment_fraction - tails_enrichment_fraction
    denominator = feed_enrichment_fraction - tails_enrichment_fraction

    feed_amount = product_amount*(numerator/denominator)

    return feed_amount


def find_swu_amount(
    product_amount,
    product_enrichment_fraction,
    tails_amount,
    tails_enrichment_fraction,
    feed_amount,
    feed_enrichment_fraction,
):
    feed_term = feed_amount*((2.*feed_enrichment_fraction)-1.) * math.log(feed_enrichment_fraction/(1.-feed_enrichment_fraction))
    tails_term = tails_amount*(2.*tails_enrichment_fraction-1.) * math.log(tails_enrichment_fraction/(1.-tails_enrichment_fraction))
    product_term = product_amount*(2.*product_enrichment_fraction-1.) * math.log(product_enrichment_fraction/(1.-product_enrichment_fraction))
    
    swu = product_term+tails_term+feed_term

    return swu


def find_cost_of_enrichment(
    product_amount,
    product_enrichment_fraction,
    swu_cost,
    tails_cost,
    tails_enrichment_fraction,
    feed_cost,
    feed_enrichment_fraction=0.0759
):

    feed_amount = find_feed_amount(
        product_amount,
        product_enrichment_fraction,
        tails_enrichment_fraction,
        feed_enrichment_fraction=0.0759,
    )

    tails_amount = feed_amount - product_amount

    swu_amount = find_swu_amount(
        product_amount=product_amount,
        product_enrichment_fraction=product_enrichment_fraction,
        tails_amount=tails_amount,
        tails_enrichment_fraction=tails_enrichment_fraction,
        feed_amount=feed_amount,
        feed_enrichment_fraction=feed_enrichment_fraction,
    )

    cost = swu_cost * swu_amount
    cost =+ feed_amount * feed_cost
    cost =- tails_amount * tails_cost

    return cost


def find_minimal_cost_of_enrichment(
    product_amount,
    product_enrichment_fraction,
    feed_cost,
    swu_cost,
    tails_cost,
):
    pass

if __name__ == '__main__':
    pass
    # feed_amount = find_feed_amount(
    #     product_amount=100,
    #     product_enrichment_fraction=60,
    #     tails_enrichment_fraction=4.,
    #     feed_enrichment_fraction=0.0759,
    # )
    # print(feed_amount)
