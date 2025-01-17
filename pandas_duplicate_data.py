import pandas as pd
df = pd.read_csv('dirtydata.csv')
print(df.to_string())

# Finding duplicate data
print(df.duplicated()) #returns true for duplicate rows else false

# Removing duplicate rows
print(df.drop_duplicates(inplace=True)) #keeps one of the duplicates aand deleted others
print(df.to_string())

