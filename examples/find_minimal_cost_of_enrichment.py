import lithium_enrichment_cost_calculator as lecc

minimal_cost, optimal_tails = lecc.find_minimal_cost_of_enrichment(
    product_amount=100,
    product_enrichment_fraction=0.6,
    swu_cost=56,
    tails_cost=28,
    feed_cost=33,
    feed_enrichment_fraction=0.0759,
)

print(f"minimal cost of enrichment {minimal_cost}")
print(f"enrichment of tails at this cost {optimal_tails}")
