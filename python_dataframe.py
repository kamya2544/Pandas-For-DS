#DataFrame: It is a 2D data structure like 2D array with table including rows and columns
import pandas as pd
data = {"cal":[420,380,390], "duration":[50,40,45]}
dataframe = pd.DataFrame(data)
print(dataframe)

#locate row: pandas use loc attribute to return one or more specified row
print(dataframe.loc[0]) #0th row
print(dataframe.loc[0][1]) #0th row's 1st element
print(dataframe.loc[[0,1]]) #0th and 1st row

#named index: with the index argument, we can name our own index
dataframe = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(dataframe)

#locate the named indexes
print(dataframe.loc["day1"])
print(dataframe.loc[["day1", "day2"]])

#load the data from csv file into dataframe i.e data.csv
fileload =pd.read_csv("data.csv")
print(fileload)
