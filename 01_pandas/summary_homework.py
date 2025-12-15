# -----------------------------------------
# PART 1: SELECTING AND INDEXING DATA
# -----------------------------------------

# 1. Select only specific columns: ["age", "income", "state", "occupation"]
cols_subset = # Use these columns ["age", "income", "state", "occupation"]

# 2. Individuals older than 40 with income > 80,000
older_high_income = # FIX ME

# 3. Rows where state is CA or TX
ca_tx = # FIX ME

# 4. Occupation contains "engineer" (case-insensitive)
engineers = # FIX ME

# -----------------------------------------
# PART 2: HANDLING MISSING DATA
# -----------------------------------------

# 1. Percentage of missing values per column
missing_pct = # FIX ME

# 2. Fill missing values for age and income with median
df_filled = df.copy()

df_filled["age"] = # Fill missing with median
df_filled["income"] = # Fill missing with median

categorical_cols = ["state", "gender", "occupation", "nationality"]
df_filled[categorical_cols] = # Fill with Unknown

# 3. Drop rows where BOTH age and income are missing
df_dropped = # FIX ME


# -----------------------------------------
# PART 3: CLEANING AND STANDARDIZING DATA
# -----------------------------------------

df_clean = df.copy()

# 1. Strip whitespace from string columns
string_cols = ["state", "nationality", "gender", "occupation"]

for col in string_cols:
    df_clean[col] = # FIX ME

# 2. Normalize cases
# Make state and nationality uppercase
df_clean["state"] = # FIX ME
df_clean["nationality"] = # FIX ME

# Make occupation title case
df_clean["occupation"] = # FIX ME

# 3. Fix known inconsistencies in state and occupation
# replace "tx" with "TX"
df_clean["state"] = # FIX ME

# replace "engineering" with "Engineer"
df_clean["occupation"] = # FIX ME

# 4. Verify cleaning using value_counts
before_counts = df["state"].value_counts(dropna=False)
after_counts = df_clean["state"].value_counts(dropna=False)


# -----------------------------------------
# PART 4: GROUPING AND AGGREGATION
# -----------------------------------------

# 1. Average income by state
avg_income_state = # FIX ME

# 2. Summary table by state and occupation
state_summary = # FIX ME


# 3. Sort by mean income descending
state_summary_sorted = # FIX ME
