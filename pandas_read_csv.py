#read csv files: (comma separated value file) It is a simple way to store big and biggest data sets.
#CSV file contains plain text

#loading csv into dataframe
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
print(df.describe())

print(df) #shows first five and last five records only and puts ... in between
print(df.to_string()) #shows complete records in output (no...)

# max_rows : to check maximum no. of rows system can display
# output is 60 so data with >60 rows needs to be displayed using tostring
# if no of rows is <60 then print(df) doesn't show ... but all records
print(pd.options.display.max_rows)

# we can increase this max rows no. using pandas hack
pd.options.display.max_rows = 700
#this may heat up gpu, ram, our system
print(df) # now it doesn't display...
#AVOID USING THIS....USE tostring

