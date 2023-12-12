import pandas as pd

# Set up the variables
spot_rates = {
    1: 0.055,
    2: 0.06,
    3: 0.0625,
    4: 0.065,
    5: 0.07,
}

# Calculate discount factors using the correct formula
discount_factors = [(1 / (1 + spot_rates[i]) ** i) for i in range(1, 6)]

# Create a DataFrame to display the correct discount factors
discount_factors_table = pd.DataFrame(index=range(1, 6))
discount_factors_table.index.name = 'Year'
discount_factors_table['Spot Rate'] = [spot_rates[i] for i in range(1, 6)]
discount_factors_table['Discount Factor'] = discount_factors

# Display the results
print(discount_factors_table)
