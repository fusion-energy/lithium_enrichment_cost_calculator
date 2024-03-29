[![CI with install](https://github.com/fusion-energy/lithium_enrichment_cost_calculator/actions/workflows/ci_with_install.yml/badge.svg)](https://github.com/fusion-energy/lithium_enrichment_cost_calculator/actions/workflows/ci_with_install.yml)

[![Upload Python Package](https://github.com/fusion-energy/lithium_enrichment_cost_calculator/actions/workflows/python-publish.yml/badge.svg)](https://github.com/fusion-energy/lithium_enrichment_cost_calculator/actions/workflows/python-publish.yml)

A Python package that is able to estimate the cost of lithium enrichment using a separative work approach.

<!-- This package is available in a convenient (web app)[]. -->

# Installation

```bash
pip install lithium-enrichment-cost-calculator
```

# Estimating the cost.

Required information

- Cost of input feed stock (```cost_feed```)

- Enrichment percent of input feed stock (```product_enrichment_fraction```) which defaults to be lithium natural abundance of isotopes (7.59% Li6 and 92.41% Li7).

- Amount of enriched product required (```product_amount```).

- Enrichment percent of lithium 6 required in the product (```product_enrichment_fraction```).

- Resale value of the depleted tails (```cost_tails```).

- Cost per separative work unit (```swu_cost```)

Once these inputs are specified then the cost of enrichment will be calculated and returned along with the optimal Li6 depletion level in the tails using the ```find_minimal_cost_of_enrichment()``` function.

The depletion level in the tails is automatically optimized to reduce the total overall costs of the enrichment process. However the cost at a specific tails depletion percent can also be calculated using the ```find_cost_of_enrichment()``` function.

# Usage examples

Find the minimal cost of lithium enrichment and the corresponding tails depletion.
```python
import lithium_enrichment_cost_calculator as lecc

minimal_enrichment_cost, tails_percent = lecc.find_minimal_cost_of_enrichment(
    product_amount=1000,  # 1000kg of enriched lithium
    product_enrichment_fraction=0.6,  # 60% is a typical HCPB blanket enrichment amount
    feed_cost=29,  #Cost in $ per kg from https://www.lme.com/Metals/EV/Lithium-prices
    swu_cost=50,  # Cost on $ per kg based on typical Uranium SWU costs
    tails_cost=900,  # Assuming there is a market for depleted lithium where 10% discount has been applied.
)

print(f'minimal_enrichment_cost {minimal_enrichment_cost} in $')
print(f'lithium 6 enrichment in tails at this optimal cost is {tails_percent} %')
```

The tails can be depleted to a lesser or greater amount to optimise the cost of the process. It is possible to achieve the required amount of product at the required enrichment in numerous ways. At the two extremes one could:
- highly depleted the tails and produce a small amount of tails
- mildly depleted the tails and produce a large amount of tails

The most cost effective solution depends on the relative cost of Separate Work Units compared to the cost of the feed (```feed_cost```) and any resale value for the tails (```tails_cost```). A basic cost optimiser has been built into this package to
demonstrate the difference that the depletion level in the tails can make to the overall cost.
```python
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

```

# Useful resources

Separative work it well documented and explained elsewhere [1](http://web.mit.edu/22.812j/www/enrichment.pdf), [2](https://en.wikipedia.org/wiki/Separative_work_units), [3](https://www.world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/uranium-enrichment.aspx)
