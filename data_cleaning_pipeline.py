# Loading the dataset and importing pandas library

import pandas as pd

df = pd.read_csv("financial_transactions.csv")
original_rows = df.shape[0]
print(df.head())

print("Original Dataset Shape:", df.shape)
# inspecting the dataset

print(df.shape)
print(df.info())
print(df.isnull().sum())

# Renaming columns to standardized snake_case format
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Cleaning Price Column

# Removing currency symbol
df["price"] = df["price"].replace(r"[$]", "", regex=True)

# Converting the datatype to a numberic datatype
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

# Converting price negative values to Positive
df["price"] = df["price"].abs()

# Filling missing values with the median price
df["price"] = df["price"].fillna(df["price"].median())
df["quantity"] = df["quantity"].fillna(df["quantity"].median())

# Clenaing Quanity Column
df["quantity"] = df["quantity"].abs()

# Standardizing Text format on product_name,payment_method and transaction_status columns
text_columns = ["product_name", "payment_method", "transaction_status"]

for col in text_columns:
    df[col] = df[col].str.strip().str.lower()
df["transaction_status"] = df["transaction_status"].fillna("unknown")

# Converting transaction_date column to datetime format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"], errors="coerce")

# Removing duplicates
df = df.drop_duplicates()

# Feature Engineering

# Total Value
df["total_value"] = df["quantity"] * df["price"]

# Order size
df["order_size"] = df["quantity"].apply(
    lambda x: "bulk" if x >= 100 else "regular")

# transaction year
df["transaction_year"] = df["transaction_date"].dt.year

# transaction month
df["transaction_month"] = df["transaction_date"].dt.month

# high value transaction
df["high_value_transaction"] = df["total_value"] > 2000

# dropping rows without transaction IDs
df = df.dropna(subset=["transaction_id"])

# dropping rows with invalid dates
df = df.dropna(subset=["transaction_date"])

# replacing missing customer ids with unknown
df["customer_id"] = df["customer_id"].fillna("unknown")


# after cleaning validation check
print("Cleaned Dataset Shape:", df.shape)
print("\nRemaining Missing Values:")
print(df.isnull().sum())
cleaned_rows = df.shape[0]

print("\nData Cleaning Summary")
print("----------------------")
print("Original rows:", original_rows)
print("Clean rows:", df.shape[0])
print("Rows removed:", original_rows - df.shape[0])

# Exporting clean dataset
df.to_csv("clean_transactions.csv", index=False)
print("Clean dataset exported successfully.")
