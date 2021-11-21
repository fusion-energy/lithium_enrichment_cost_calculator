import lithium_enrichment_cost_calculator as lecc

minimal_enrichment_cost, tails_percent = lecc.find_minimal_cost_of_enrichment(
    product_amount=1000,  # 1000kg of enriched lithium
    product_enrichment_fraction=0.6,  # 60% is a typical HCPB blanket enrichment amount
    feed_cost=29,  # Cost in $ per kg from https://www.lme.com/Metals/EV/Lithium-prices
    swu_cost=50,  # Cost on $ per kg based on typical Uranium SWU costs
    tails_cost=900,  # Assuming there is a market for depleted lithium where 10% discount has been applied.
)

print(f"minimal_enrichment_cost {minimal_enrichment_cost}")

print(f"tails_percent {tails_percent}")
