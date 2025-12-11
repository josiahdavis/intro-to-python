"""
REFERENCE GUIDE FOR BASIC PYTHON DATA ANALYSIS WITH PANDAS
A single-file reference covering the most common pandas operations 
for data analysis: loading/saving, inspection, indexing & selection, 
filtering, grouping & aggregation, reshaping, joining, handling missing 
data, time series, categorical data, performance tips, plotting, and 
practical examples.
"""

# ------------------------------------------------------------
# 1. CORE OBJECTS: SERIES AND DATAFRAME
# ------------------------------------------------------------

import pandas as pd

# pd.Series: 1D labeled homogeneous data
s = pd.Series([1, 3, 5], index=['a','b','c'])
# a    1
# b    3
# c    5
# dtype: int64

# pd.DataFrame: 2D labeled tabular data (columns can have different types).
df = pd.DataFrame({'A':[1,2,3], 'B':['x','y','z']})
#    A  B
# 0  1  x
# 1  2  y
# 2  3  z

# Key attributes of dataframe
df.shape     # number of rows, number of columns
df.columns   # column labels
df.index     # row labels
df.dtypes    # each column can have unique type
df.head()    # first k rows
df.tail()    # last k rows

# ------------------------------------------------------------
# 2. CREATING DATAFRAMES
# ------------------------------------------------------------

# dict-of-lists
df = pd.DataFrame({'year':[2020,2021], 'sales':[100,150]})

# list of dicts / records
rec = [{'a':1,'b':2}, {'a':3,'b':4}]
df2 = pd.DataFrame(rec)

# from numpy
arr = np.random.randn(5,3)
df3 = pd.DataFrame(arr, columns=['x','y','z'])

# from a Series
s = pd.Series([10,20,30], index=['a','b','c'])
df4 = s.to_frame(name='value')
