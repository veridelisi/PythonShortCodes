import matplotlib.pyplot as plt
import seaborn as sns

# Given forward rates
F_1_1 = ((1 + r_2)**2 / (1 + r_1)**1 - 1) * 100
F_2_1 = ((1 + r_3)**3 / (1 + r_2)**2 - 1) * 100
F_1_2 = (((1 + r_3)**3 / (1 + r_1)**1) ** 0.5 - 1) * 100

# Create a Seaborn bar plot to visualize the forward rates
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

# Create a bar plot for forward rates
sns.barplot(x=['F(1,1)', 'F(1,2)', 'F(2,1)'], y=[F_1_1,  F_1_2, F_2_1])

# Customize the plot
plt.title('Forward Rates')
plt.ylabel('Forward Rate (%)')
plt.show()
