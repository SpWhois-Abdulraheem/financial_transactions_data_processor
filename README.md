# financial_transactions_data_processor
# Data Cleaning Pipeline for Financial Transactions

## Project Overview

This project demonstrates the development of a data cleaning and transformation pipeline using Python and the Pandas library.

The dataset used in this project contains 100,000 financial transaction records with intentionally introduced inconsistencies such as missing values, invalid dates, inconsistent text formatting, and incorrect numeric formats.

The objective of this assignment was to design a data engineering pipeline capable of cleaning, transforming, and enriching the dataset so it becomes suitable for downstream analytics.

---

## Dataset

The dataset contains the following columns:

* Transaction_ID
* Transaction_Date
* Customer_ID
* Product_Name
* Quantity
* Price
* Payment_Method
* Transaction_Status

Several data quality issues were intentionally present in the dataset including:

* Missing values
* Invalid transaction dates
* Negative numeric values
* Currency symbols in numeric fields
* Inconsistent text formatting
* Duplicate records

---

## Data Cleaning Approach

The data cleaning pipeline was implemented using **Python and Pandas** and involved the following steps:

### 1. Data Inspection

Initial exploration of the dataset to understand its structure and identify potential data quality issues.

* Displayed dataset preview
* Checked dataset shape
* Inspected column data types
* Identified missing values

### 2. Column Standardization

All column names were converted to **snake_case format** to follow common data engineering naming conventions.

### 3. Numeric Data Cleaning

The price and quantity columns were cleaned by:

* Removing currency symbols
* Converting values to numeric types
* Converting negative values to positive
* Filling missing values with median values

### 4. Text Standardization

Text-based columns were standardized by:

* Removing leading/trailing spaces
* Converting text values to lowercase

Affected columns:

* product_name
* payment_method
* transaction_status

### 5. Date Cleaning

The transaction_date column was converted to datetime format. Invalid dates were coerced to null values and removed.

### 6. Duplicate Removal

Duplicate transaction records were identified and removed to maintain data integrity.

### 7. Handling Missing Values

Additional cleaning steps included:

* Removing rows with missing transaction IDs
* Removing rows with invalid transaction dates
* Filling missing customer IDs with "unknown"

### 8. Feature Engineering

New analytical features were created to enhance the dataset:

* total_value → quantity × price
* order_size → categorizes orders as bulk or regular
* transaction_year → extracted from transaction date
* transaction_month → extracted from transaction date
* high_value_transaction → identifies transactions above a defined threshold 2000



## Final Output

The cleaned dataset was exported as:


clean_transactions.csv


The resulting dataset is fully cleaned, standardized, and enriched with additional analytical features.



## Technologies Used

* Python
* Pandas
* CSV data processing

---

## Project Structure


DataEngineeringWk3
│
├── financial_transactions.csv
├── clean_transactions.csv
├── data_cleaning_pipeline.py
└── README.md


---

## Key Learning Outcomes

This project demonstrates important **data engineering concepts**, including:

* Data inspection and validation
* Data cleaning and transformation
* Handling missing values
* Feature engineering
* Building a simple ETL-style data pipeline using Python

---

  
