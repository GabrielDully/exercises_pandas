'''
Data Selection and Filtering:

Select a single column from the DataFrame using square brackets or dot notation.
Filter the DataFrame to include only rows that meet a specific condition, such as values greater than a certain threshold.
'''

import pandas as pd

def data_selection_and_filtering():
    
    df = pd.read_csv('example.csv')

    print(df['Index'])
    print(df.Website)

    print(df[df['Index'] > 95])
