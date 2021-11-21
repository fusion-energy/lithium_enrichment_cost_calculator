
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


def find_swu_amount(
    product_amount,
    product_enrichment,
    tails_amount,
    tails_enrichment,
    feed_amount,
    feed_enrichment,
):
    feed_term = feed_amount*(2.*feed_enrichment-1.) * math.log(feed_enrichment/(1.-feed_enrichment))
    tails_term = tails_amount*(2.*tails_enrichment-1.) * math.log(tails_enrichment/(1.-tails_enrichment))
    product_term = product_amount*(2.*product_enrichment-1.) * math.log(product_enrichment/(1.-product_enrichment))
    
    swu = product_term+tails_term+feed_term

    return swu


def find_cost_of_enrichment(
    product_amount,
    product_enrichment,
    swu_cost,
    tails_cost,
    tails_enrichment,
    feed_cost,
    feed_enrichment=7.59
):

    feed_amount = find_feed_amount(
        product_amount,
        product_enrichment,
        tails_enrichment,
        feed_enrichment=0.079,
    )

    tails_amount = feed_amount - product_amount

    swu_amount = find_swu_amount(
        product_amount=product_amount,
        product_enrichment=product_enrichment,
        tails_amount=tails_amount,
        tails_enrichment=tails_enrichment,
        feed_amount=feed_amount,
        feed_enrichment=feed_enrichment,
    )

    cost = swu_cost * swu_amount
    cost =+ feed_amount * feed_cost
    cost =- tails_amount * tails_cost

    return cost


def find_minimal_cost_of_enrichment(
    product_amount,
    product_enrichment,
    feed_cost,
    swu_cost,
    tails_cost,
):
    pass

if __name__ == '__main__':
    pass
    # feed_amount = find_feed_amount(
    #     product_amount=100,
    #     product_enrichment=60,
    #     tails_enrichment=4.,
    #     feed_enrichment=7.9,
    # )
    # print(feed_amount)
