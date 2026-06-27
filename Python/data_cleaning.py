# ==========================================================
# Project : Customer Insights & Recommendation Project

# -----------------------------
# Import Libraries
# -----------------------------
from pathlib import Path
import pandas as pd

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset Path
DATASET_PATH = BASE_DIR / "Dataset" / "Customer_Insights_Dataset.csv"

print("Dataset Path:", DATASET_PATH)

df = pd.read_csv(DATASET_PATH)

import numpy as np  # type: ignore[import-not-found]

pd.set_option("display.max_columns",None)

print("="*70)
print(" CUSTOMER INSIGHTS PROJECT ")
print("="*70)

# -----------------------------
# Load Dataset
# -----------------------------
# Dataset already loaded from DATASET_PATH above.

print("\nDataset Loaded Successfully\n")

# -----------------------------
# Dataset Shape
# -----------------------------

print("Rows :",df.shape[0])
print("Columns :",df.shape[1])

# -----------------------------
# Preview
# -----------------------------

print(df.head())

print(df.tail())

# -----------------------------
# Dataset Information
# -----------------------------

print("\nInformation\n")

print(df.info())

# -----------------------------
# Describe
# -----------------------------

print(df.describe())

print(df.describe(include="object"))

# -----------------------------
# Column Names
# -----------------------------

print(df.columns)

# -----------------------------
# Rename Columns
# -----------------------------

df.columns=df.columns.str.strip()

# -----------------------------
# Missing Values
# -----------------------------

print("\nMissing Values")

print(df.isnull().sum())

# Missing %

missing=(df.isnull().sum()/len(df))*100

print(missing)

# -----------------------------
# Fill Missing Values
# -----------------------------

for col in df.columns:

    if df[col].dtype=="object":

        if col == "Order Date":
            df[col] = df[col].astype("string").fillna(pd.NA)
        else:
            df[col] = df[col].fillna("Unknown")

    else:

        df[col]=df[col].fillna(df[col].median())

print("Missing Values Handled")

# -----------------------------
# Duplicate Records
# -----------------------------

duplicate=df.duplicated().sum()

print("Duplicate :",duplicate)

df=df.drop_duplicates()

# -----------------------------
# Remove Extra Spaces
# -----------------------------

for col in df.select_dtypes(include="object"):

    df[col]=df[col].str.strip()

print("Spaces Removed")

# -----------------------------
# Data Type Conversion
# -----------------------------

numeric_columns=[
"Amount",
"Profit",
"Quantity"
]

for col in numeric_columns:

    if col in df.columns:

        df[col]=pd.to_numeric(
            df[col],
            errors="coerce"
        )

        df[col]=df[col].fillna(0)

# -----------------------------
# Date Conversion
# -----------------------------

if "Order Date" in df.columns:

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True,
        errors="coerce"
    )

# -----------------------------
# Feature Engineering
# -----------------------------

print("\nCreating Features...")

# Year

df["Year"]=df["Order Date"].dt.year

# Month

df["Month"]=df["Order Date"].dt.month_name()

# Quarter

df["Quarter"]=df["Order Date"].dt.quarter

# Day

df["Day"]=df["Order Date"].dt.day

# Weekday

df["Weekday"]=df["Order Date"].dt.day_name()

# Profit Margin

df["Profit_Margin_%"]=np.where(

    df["Amount"]==0,

    0,

    round((df["Profit"]/df["Amount"])*100,2)

)

# Average Selling Price

df["Avg_Price"]=np.where(

    df["Quantity"]==0,

    0,

    round(df["Amount"]/df["Quantity"],2)

)

# Order Type

order_type=[]

for i in df["Amount"]:

    if i>=10000:

        order_type.append("High Value")

    elif i>=5000:

        order_type.append("Medium Value")

    else:

        order_type.append("Low Value")

df["Order_Type"]=order_type

# Profit Status

profit=[]

for i in df["Profit"]:

    if i>0:

        profit.append("Profit")

    elif i==0:

        profit.append("Break Even")

    else:

        profit.append("Loss")

df["Profit_Status"]=profit

print("Feature Engineering Completed")

# -----------------------------
# Outlier Detection
# -----------------------------

Q1=df["Amount"].quantile(.25)

Q3=df["Amount"].quantile(.75)

IQR=Q3-Q1

lower=Q1-1.5*IQR

upper=Q3+1.5*IQR

print("Lower :",lower)

print("Upper :",upper)

# -----------------------------
# Basic Analysis
# -----------------------------

print("\nTotal Sales")

print(df["Amount"].sum())

print("\nTotal Profit")

print(df["Profit"].sum())

print("\nAverage Order Value")

print(round(df["Amount"].mean(),2))

print("\nTop 10 Customers")

print(

df.groupby("CustomerName")["Amount"]

.sum()

.sort_values(ascending=False)

.head(10)

)

print("\nTop States")

print(

df.groupby("State")["Amount"]

.sum()

.sort_values(ascending=False)

)

print("\nCategory Analysis")

print(

df.groupby("Category")["Amount"]

.sum()

)

print("\nPayment Mode")

print(

df.groupby("PaymentMode")["Amount"]

.sum()

)

# -----------------------------
# Export Clean Dataset
# -----------------------------

output_path = BASE_DIR / "Output" / "Cleaned_Customer_Data.csv"

df.to_csv(

    output_path,

    index=False

)

print("\nClean Dataset Saved")

print("="*70)

print("DATA CLEANING COMPLETED SUCCESSFULLY")

print("="*70)