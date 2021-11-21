# lithium enrichment cost calculator

A Python package that is able to estimate the cost of lithium enrichment using a separative work approach.

<!-- This package is available in a convenient (web app)[]. -->

# Installation

```bash
pip install lithium-enrichment-cost-calculator
```

# Estimating the cost.

Required information

- Cost of input feed stock (```cost_feed```)

- Enrichment percent of input feed stock (```product_enrichment```) which defaults to be lithium natural abundance of isotopes (7.59% Li6 and 92.41% Li7).

- Amount of enriched product required (```product_amount```).

- Enrichment percent of lithium 6 required in the product (```product_enrichment```).

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
    product_enrichment=60,  # 60% is a typical HCPB blanket enrichment amount
    feed_cost=29,  #Cost in $ per kg from https://www.lme.com/Metals/EV/Lithium-prices
    swu_cost=50,  # Cost on $ per kg based on typical Uranium SWU costs
    tails_cost=900,  # Assuming there is a market for depleted lithium where 10% discount has been applied.
)

print(f'minimal_enrichment_cost {minimal_enrichment_cost} in $')
print('lithium 6 enrichment in tails at this optimal cost is {tails_percent} %')
```

# Useful resources

Separative work it well documented and explained elsewhere [1](http://web.mit.edu/22.812j/www/enrichment.pdf), [2](https://en.wikipedia.org/wiki/Separative_work_units), [3](https://www.world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/uranium-enrichment.aspx)
