# data in a wrong format: remove all rows with wrong format or convert all cells in column to same format

import pandas as pd
df = pd.read_csv('dirtydata.csv')

# Converting all cells in date column to dates using to_datatime()
df["Date"] = pd.to_datetime(df['Date'], format='mixed') #use format='mixed' so as to fetch all the data present present in diffrent formats, to be worked upon
print(df.to_string())
#NaN is converted to NaT that means Not a Time

# Removing rows with null values in 'Date' column and changing wrong format to correct one
df = pd.read_csv('dirtydata.csv')
df["Date"] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset = ['Date'], inplace=True)
print(df.to_string())

