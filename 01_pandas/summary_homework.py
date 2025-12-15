# -----------------------------------------
# PART 1: SELECTING AND INDEXING DATA
# -----------------------------------------

# 1. Select only specific columns
cols_subset = df[["age", "income", "state", "occupation"]]

# 2. Individuals older than 40 with income > 80,000
older_high_income = df[(df["age"] > 40) & (df["income"] > 80_000)]

# 3. Rows where state is CA or TX
ca_tx = df[df["state"].isin(["CA", "TX"])]

# 4. Occupation contains "engineer" (case-insensitive)
engineers = df[
    df["occupation"]
    .astype(str)
    .str.contains("engineer", case=False, na=False)
]

# -----------------------------------------
# PART 2: HANDLING MISSING DATA
# -----------------------------------------

# 1. Percentage of missing values per column
missing_pct = df.isna().mean() * 100

# 2. Fill missing values for age and income with median
df_filled = df.copy()

df_filled["age"] = df_filled["age"].fillna(df["age"].median())
df_filled["income"] = df_filled["income"].fillna(df["income"].median())

categorical_cols = ["state", "gender", "occupation", "nationality"]
df_filled[categorical_cols] = df_filled[categorical_cols].fillna("Unknown")

# 3. Drop rows where BOTH age and income are missing
df_dropped = df.dropna(subset=["age", "income"], how="all")


# -----------------------------------------
# PART 3: CLEANING AND STANDARDIZING DATA
# -----------------------------------------

df_clean = df.copy()

# 1. Strip whitespace from string columns
string_cols = ["state", "nationality", "gender", "occupation"]

for col in string_cols:
    df_clean[col] = df_clean[col].astype(str).str.strip()

# 2. Normalize cases
# Make state and nationality uppercase
df_clean["state"] = df_clean["state"].str.upper()
df_clean["nationality"] = df_clean["nationality"].str.upper()

# Make occupation title case
df_clean["occupation"] = df_clean["occupation"].str.title()

# 3. Fix known inconsistencies in state and occupation
# replace "tx" with "TX"
df_clean["state"] = df_clean["state"].replace({
    "tx": "TX"
})

# replace "engineering" with "Engineer"
df_clean["occupation"] = df_clean["occupation"].replace({
    "Engineering": "Engineer"
})

# 4. Verify cleaning using value_counts
before_counts = df["state"].value_counts(dropna=False)
after_counts = df_clean["state"].value_counts(dropna=False)


# -----------------------------------------
# PART 4: GROUPING AND AGGREGATION
# -----------------------------------------

# 1. Average income by state
avg_income_state = (
    df_clean
    .groupby("state")["income"]
    .mean()
)

# 2. Summary table by state and occupation
state_summary = (
    df_clean
    .groupby(["state", "occupation"])
    .agg(
        mean_income=("income", "mean"),
        median_age=("age", "median"),
        count=("id", "count")
    )
)

# 3. Sort by mean income descending
state_summary_sorted = state_summary.sort_values(
    by="mean_income",
    ascending=False
)
