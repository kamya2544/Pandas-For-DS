# A Pandas series is like a column in a table. It is 1D array which holds data of an y type.

import pandas as pd
x = [1,7,2]
y = pd.Series(x)
print(x)
print(y)

# print(y.value_counts())
# print(y.describe())

#labelling
#A label can be used to access a specified value
print(y[0])

#with create label we can create our own name labels
#default index ki jgh apni index values de skte hain
z = pd.Series(x, index=["a", "b", "c"])
print(z)

#access after creating own label
print(z["a"])

#we can also use a key or value object like dictionary when creating a series
#creating a simple pandas series from disctionary
cal = {"day1": 420, "day2": 380, "day3": 390}
cal_new = pd.Series(cal)
print(cal_new)

#creating a series using data from day 1 and day 2 only
result = pd.Series(cal, index=["day1", "day2"])
print(result)

#DataFrame: Datasets in Pandas are usually multi-dimensional table and they are called dataframes.
#Series are like columns and Dataframe is the whole table
record = {"cal":[420,380,390], "duration":[50,40,45]}
record_new = pd.DataFrame(record)
print(record_new)



