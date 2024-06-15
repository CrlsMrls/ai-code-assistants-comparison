# Create a stock plotter with Python

## Installation

```bash
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python plot.py NVIDIA '2023-01-01' 600
```

## Add more stocks

You can add more stocks to the `data` folder. Go to NASDAQ website and download the historical data of the stock you want to add. For example, for MSFT you can download the data from [here](https://www.nasdaq.com/market-activity/stocks/msft/historical?page=1&rows_per_page=10&timeline=y10).


## Prompting the GenAI

I have a Python script that reads stock data from a CSV file, plots the closing price over time, and saves the plot as a PNG image. The CSV file contains a 'Date' column, a 'Close/Last' column with prices prefixed with a dollar sign, and a 'Volume' column. The 'Date' column is not sorted and the slicing operation on the DataFrame is causing issues. I want to:

- Load the file from the 'data' folder and parse the 'Date' column as dates.
- Remove the dollar sign from the 'Close/Last' prices and convert them to float. 
- Sort the DataFrame by date. 
- Add a subplot for the 'Volume' at the bottom of the image, which should be 1/10th the size of the price plot. 
- add some error handling to the script, such as checking if the file exists and if the columns are present.
- Save the resulting images in an 'output' folder. 
- The script also takes command line arguments for the stock quote name, start date, and number of days to plot.

could you create the code of this program?