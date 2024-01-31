# Spot rate curve data
spot_rates = {
    1: 0.02, # 2%
    2: 0.04, # 4%
    3: 0.06, # 6%
    4: 0.07  # 7%
}

# Function to calculate swap rate
def calculate_swap_rate(T, spot_rates):
    numerator = 0
    denominator = 0
    
    for t in range(1, T + 1):
        discount_factor = 1 / ((1 + spot_rates[t]) ** t)
        denominator += discount_factor
    
    numerator = 1 - (1 / ((1 + spot_rates[T]) ** T))
    
    swap_rate = (numerator / denominator)*100
    
    return swap_rate

# Calculate swap rates for each maturity
swap_rates = {}
for T in range(1, 5):
    swap_rates[T] = calculate_swap_rate(T, spot_rates)

swap_rates
