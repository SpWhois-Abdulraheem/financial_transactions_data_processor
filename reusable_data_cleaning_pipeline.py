import pandas as pd


def clean_transaction_data(input_file, output_file="clean_transactions.csv"):
    """
    Cleans financial transaction dataset and exports a cleaned version.

    Parameters:
    input_file (str): Path to the raw dataset
    output_file (str): Path to save the cleaned dataset

    Returns:
    pandas.DataFrame: Cleaned dataframe
    """

    # Load dataset
    df = pd.read_csv(input_file)

    original_rows = df.shape[0]

    print("Preview of Dataset")
    print(df.head())

    print("\nOriginal Dataset Shape:", df.shape)

    # Inspect dataset
    print("\nDataset Info")
    print(df.info())

    print("\nMissing Values")
    print(df.isnull().sum())

    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # -------------------------
    # Cleaning Price Column
    # -------------------------

    # Remove currency symbols
    df["price"] = df["price"].replace(r"[$]", "", regex=True)

    # Convert numeric columns
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    # Convert negative values to positive
    df["price"] = df["price"].abs()
    df["quantity"] = df["quantity"].abs()

    # Fill missing numeric values
    df["price"] = df["price"].fillna(df["price"].median())
    df["quantity"] = df["quantity"].fillna(df["quantity"].median())

    # -------------------------
    # Text Standardization
    # -------------------------

    text_columns = ["product_name", "payment_method", "transaction_status"]

    for col in text_columns:
        df[col] = df[col].str.strip().str.lower()

    df["transaction_status"] = df["transaction_status"].fillna("unknown")

    # -------------------------
    # Date Cleaning
    # -------------------------

    df["transaction_date_missing"] = df["transaction_date"].isna()

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"], errors="coerce"
    )

    df["transaction_date"] = df["transaction_date"].fillna(
        pd.Timestamp("2026-01-01"))

    # -------------------------
    # Remove Duplicates
    # -------------------------

    df = df.drop_duplicates()

    # -------------------------
    # Feature Engineering
    # -------------------------

    df["total_value"] = df["quantity"] * df["price"]

    df["order_size"] = df["quantity"].apply(
        lambda x: "bulk" if x >= 100 else "regular"
    )

    df["transaction_year"] = df["transaction_date"].dt.year
    df["transaction_month"] = df["transaction_date"].dt.month

    df["high_value_transaction"] = df["total_value"] > 2000

    # -------------------------
    # Handle Missing Values
    # -------------------------

    df = df.dropna(subset=["transaction_id"])
    df = df.dropna(subset=["transaction_date"])

    df["customer_id"] = df["customer_id"].fillna("unknown")

    # -------------------------
    # Validation Checks
    # -------------------------

    print("\nCleaned Dataset Shape:", df.shape)

    print("\nRemaining Missing Values:")
    print(df.isnull().sum())

    cleaned_rows = df.shape[0]

    print("\nData Cleaning Summary")
    print("----------------------")
    print("Original rows:", original_rows)
    print("Clean rows:", cleaned_rows)
    print("Rows removed:", original_rows - cleaned_rows)

    # -------------------------
    # Export Clean Data
    # -------------------------

    df.to_csv(output_file, index=False)

    print("\nClean dataset exported successfully.")

    return df


# Run the function if script is executed directly
if __name__ == "__main__":
    clean_transaction_data("financial_transactions.csv")
