import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec

def main(stock_quote, start_date, num_days):
  # Check if file exists
  file_path = f'data/{stock_quote}.csv'
  if not os.path.exists(file_path):
    print(f"File {file_path} does not exist.")
    return

  # Load the CSV file and parse 'Date' column as dates
  df = pd.read_csv(file_path, parse_dates=['Date'])

  # Check if required columns are present
  required_columns = ['Date', 'Close/Last', 'Volume']
  if not all(column in df.columns for column in required_columns):
    print("Required columns are missing from the CSV file.")
    return

  # Remove the dollar sign from the 'Close/Last' prices and convert them to float
  df['Close/Last'] = df['Close/Last'].replace({r'\$': ''}, regex=True).astype(float)

  # Sort the DataFrame by date
  df = df.sort_values('Date')

  # Filter data based on start_date and num_days
  df = df[(df['Date'] >= start_date) & (df['Date'] < start_date + pd.Timedelta(days=num_days))]

  # Create subplots
  fig = plt.figure(figsize=(10, 8))
  gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1]) 
  ax0 = plt.subplot(gs[0])
  ax1 = plt.subplot(gs[1], sharex = ax0)

  # Plot 'Close/Last' prices
  ax0.plot(df['Date'], df['Close/Last'], label='Close/Last')
  ax0.legend()

  # Plot 'Volume'
  ax1.bar(df['Date'], df['Volume'], label='Volume')
  ax1.legend()

  # Save the resulting image in an 'output' folder
  os.makedirs('output', exist_ok=True)
  plt.savefig(f'output/{stock_quote}.png')

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Plot stock data.')
  parser.add_argument('stock_quote', type=str, help='Stock quote name')
  parser.add_argument('start_date', type=pd.to_datetime, help='Start date in YYYY-MM-DD format')
  parser.add_argument('num_days', type=int, help='Number of days to plot')
  args = parser.parse_args()

  main(args.stock_quote, args.start_date, args.num_days)