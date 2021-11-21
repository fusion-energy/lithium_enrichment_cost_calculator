
import lithium_enrichment_cost_calculator as lecc 

cost_of_enrichment = lecc.find_cost_of_enrichment(
    product_amount=100,
    product_enrichment_fraction=0.6,
    swu_cost=56,
    tails_cost=28,
    tails_enrichment_fraction=0.03,
    feed_cost=33,
    feed_enrichment_fraction=0.0759
)

print(f'cost_of_enrichment {cost_of_enrichment}')
