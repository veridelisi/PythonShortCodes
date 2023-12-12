import pandas as pd

# Set up the variables
spot_rates = {
    1: 0.055,
    2: 0.06,
    3: 0.0625,
    4: 0.065,
    5: 0.07,
}

notional_principal = 10000000  # $10,000,000

# Calculate discount factors
discount_factors = [(1 / (1 + spot_rates[i]) ** i) for i in range(1, 6)]

# Calculate forward rates as specified
forward_rates = [(discount_factors[i] / discount_factors[i + 1]) - 1 for i in range(4)]
forward_rates = [rate * 100 for rate in forward_rates]  # Convert to percentage

# Create a DataFrame to display the results
result_table = pd.DataFrame(index=range(1, 6))
result_table.index.name = 'Year'
result_table['Spot Rate'] = [spot_rates[i] for i in range(1, 6)]
result_table['Discount Factor'] = discount_factors

# Correct forward rate calculation for each year
result_table['Forward Rate'] = [spot_rates[1] * 100] + forward_rates

# Calculate floating payments for each year and round down
result_table['Floating Payment'] = [int(notional_principal * (forward_rate / 100)) for forward_rate in result_table['Forward Rate']]

# Display the results
print(result_table)
