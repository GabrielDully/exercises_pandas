'''
Read and Summarize Data:

Read a CSV file into a Pandas DataFrame.
Display the first few rows of the DataFrame using the head() method.
Use the info() method to display information about the DataFrame, such as the column names, data types, and non-null counts.
'''

import pandas as pd

def read_and_summarize_csv_data():
    
    df = pd.read_csv('example.csv')

    print(df.head())

    df.info()
