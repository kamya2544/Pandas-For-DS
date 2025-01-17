# Cleaning Data: It means fixing the bad data in our dataset.
# Bad Data could be empty cell, duplicate data, wrong data, data in wrong format, etc

# Loading and reading the original dataframe
import pandas as pd
df = pd.read_csv('dirtydata.csv')
print(df.to_string())

# Empty Cell always leads to wrong results so we will remove the rows that contain bad data. (NaN)
df_new = df.dropna()
print(df_new.to_string())

# We didn't directly change df and used df_new instead because we may need original data at some point in future which is stored as df

# Case where we change the original data, we use inplace=True
df.dropna(inplace=True)
print(df.to_string())

# Replacing the empy value using fillna() method
df = pd.read_csv('dirtydata.csv')
df.fillna(130, inplace=True)
print(df.to_string())

#To replace only the empty value for one columne, we need to specify the column name
df = pd.read_csv('dirtydata.csv')
df["Calories"] = df["Calories"].fillna(130)
print(df.to_string())


# Mean, Median, Mode Replacement in empty cell
df = pd.read_csv('dirtydata.csv')
mean_cal = df["Calories"].mean()
df["Calories"] = df["Calories"].fillna(mean_cal)
print(df.to_string())

df = pd.read_csv('dirtydata.csv')
mode_cal = df["Calories"].mode()[0] #id we don't use [0] then it will not display mode but NaN only that is because we need to iterate one by one so we use indexing
df["Calories"] = df["Calories"].fillna(mode_cal)
print(df.to_string())

df = pd.read_csv('dirtydata.csv')
median_cal = df["Calories"].median()
df["Calories"] = df["Calories"].fillna(median_cal)
print(df.to_string())



