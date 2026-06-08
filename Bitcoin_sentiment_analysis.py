import pandas as pd

# Load the datasets
trader_df = pd.read_csv("D:/Bitcoin sentiment Analysis project/historical_data.csv")
fear_greed_df = pd.read_csv("D:/Bitcoin sentiment Analysis project/fear_greed.csv")

print("Trader Data Shape:", trader_df.shape)
print("Fear Greed Shape:", fear_greed_df.shape)

# first 5 rows
print(trader_df.head())

# column names and data types
print(trader_df.info())

# Basic statistics
print(trader_df.describe())

print(fear_greed_df.head())
print(fear_greed_df.info())

# Checking missing values
print("Trader Data - Missing Values:")
print(trader_df.isnull().sum())

print("\nFear Greed - Missing Values:")
print(fear_greed_df.isnull().sum())

# Checking duplicates
print("\nTrader Duplicates:", trader_df.duplicated().sum())
print("Fear Greed Duplicates:", fear_greed_df.duplicated().sum())

# Convert Timestamp IST to date (dayfirst=True, format is DD-MM-YYYY)
trader_df['date'] = pd.to_datetime(trader_df['Timestamp IST'], dayfirst=True).dt.date

# Convert fear_greed date column
fear_greed_df['date'] = pd.to_datetime(fear_greed_df['date']).dt.date

# Preview
print(trader_df['date'].head())
print(fear_greed_df['date'].head())

# Merge trader data with fear/greed on date
merged_df = pd.merge(trader_df, fear_greed_df[['date', 'value', 'classification']], 
                     on='date', how='inner')

# result
print("Merged Data Shape:", merged_df.shape)
print(merged_df.head())
print("\nSentiment Counts:")
print(merged_df['classification'].value_counts())

# Average Closed PnL by Sentiment
pnl_by_sentiment = merged_df.groupby('classification')['Closed PnL'].mean()
print("Average PnL by Sentiment:")
print(pnl_by_sentiment)

# Win rate by sentiment
merged_df['is_win'] = merged_df['Closed PnL'] > 0

win_rate = merged_df.groupby('classification')['is_win'].mean() * 100
print("Win Rate % by Sentiment:")
print(win_rate)

# Average trade size by sentiment
volume_by_sentiment = merged_df.groupby('classification')['Size USD'].mean()
print("Average Trade Size (USD) by Sentiment:")
print(volume_by_sentiment)

# Side distribution by sentiment
side_by_sentiment = merged_df.groupby(['classification', 'Side']).size().unstack()
print("Long vs Short by Sentiment:")
print(side_by_sentiment)

import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Chart 1: Average PnL by Sentiment
pnl_by_sentiment.sort_values().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average PnL by Market Sentiment')
plt.xlabel('Sentiment')
plt.ylabel('Average Closed PnL (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 2: Win Rate by Sentiment
win_rate.sort_values().plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Win Rate % by Market Sentiment')
plt.xlabel('Sentiment')
plt.ylabel('Win Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 3: Average Trade Size by Sentiment
volume_by_sentiment.sort_values().plot(kind='bar', color='salmon', edgecolor='black')
plt.title('Average Trade Size (USD) by Sentiment')
plt.xlabel('Sentiment')
plt.ylabel('Average Size USD')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 4: Buy vs Sell by Sentiment
side_by_sentiment.plot(kind='bar', color=['lightblue', 'salmon'], edgecolor='black')
plt.title('Buy vs Sell Count by Market Sentiment')
plt.xlabel('Sentiment')
plt.ylabel('Number of Trades')
plt.xticks(rotation=45)
plt.legend(['BUY', 'SELL'])
plt.tight_layout()
plt.show()

# Top 10 traders by total PnL
top_traders = merged_df.groupby('Account')['Closed PnL'].sum().sort_values(ascending=False).head(10)
print("Top 10 Traders by Total PnL:")
print(top_traders)

# Monthly PnL trend
merged_df['month'] = pd.to_datetime(merged_df['date']).dt.to_period('M')
monthly_pnl = merged_df.groupby('month')['Closed PnL'].mean()

monthly_pnl.plot(kind='line', color='blue', marker='o')
plt.title('Monthly Average PnL Trend')
plt.xlabel('Month')
plt.ylabel('Average PnL')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()