#Chaikin Volatility is a technical analysis indicator used to measure the volatility of a stock's price over time.
def get_latest_price(ticker):
    """Get the latest price for the given ticker."""
    data = yf.Ticker(ticker)
    return data.history(period='1d')['Close'].iloc[-1]

def get_latest_time():
    """Get the current time."""
    return datetime.now().strftime('%H:%M:%S')

# Set the ticker symbol
ticker = "AGIX-USD"

# Get the latest price and time
latest_price = get_latest_price(ticker)
latest_time = get_latest_time()

# Display the latest price and time
print("Latest Price:", latest_price)
print("Latest Time:", latest_time)

#

import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta
import time

def get_data(ticker):
    """Fetch latest 60 days of closing price data for given ticker and update with the latest available close."""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=60)  # Adjust range as needed
    data = yf.download(ticker, start=start_date, end=end_date)
    return data['Close']

def plot_data(data, ticker):
    """Plot the data with an interactive range slider."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data, name='Close'))

    # Set layout options
    fig.update_layout(
        title=f'{ticker} Closing Price',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=True,  # Enable range slider
        xaxis=dict(
            
            type='date'
        )
    )

    fig.show()

# Main loop to continuously update the plot
ticker = "AGIX-USD"
while True:
    data = get_data(ticker)
    plot_data(data, ticker)
    time.sleep(300)  # Update every 5 minutes

#
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from datetime import datetime

def download_stock_data(tickers, start_date, end_date):
    """Download stock data for given tickers between specified dates."""
    return yf.download(tickers, start=start_date, end=end_date)

def calculate_true_range(data):
    """Calculate the True Range (TR) for ATR calculation."""
    return np.maximum.reduce([
        data['High'] - data['Low'],
        abs(data['High'] - data['Close'].shift()),
        abs(data['Low'] - data['Close'].shift())
    ])

def calculate_indicators(data, window_size):
    """Calculate the Average True Range (ATR), highest high, lowest low, and Choppiness Index."""
    data['TR'] = calculate_true_range(data)
    data['ATR'] = data['TR'].rolling(window=window_size).mean()
    data['highestHigh'] = data['High'].rolling(window=window_size).max()
    data['lowestLow'] = data['Low'].rolling(window=window_size).min()
    data['Sum_TR'] = data['TR'].rolling(window=window_size).sum()
    data['Range'] = data['highestHigh'] - data['lowestLow']
    data['CHOP'] = 100 * np.log10(data['Sum_TR'] / data['Range']) / np.log10(window_size)
    data['CHOP'] = data['CHOP'].clip(lower=0, upper=100)

def generate_signals(data):
    """Generate buy and sell signals based on the Choppiness Index."""
    data['CHOP_lag1'] = data['CHOP'].shift()
    data['signal'] = np.where((data['CHOP'] < 30) & (data['CHOP_lag1'] >= 30), 'Buy Signal',
                              np.where((data['CHOP'] > 60) & (data['CHOP_lag1'] <= 60), 'Sell Signal', 'Neutral'))

def plot_data(data, ticker):
    """Visualize stock price and signals with an interactive range slider using Plotly."""
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02, subplot_titles=(f"{ticker} Closing Price", f"{ticker} Choppiness Index"))
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Closing Price', line=dict(color='blue')), row=1, col=1)
    buy_signals = data[data['signal'] == 'Buy Signal']
    sell_signals = data[data['signal'] == 'Sell Signal']
    fig.add_trace(go.Scatter(x=buy_signals.index, y=buy_signals['Close'], mode='markers', name='Potential Buy Signal', marker=dict(color='green', size=10, symbol='triangle-up')), row=1, col=1)
    fig.add_trace(go.Scatter(x=sell_signals.index, y=sell_signals['Close'], mode='markers', name='Potential Sell Signal', marker=dict(color='red', size=10, symbol='triangle-down')), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['CHOP'], name='Choppiness Index', line=dict(color='purple')), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=[60]*len(data), name='Sell Threshold', line=dict(color='red', dash='dash')), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=[30]*len(data), name='Buy Threshold', line=dict(color='green', dash='dash')), row=2, col=1)
    # Update layout to add the range slider below the second subplot
    fig.update_layout(
        xaxis=dict(
            # Disable range slider for the first x-axis (top subplot)
            rangeslider=dict(visible=False),
        ),
        xaxis2=dict(
            # Enable range slider for the second x-axis (bottom subplot)
            rangeslider=dict(visible=True),
            type='date',
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label='1m', step='month', stepmode='backward'),
                    dict(count=6, label='6m', step='month', stepmode='backward'),
                    dict(step='all')
                ])
            ),
        ),
        # Adjust height if necessary
        height=800
    )
    
    fig.show()

# Execute Functions
tickers = "AGIX-USD"
start_date = "2018-01-01"
end_date = datetime.today().strftime('%Y-%m-%d')
data = download_stock_data(tickers, start_date=start_date, end_date=end_date)
window_size = 14
calculate_indicators(data, window_size)
generate_signals(data)
plot_data(data, tickers)


