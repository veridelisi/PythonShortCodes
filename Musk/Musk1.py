import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file (Ensure the correct file path is used in Colab)
file_path = "x_elonmusk_2025-01-20.xlsx"  # Update this with your actual file path

# Load the Excel file
df = pd.read_excel(file_path)

# Display the first few rows
df.head()

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date']).dt.date  # Extract only the date (without time)

# Group by date to get daily counts
daily_data = df.groupby('Date').agg({
    'Content': 'count',  # Number of tweets per day
    'Retweet Count': 'sum',  # Total retweets per day
    'Comment Count': 'sum'  # Total comments per day
}).rename(columns={'Content': 'Total Tweets'})

# Plot Total Tweets per Day
plt.figure(figsize=(10, 5))
plt.plot(daily_data.index, daily_data['Total Tweets'], marker='o', linestyle='-')
plt.xlabel("Date")
plt.ylabel("Total Tweets")
plt.title("Daily Tweets by Elon Musk")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Plot Total Retweets per Day
plt.figure(figsize=(10, 5))
plt.plot(daily_data.index, daily_data['Retweet Count'], marker='o', linestyle='-', color='red')
plt.xlabel("Date")
plt.ylabel("Total Retweets")
plt.title("Daily Retweets on Elon Musk's Tweets")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Plot Total Comments per Day
plt.figure(figsize=(10, 5))
plt.plot(daily_data.index, daily_data['Comment Count'], marker='o', linestyle='-', color='green')
plt.xlabel("Date")
plt.ylabel("Total Comments")
plt.title("Daily Comments on Elon Musk's Tweets")
plt.xticks(rotation=45)
plt.grid()
plt.show()
