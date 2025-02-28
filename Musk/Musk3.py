# Import libraries
import pandas as pd
import numpy as np
from statsmodels.tsa.vector_ar.var_model import VAR
import matplotlib.pyplot as plt
from google.colab import files

# Step 1: Load the Excel file
file_path = "x_elonmusk_2025-01-20.xlsx"  # Update if the file name is different
df = pd.read_excel(file_path)

# Step 2: Convert 'Date' to datetime and extract just the date
df['Date'] = pd.to_datetime(df['Date']).dt.date

# Step 3: Group by date to get daily totals
daily_data = df.groupby('Date').agg({
    'Content': 'count',          # Total Tweets
    'Retweet Count': 'sum',      # Total Retweets
    'Comment Count': 'sum'       # Total Comments
}).rename(columns={'Content': 'Total Tweets'})

# Step 4: Add real Tesla stock prices
stock_prices_dict = {
    '2025-01-21': 424.070007, '2025-01-22': 415.109985, '2025-01-23': 412.380005,
    '2025-01-24': 406.579987, '2025-01-27': 397.149994, '2025-01-28': 398.089996,
    '2025-01-29': 389.100006, '2025-01-30': 400.279999, '2025-01-31': 404.600006,
    '2025-02-03': 383.679993, '2025-02-04': 392.209991, '2025-02-05': 378.170013,
    '2025-02-06': 374.320007, '2025-02-07': 361.619995, '2025-02-10': 350.730011,
    '2025-02-11': 328.500000, '2025-02-12': 336.510010, '2025-02-13': 355.940002,
    '2025-02-14': 355.839996, '2025-02-18': 354.109985, '2025-02-19': 360.559998,
    '2025-02-20': 354.399994, '2025-02-21': 337.799988, '2025-02-24': 330.529999,
    '2025-02-25': 302.799988, '2025-02-26': 290.799988, '2025-02-27': 281.950012
}

# Create stock price DataFrame
price_df = pd.DataFrame(list(stock_prices_dict.items()), columns=['Date', 'Tesla Stock Price'])
price_df['Date'] = pd.to_datetime(price_df['Date']).dt.date

# Estimate Jan 20 and Feb 28
extra_dates = pd.DataFrame({
    'Date': [pd.to_datetime('2025-01-20').date(), pd.to_datetime('2025-02-28').date()],
    'Tesla Stock Price': [424.07, 281.95]  # Jan 20 = same as Jan 21, Feb 28 = same as Feb 27
})
price_df = pd.concat([price_df, extra_dates], ignore_index=True)

# Step 5: Merge tweet data with stock prices
final_data = daily_data.merge(price_df, on='Date', how='left')
final_data['Tesla Stock Price'] = final_data['Tesla Stock Price'].fillna(method='ffill')

# Ensure data is sorted by date
final_data = final_data.sort_values('Date')

# Step 6: Time Series Plots
plt.figure(figsize=(12, 6))

# Plot Tesla Stock Price
plt.plot(final_data['Date'], final_data['Tesla Stock Price'], label='Tesla Stock Price', color='blue')
plt.title('Tesla Stock Price Over Time (Jan 20 - Feb 28, 2025)')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Plot Tweet Metrics (scaled for visibility)
plt.figure(figsize=(12, 6))
plt.plot(final_data['Date'], final_data['Total Tweets'], label='Total Tweets', color='green')
plt.plot(final_data['Date'], final_data['Retweet Count'] / 1000000, label='Retweet Count (Millions)', color='orange')
plt.plot(final_data['Date'], final_data['Comment Count'] / 1000, label='Comment Count (Thousands)', color='red')
plt.title('Tweet Metrics Over Time (Jan 20 - Feb 28, 2025)')
plt.xlabel('Date')
plt.ylabel('Count (Scaled)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Step 7: Scatter Plots to Check Relationships
plt.figure(figsize=(15, 5))

# Scatter: Total Tweets vs Stock Price
plt.subplot(1, 3, 1)
plt.scatter(final_data['Total Tweets'], final_data['Tesla Stock Price'], color='green')
plt.title('Total Tweets vs Tesla Stock Price')
plt.xlabel('Total Tweets')
plt.ylabel('Stock Price (USD)')

# Scatter: Retweet Count vs Stock Price (scaled)
plt.subplot(1, 3, 2)
plt.scatter(final_data['Retweet Count'] / 1000000, final_data['Tesla Stock Price'], color='orange')
plt.title('Retweet Count (Millions) vs Tesla Stock Price')
plt.xlabel('Retweet Count (Millions)')
plt.ylabel('Stock Price (USD)')

# Scatter: Comment Count vs Stock Price (scaled)
plt.subplot(1, 3, 3)
plt.scatter(final_data['Comment Count'] / 1000, final_data['Tesla Stock Price'], color='red')
plt.title('Comment Count (Thousands) vs Tesla Stock Price')
plt.xlabel('Comment Count (Thousands)')
plt.ylabel('Stock Price (USD)')

plt.tight_layout()
plt.show()

# Step 8: VAR Analysis
# Select variables for VAR
var_data = final_data[['Total Tweets', 'Retweet Count', 'Comment Count', 'Tesla Stock Price']]

# Check for stationarity (using simple differencing for this example)
# In practice, you might need to use Augmented Dickey-Fuller (ADF) test
var_data_diff = var_data.diff().dropna()

# Fit VAR model (using lag 1 as an example; you can adjust based on information criteria)
model = VAR(var_data_diff)
results = model.fit(maxlags=1, ic='aic')

# Step 9: Show VAR results
print("\nVAR Results Summary:")
print(results.summary())
