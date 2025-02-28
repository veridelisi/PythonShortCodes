import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the Tesla stock symbol
ticker = "TSLA"

# Define the date range
start_date = "2025-01-20"
end_date = "2025-02-28"

# Fetch historical stock data from Yahoo Finance
tesla_stock = yf.download(ticker, start=start_date, end=end_date)

# Check the available columns
print("Available columns:", tesla_stock.columns)

# Use 'Close' if 'Adj Close' is missing
if 'Adj Close' in tesla_stock.columns:
    tesla_stock = tesla_stock[['Adj Close']].rename(columns={'Adj Close': 'Tesla Stock Price'})
else:
    tesla_stock = tesla_stock[['Close']].rename(columns={'Close': 'Tesla Stock Price'})

# Plot Tesla's stock price over time
plt.figure(figsize=(10, 5))
plt.plot(tesla_stock.index, tesla_stock['Tesla Stock Price'], marker='o', linestyle='-', color='blue')
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title("Daily Tesla Stock Price (Jan 20 - Feb 28, 2025)")
plt.xticks(rotation=45)
plt.grid()
plt.show()
