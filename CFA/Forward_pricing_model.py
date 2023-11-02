import matplotlib.pyplot as plt
import seaborn as sns

# Given spot rates
r_1 = 0.07  # 7%
r_3 = 0.09  # 9%

# Calculate discount factors
P_1 = 1 / (1 + r_1)
P_3 = 1 / (1 + r_3)**3

# Calculate the correct forward price of a two-year bond to be issued in one year
F_1_2 = P_3 / P_1

# Create a Seaborn bar plot to visualize the discount factors
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

# Create a bar plot for discount factors
sns.barplot(x=['1-Year Discount Factor', '3-Year Discount Factor'], y=[P_1, P_3])

# Customize the plot
plt.title('Discount Factors')
plt.ylabel('Discount Factor (P)')
plt.show()

# Print the corrected forward price
print(f"The forward price of a two-year bond to be issued in one year is: {F_1_2:.2f}")
