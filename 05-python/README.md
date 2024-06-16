# Create a stock plotter with Python

This folder focuses on creating a small self-contained Python script. The task is to create a Python script that reads stock data from a CSV file, plots the closing price over time, and saves the plot as a PNG image. The task is simple enough to validate it does what it is supposed to do.

## Folders
This folder contains the following subfolders:

- **Data:** The `data` folder includes some CSV files with historical stock data. You can add more stocks by going to NASDAQ website and downloading historical data. For example, for MSFT you can download the data from [here](https://www.nasdaq.com/market-activity/stocks/msft/historical?page=1&rows_per_page=10&timeline=y10), press the "Download" button, and save the file as CSV in the `data` folder. Remember to rename the file to `MSFT.csv`.
- **Output:** The script should save the resulting images in an `output` folder, which includes some previous examples. There is no need to keep them, they are just examples.
- **Past results:** Although this folder includes some complete examples inside the `past-results` folder, you should start from scratch. 


## Installation
For those who are not "[Pythonists](https://en.wiktionary.org/wiki/Pythonist)", here is a very basic step-by-step guide to install the required dependencies.

Make sure you have Python 3 installed. You can verify that by running the following command: `python3 --version`. If you don't have Python 3 installed, you can download it from the [official website](https://www.python.org/downloads/).


```bash
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

The dependencies should be based on the result of the AI. If the code requires other dependencies, include them into the `requirements.txt` file.

Once you created the virtual environment, installed the dependencies, and created the script. You should be able to run it with the following command:

```bash
python3 plot.py NVIDIA '2023-01-01' 600
```

## Prompting the GenAI

As with the other examples, be consistent with the prompt. Here is a prompt to get you started, but feel free to change it. 

```text
You are a Python developer. We need to create a stock plotter with Python. The task is to create a Python script that reads stock data from a CSV file, plots the closing price over time, and saves the plot as a PNG image. The CSV file contains a 'Date' column, a 'Close/Last' column with prices prefixed with a dollar sign, and a 'Volume' column. The 'Date' column is not sorted and the slicing operation on the DataFrame may cause issues. I want to:

- Load the file from the 'data' folder and parse the 'Date' column as dates.
- Remove the dollar sign from the 'Close/Last' prices and convert them to float. 
- Sort the DataFrame by date. 
- Add a subplot for the 'Volume' at the bottom of the image, which should be 1/10th the size of the price plot. 
- add some error handling to the script, such as checking if the file exists and if the columns are present.
- Save the resulting images in an 'output' folder. 
- The script also takes command line arguments for the stock quote name, start date, and number of days to plot.

could you create the code of this script? 
```

## Evaluation
It is common and expected to have an iterative process with the AI: work through the code, validate it, and then ask refinement questions until you are satisfied with the result. 

The evaluation of this task should be pretty straightforward. The script should create a PNG image with the stock. You should ask yourself:

- Does it produce an image with the closing price over time? 
- Compare the result with real data. For example, for APPLE stock, you could compare the resulting image with the plot from [Yahoo Finance Chart](https://finance.yahoo.com/quote/AAPL/chart/).
- Does the script handle errors correctly? For example, what happens if the file does not exist or the columns are not present? Does the script handle missing data correctly?
- Is the code clean and well-structured? Is it easy to read and understand?
- Which code assistant requires less steps to complete the task? 


## Follow-up tasks
As follow-up tasks, you could also ask the AI to:
- The volume should represent positive days in green and negative days in red. 
- Create a new script that compares two stocks in the same plot.
