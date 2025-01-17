# iloc: integer location function
# dataframe.iloc[row_ind, column]

# selecting a single element
###val = dataframe.iloc[row,column]
# selecting a specific row
###val = dataframe.iloc[row_index]
# selecting a multiple rows using slicing
###val = dataframe.iloc[start_row:end_row]
# selecting a row and a column
###val = dataframe.iloc[[row1, row2], [col1, col2]]
# selecting all rows of specified column
###val = dataframe.iloc[:, [col1, col2]]

#example
import pandas as pd
data= {"name": ['sharad', 'sanjay', 'piyush', 'dhanraj'],
       "age": [25, 30, 22, 28],
       "country": ["China", "United States", "Dubai", "Australia"]}
df = pd.DataFrame(data)
print(df)

# selecting 'United States'
element = df.iloc[1,2]
print(element)

# selecting a row and a column
subset = df.iloc[1:3, 0:2]
print(subset)
