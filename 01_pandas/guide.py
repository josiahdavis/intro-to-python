"""
REFERENCE GUIDE FOR BASIC PYTHON DATA ANALYSIS WITH PANDAS
A single-file reference covering the most common pandas operations 
for data analysis: loading/saving, inspection, indexing & selection, 
filtering, grouping & aggregation, reshaping, joining, handling missing 
data, time series, categorical data, performance tips, plotting, and 
practical examples.
"""

# ------------------------------------------------------------
# 1. CORE OBJECTS: DATAFRAME AND SERIES
# ------------------------------------------------------------

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

# ------------------------------------------------------------
# 1. READING AND WRITING DATA
# ------------------------------------------------------------

import pandas as pd

# Reading
df = pd.read_csv("data.csv")
# df = pd.read_parquet("data.parquet")

# Writing
df.to_csv("data.csv", index=False)
df.to_parquet("data.parquet", index=False)

# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

# ------------------------------------------------------------
# 2. Inspecting Data
# ------------------------------------------------------------

df.shape       # number of rows, number of columns

df.columns     # dataframe has column labels
df.index       # dataframe has row labels
df.dtypes      # each column can have unique type

df.head()      # first k rows
df.tail()      # last k rows
df.sample(5)   # randonly selected rows

df.isna().sum() # Check missing values

df["state"].value_counts()                # check count for string/category
df["state"].value_counts(dropna=False)    # include missing

# Additional methods to explore
df.info()
df.describe()
df.describe(include='object')

# ------------------------------------------------------------
# 3. Indexing & Selection
# ------------------------------------------------------------

# Column selection
ages = df["age"]
subset = df[["age", "income", "state"]]

# Row selection with iloc (position-based)
first_5 = df.iloc[:5]

# Row/col selection with loc (label-based)
state_age = df.loc[df.index[:5], ["state", "age"]]

# Boolean selection
high_income = df[df["income"] > 100000]


# ------------------------------------------------------------
# 4. Filtering
# ------------------------------------------------------------

# Filter by multiple conditions
filtered = df[(df["age"] > 30) & (df["state"] == "CA")]

# Filter with .isin
states_of_interest = df[df["state"].isin(["CA", "TX"])]

# Filter on string operations
contains_us = df[df["nationality"].astype(str).str.contains("us", case=False, na=False)]


# ------------------------------------------------------------
# 5. Grouping & Aggregation
# ------------------------------------------------------------

# Average income by state
avg_income_state = df.groupby("state")["income"].mean()

# Multiple aggregations
summary = df.groupby("state").agg(
    avg_income=("income", "mean"),
    median_age=("age", "median"),
    count=("id", "count")
)

# ------------------------------------------------------------
# 6. Joining / Merging
# ------------------------------------------------------------

# Create a small lookup table to merge
state_region = pd.DataFrame({
    "state": ["CA", "NY", "TX", "WA"],
    "region": ["West", "Northeast", "South", "West"]
})

df_merged = df.merge(state_region, on="state", how="left")

df_merged.head()

# ------------------------------------------------------------
# 7. Handling Missing Data
# ------------------------------------------------------------

# Detect missing
missing_report = df.isna().sum()

# Drop rows with missing values in selected columns
df_no_missing_income = df.dropna(subset=["income"])

# Fill missing numeric values
df_filled_age = df.copy()
df_filled_age["age"] = df_filled_age["age"].fillna(df["age"].median())

# Fill missing categorical with a placeholder
df_filled_cat = df.copy()
df_filled_cat["nationality"] = df_filled_cat["nationality"].fillna("Unknown")


# ------------------------------------------------------------
# 8. Cleaning Data
# ------------------------------------------------------------

df_clean = df.copy()

# Strip whitespace
for col in ["nationality", "state", "gender", "occupation"]:
    df_clean[col] = df_clean[col].astype(str).str.strip()

# Normalize case
df_clean["nationality"] = df_clean["nationality"].str.title()
df_clean["state"] = df_clean["state"].str.upper()
df_clean["gender"] = df_clean["gender"].str.title()
df_clean["occupation"] = df_clean["occupation"].str.title()

# Fix known misspellings
df_clean["nationality"] = df_clean["nationality"].replace({
    "Usa": "USA",
})

df_clean["state"] = df_clean["state"].replace({
    "Tx": "TX",
})

df_clean["gender"] = df_clean["gender"].replace({
    "Female ": "Female"
})

# ------------------------------------------------------------
# 9. Categorical Data
# ------------------------------------------------------------

df_cat = df_clean.copy()
df_cat["state"] = df_cat["state"].astype("category")
df_cat["gender"] = df_cat["gender"].astype("category")

df_cat.dtypes


# ------------------------------------------------------------
# 10. Working With Dates
# ------------------------------------------------------------

# Create a synthetic date column
df_cat["date"] = pd.to_datetime(
    np.random.choice(pd.date_range("2010-01-01", "2024-12-31"), size=len(df_cat))
)

# Extract date parts
df_cat["year"] = df_cat["date"].dt.year
df_cat["month"] = df_cat["date"].dt.month
df_cat["week"] = df_cat["date"].dt.isocalendar().week

df_cat[["date", "year", "month", "week"]].head()

# ------------------------------------------------------------
# 11. CREATING DATAFRAMES
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
