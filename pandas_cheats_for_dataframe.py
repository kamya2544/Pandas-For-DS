# We specified values for each column
import pandas as pd
df1 = pd.DataFrame({'a':[4,5,6], 'b':[7,8,9], 'c':[10,11,12]}, index = [1,2,3])
print(df1)

# We specified values for each row
df2 = pd.DataFrame([[4, 5, 6], [7, 8, 9], [10,11,12]], index=[1, 2, 3], columns=['a', 'b', 'c'])
print(df2)

# Multi-indexing
df3 = pd.DataFrame({'a':[4,5,6], 'b':[7,8,9], 'c':[10,11,12]}, index = pd.MultiIndex.from_tuples([('D', 1), ('D', 2), ('e', 2)], names = ['N', 'v']))
print(df3)
