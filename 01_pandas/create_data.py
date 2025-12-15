"""Simple script to generate some data to work for pandas training."""

import numpy as np
import pandas as pd

N = 10_000
np.random.seed(42)

df = pd.DataFrame({
    "id": np.arange(1, N + 1),
    "time_period": np.random.choice(["2010-2014", "2015-2019", "2020-2024"], size=N),
    "age": np.random.randint(18, 80, size=N),
    "nationality": np.random.choice(["USA", "Canada", "Mexico"], size=N),
    "state": np.random.choice(["CA", "NY", "TX", "WA"], size=N),
    "income": np.random.normal(60000, 15000, size=N).round(2),
    "gender": np.random.choice(["Male", "Female", "Non-Binary"], size=N),
    "occupation": np.random.choice(["Engineer", "Teacher", "Nurse"], size=N)
})

# Add missing data
for col in ["age", "nationality", "state", "income", "gender", "occupation"]:
    mask = np.random.rand(N) < 0.05
    df.loc[mask, col] = np.nan

# Add messy categories (case issues, whitespace, misspellings)
df.loc[df.sample(frac=0.03).index, "nationality"] = " usa "
df.loc[df.sample(frac=0.03).index, "state"] = "tx "
df.loc[df.sample(frac=0.02).index, "gender"] = "FEMALE "
df.loc[df.sample(frac=0.02).index, "occupation"] = "nurse  "

# Add extreme outliers
df.loc[df.sample(20).index, "age"] = np.random.choice([0, 5, 150, 200], size=20)
df.loc[df.sample(20).index, "income"] = np.random.choice([500, 1000, 2000000], size=20)

# Saving data
file_loc = "data.csv"
print(f"Saving data to {file_loc}")
df.to_csv(file_loc, index=False)

"""
Output:

        id time_period   age nationality state    income  gender occupation
5421  5422   2010-2014  69.0      Mexico    WA  57757.04    Male    Teacher
8267  8268   2010-2014  27.0      Canada    CA  32324.92    Male    Teacher
8374  8375   2015-2019  39.0         USA    TX  47872.32  Female   Engineer
3131  3132   2020-2024  36.0      Canada   NaN  68254.56     NaN    Teacher
3581  3582   2010-2014  18.0         USA    tx  33562.09    Male   Engineer
"""
