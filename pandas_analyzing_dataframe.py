#Viewing the data: one of the most used method for a quick overview of dataframe is the head() method. It returns the headers and a specified no. of rows.

#Printing first 10 rows in dataframe
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(10))
print(df.head())
#it is same as print(df) i.e by default takes 5 as argument and displays first 5 rows


#Printing last 10 rows
print(df.tail(10))
print(df.tail()) #by default, it takes 5 as argument and displays last 5 rows


#Displaying information about dataframe
print(df.describe())
print(df.info())
