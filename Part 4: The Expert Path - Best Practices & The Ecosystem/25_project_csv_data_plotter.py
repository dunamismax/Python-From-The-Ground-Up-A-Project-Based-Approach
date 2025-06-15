# -*- coding: utf-8 -*-
"""
Part 4, Lesson 25: Project: CSV Data Plotter

Author: dunamismax
Date: 06-15-2025

This file is a project that reads numerical data from a CSV file and
uses the `matplotlib` library to create a simple line chart, introducing
the basics of data visualization in Python.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to your final project for the Expert Path! We've learned how to handle
files, manage dependencies, and scrape the web. Now, we'll tackle a cornerstone
of data analysis and data science: DATA VISUALIZATION.

Raw data, like a table of numbers, can be hard to interpret. A chart or graph
can reveal trends, patterns, and insights in an instant.

THE DATA SOURCE: CSV FILES
CSV (Comma-Separated Values) is one of the most common formats for storing tabular
data. It's a simple text file where each line is a row, and columns are separated
by commas. Python's built-in `csv` module makes it easy to read these files.

THE PLOTTING TOOL: MATPLOTLIB
To create charts, we'll use MATPLOTLIB, the most widely used and foundational
data visualization library in the Python ecosystem. It's incredibly powerful,
allowing you to create everything from simple line charts to complex 3D plots.

This project will teach you to build a simple data pipeline:
Read Data (from CSV) -> Process Data (in Python) -> Visualize Data (with Matplotlib)

--- SETUP: THIS PROJECT REQUIRES `matplotlib` ---

Follow the professional workflow we've learned:

1.  Create a new project folder and navigate into it:
    `mkdir data_plotter_project && cd data_plotter_project`

2.  Create and activate a virtual environment:
    `python -m venv venv`
    `source venv/bin/activate` (or `.\\venv\\Scripts\\activate` on Windows)

3.  Install the `matplotlib` package:
    `pip install matplotlib`

4.  Save your dependencies:
    `pip freeze > requirements.txt`

5.  Now, create this Python file (`25_project_csv_data_plotter.py`) and the
    data file described below inside your project folder.
'''

# We need the `csv` module to read the data file.
import csv
# We import the `pyplot` interface from `matplotlib` and give it the
# conventional alias `plt`.
import matplotlib.pyplot as plt


# --- Part 1: The Data File ---
#
# Before we can plot anything, we need data. Create a new file in the SAME
# directory as this script and name it `sample_sales_data.csv`.
#
# Copy and paste the following content into that file exactly as it appears:
#
# Month,Revenue,Profit
# January,10000,2000
# February,11500,2500
# March,13000,3000
# April,12000,2800
# May,14000,3500
# June,15500,4000
# July,16000,4200
# August,15000,3900
# September,17000,4500
# October,18500,5000
# November,20000,5500
# December,22000,6000
#

# The main execution block starts here.
if __name__ == "__main__":
    
    # --- Part 2: Reading and Processing the CSV Data ---
    print("--- Reading data from CSV file ---")
    
    # We will store our columns of data in these lists.
    months = []
    revenues = []
    profits = []
    
    file_path = 'sample_sales_data.csv'

    try:
        # We open the file using a `with` statement.
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            # `csv.reader` creates a reader object that lets us iterate over
            # lines in the CSV, and it automatically handles splitting the
            # columns for us.
            csv_reader = csv.reader(csv_file)
            
            # The first row is the header. We want to skip it.
            # The `next()` function retrieves the next item from an iterator.
            header = next(csv_reader)
            print(f"CSV Header: {header}")
            
            # Now, we loop over the remaining rows in the file.
            for row in csv_reader:
                # Each `row` is a list of strings, e.g., ['January', '10000', '2000']
                # We append the month to our list.
                months.append(row[0])
                
                # IMPORTANT: Data from files is read as STRINGS. To do math or
                # plot them as numbers, we MUST convert them.
                # We use int() to convert the revenue and profit strings to integers.
                revenues.append(int(row[1]))
                profits.append(int(row[2]))

        print("Successfully read and processed data.")
        # print(f"Months: {months}")
        # print(f"Revenues: {revenues}")
        # print(f"Profits: {profits}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print("Please make sure you have created the file and it's in the correct directory.")
        exit() # Exit the script if the data file is missing.
    except (ValueError, IndexError) as e:
        print(f"Error processing data in the CSV file: {e}")
        print("Please ensure the CSV is formatted correctly (Month,Number,Number).")
        exit()


    # --- Part 3: Creating the Plot with Matplotlib ---
    if months: # Only try to plot if we successfully loaded data.
        print("\n--- Generating plot with Matplotlib ---")
        
        # Create a PLOT. The `plt.plot()` function is the most basic.
        # It takes x-values (months) and y-values (revenues/profits).
        plt.plot(months, revenues, label='Revenue', marker='o') # 'marker' adds dots
        plt.plot(months, profits, label='Profit', marker='x')  # Plot a second line
        
        # Add labels and a title to make the chart understandable.
        plt.title('Monthly Revenue and Profit')
        plt.xlabel('Month')
        plt.ylabel('Amount (USD)')
        
        # `xticks` can be used to rotate labels if they overlap.
        plt.xticks(rotation=45)
        
        # A LEGEND is a key that explains what each line represents.
        # It uses the `label` we provided in the `plot()` calls.
        plt.legend()
        
        # A GRID can make the chart easier to read.
        plt.grid(True)
        
        # Ensures all elements fit nicely within the figure window.
        plt.tight_layout()
        
        # `plt.show()` displays the plot in a new window. The script will
        # pause here until you close that window.
        plt.show()
        
        print("Plot window closed. Program finished.")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

Congratulations! You have successfully built a program that reads structured
data from a file, processes it, and creates a professional-looking visualization.
This is a foundational skill in any data-related field.

Key Concepts Learned:
1.  CSV (Comma-Separated Values) is a standard file format for tabular data.
2.  Python's built-in `csv` module simplifies reading and parsing CSV files.
3.  MATPLOTLIB is the go-to library for data visualization in Python. We use its
    `pyplot` interface (as `plt`).
4.  Data from files must often be converted to the correct type (e.g., `int()`)
    before it can be used for calculations or plotting.
5.  A good plot includes a TITLE, axis LABELS (`xlabel`, `ylabel`), and a
    LEGEND to be clear and informative.
6.  `plt.show()` is the command that actually displays the generated chart.

This project caps off the Expert Path, tying together file I/O, dependency
management, and interaction with a major third-party library.

HOW TO RUN THIS CODE:

1.  Follow the setup instructions at the top of the file to create a folder,
    a virtual environment, and `pip install matplotlib`.
2.  Create the `sample_sales_data.csv` file in the same directory and paste the
    provided data into it.
3.  Save this script as `25_project_csv_data_plotter.py`.
4.  With your virtual environment active, run the script from your terminal:
    `python 25_project_csv_data_plotter.py`
5.  A new window should appear displaying your line chart. Close the window to
    end the program.
'''