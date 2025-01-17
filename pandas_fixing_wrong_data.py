# Wrong Data: It doesn't mean wrong format but wrongly fed data by humans.

import pandas as pd
df = pd.read_csv('dirtydata.csv')
print(df.to_string())

# Data Entry in 'Duration' column at index '7; is wrongly fed asper rest of the data
# We have to set it manually since it is a typo error

# Setting 450 in 'Duration' column in 7th row to 45
df.loc[7, 'Duration'] = 45
print(df.to_string())
#this works in smaller dataset

# For larger dataset, loop through all values in 'Duration' column
# If value is higher then 60 then set it to 60
# Define such rules
df = pd.read_csv('dirtydata.csv')
for i in df.index:
    if df.loc[i, 'Duration'] > 60:
        df.loc[i, 'Duration'] = 61
print(df.to_string())

# We can also remove the rows for wrong data in larger datasets
df = pd.read_csv('dirtydata.csv')
for i in df.index:
    if df.loc[i, 'Duration'] > 60:
        df.drop(i, inplace=True)
print(df.to_string())

