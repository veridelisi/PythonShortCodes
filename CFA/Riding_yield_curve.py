# Initial spot rates
S1 = 0.04  # 4%
S2 = 0.06  # 6%

# Calculate bond prices
price_1_year_bond = 100 / (1 + S1)
price_2_year_bond = 100 / (1 + S2)**2

# Price of 1-year bond: $96.15
# Price of 2-year bond: $89.00

# Calculate forward rate F(1,1)
forward_rate_1_1= ((((1 + S2)**2) /(1 + S1))-1)*100

# forward_rate_1_1 0.08  # 8%



# Scenario 1: Spot rate in one year matches the one-year forward rate_1_1 (8%)
spot_rate_year_1 = 0.08  # 8%
price_2_year_bond_year_1 = 100 / (1 + spot_rate_year_1)
profit_scenario_1 = (price_2_year_bond_year_1 - price_2_year_bond) / price_2_year_bond

# Scenario 2: Spot rate in one year is lower than the one-year forward rate (7%)
spot_rate_year_1_lower = 0.07  # 7%
price_2_year_bond_year_1_lower = 100 / (1 + spot_rate_year_1_lower)
profit_scenario_2 = (price_2_year_bond_year_1_lower - price_2_year_bond) / price_2_year_bond

# Scenario 3: Spot rate in one year is lower than the one-year forward rate (9%)
spot_rate_year_1_higher = 0.09  # 9%
price_2_year_bond_year_1_higher = 100 / (1 + spot_rate_year_1_higher)
profit_scenario_3 = (price_2_year_bond_year_1_higher - price_2_year_bond) / price_2_year_bond

# Print the results
print(f"Price of 1-year bond: ${price_1_year_bond:.2f}")
print(f"forward_rate_1_1: %{forward_rate_1_1:.2f}")
print(f"Price of 2-year bond: ${price_2_year_bond:.2f}")
print(f"Scenario 1 Profit: {profit_scenario_1*100:.2f}%")
print(f"Scenario 2 Profit: {profit_scenario_2*100:.2f}%")
print(f"Scenario 3 Profit: {profit_scenario_3*100:.2f}%")


import matplotlib.pyplot as plt
import seaborn as sns

# Define the spot rates and corresponding profits
spot_rates = [spot_rate_year_1_lower, spot_rate_year_1, spot_rate_year_1_higher]
profits = [profit_scenario_2, profit_scenario_1, profit_scenario_3]

# Create a timeline plot using Seaborn without grid lines
sns.set_theme(style="darkgrid")
plt.figure(figsize=(10, 6))
ax = sns.lineplot(x=spot_rates, y=[profit*100 for profit in profits], marker='o', dashes=False)  # Remove grid lines
ax.set(xlabel='Spot Rate in 1 Year', ylabel='Profit (%)', title='Bond Profit Over Different Spot Rates')
plt.xticks(spot_rates, [f'{rate*100:.2f}%' for rate in spot_rates])

# Display the line plot
plt.show()
