'''
Data Manipulation:

Add a new column to the DataFrame by performing arithmetic operations on existing columns.
Rename one or more columns in the DataFrame using the rename() method.
'''

import pandas as pd

df = pd.DataFrame(
    {
        'column_1': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'column_2': [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],
        'column_3': [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    }
)

df['addition'] = df['column_1'] + df['column_2']

df.rename(columns=
    {
        'column_1': 'natural',
        'column_2': 'even',
        'column_3': 'integer',
        'addition': 'total'
    },
    inplace = True
)

print(df.info())