import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sys
import os

def plot_stock(quote_name, start_date, num_days):
  # Check if file exists
  if not os.path.isfile(f'data/{quote_name}.csv'):
    print(f"File 'data/{quote_name}.csv' does not exist.")
    return

  # Check if num_days is positive
  if num_days <= 0:
    print("Number of days must be positive.")
    return

  

  try:
    # Read the CSV file
    df = pd.read_csv(f'data/{quote_name}.csv')
    
    # Convert 'Date' to datetime and set as index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    # Sort the DataFrame by the index
    df.sort_index(inplace=True)
    
    # Remove dollar sign from 'Close/Last' and convert to float
    df['Close/Last'] = df['Close/Last'].replace({r'\$': ''}, regex=True).astype(float)
    
    # Slice the DataFrame
    df = df.loc[start_date:].iloc[:num_days]
    
    # Create subplots with different sizes
    fig = plt.figure(figsize=(1052/72, 1052/72), dpi=72)
    gs = gridspec.GridSpec(10, 1)
    ax1 = plt.subplot(gs[:9])
    ax2 = plt.subplot(gs[9:], sharex=ax1)
    
    # Plot the 'Close/Last' column
    ax1.plot(df['Close/Last'])
    
    # Plot the 'Volume' column
    ax2.bar(df.index, df['Volume'], width=0.5)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Create 'output' directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # Save the plot in the 'output' folder
    plt.savefig(f'output/{quote_name}.png')
  except Exception as e:
    print(f"An error occurred: {e}")

# Check number of arguments
if len(sys.argv) != 4:
  print("Usage: python script_name.py QUOTE_NAME START_DATE NUM_DAYS")
else:
  # Command line arguments
  quote_name = sys.argv[1]
  start_date = sys.argv[2]
  num_days = int(sys.argv[3])

  plot_stock(quote_name, start_date, num_days)