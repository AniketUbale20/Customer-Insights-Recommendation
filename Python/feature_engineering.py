

import pandas as pd
import numpy as np
from pathlib import Path

# ----------------------------------------------------------
# Project Paths
# ----------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "Output" / "Cleaned_Customer_Data.csv"
OUTPUT_FILE = BASE_DIR / "Output" / "Customer_Feature_Engineered.csv"

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print("="*60)
print("Feature Engineering Started")
print("="*60)

# ----------------------------------------------------------
# Customer Total Spend
# ----------------------------------------------------------

customer_spend = (
    df.groupby("CustomerName")["Amount"]
      .sum()
      .reset_index()
      .rename(columns={"Amount":"Customer_Total_Spend"})
)

df = df.merge(customer_spend,on="CustomerName",how="left")

# ----------------------------------------------------------
# Customer Total Orders
# ----------------------------------------------------------

customer_orders = (
    df.groupby("CustomerName")
      .size()
      .reset_index(name="Total_Orders")
)

df = df.merge(customer_orders,on="CustomerName",how="left")

# ----------------------------------------------------------
# Customer Total Profit
# ----------------------------------------------------------

customer_profit = (
    df.groupby("CustomerName")["Profit"]
      .sum()
      .reset_index()
      .rename(columns={"Profit":"Customer_Total_Profit"})
)

df = df.merge(customer_profit,on="CustomerName",how="left")

# ----------------------------------------------------------
# Customer Segment
# ----------------------------------------------------------

conditions = [
    df["Customer_Total_Spend"] >= 15000,
    df["Customer_Total_Spend"] >= 7000
]

values = [
    "High Value",
    "Medium Value"
]

df["Customer_Segment"] = np.select(
    conditions,
    values,
    default="Low Value"
)

# ----------------------------------------------------------
# Profit Category
# ----------------------------------------------------------

conditions = [
    df["Profit"] > 500,
    df["Profit"] > 0,
    df["Profit"] <= 0
]

values = [
    "High Profit",
    "Medium Profit",
    "Loss"
]

df["Profit_Category"] = np.select(
    conditions,
    values,
    default="Loss"
)

# ----------------------------------------------------------
# Average Customer Spend
# ----------------------------------------------------------

df["Average_Customer_Spend"] = (
    df["Customer_Total_Spend"] /
    df["Total_Orders"]
).round(2)

# ----------------------------------------------------------
# Estimated Customer Lifetime Value
# ----------------------------------------------------------

df["Estimated_CLV"] = (
    df["Average_Customer_Spend"] *
    df["Total_Orders"]
).round(2)

# ----------------------------------------------------------
# Discount Impact
# ----------------------------------------------------------

df["Discount_Impact"] = np.where(
    df["Profit"] < 0,
    "High",
    "Low"
)

# ----------------------------------------------------------
# Sales Performance
# ----------------------------------------------------------

conditions = [
    df["Amount"] >= 10000,
    df["Amount"] >= 5000
]

values = [
    "Excellent",
    "Good"
]

df["Sales_Performance"] = np.select(
    conditions,
    values,
    default="Average"
)

# ----------------------------------------------------------
# Save Dataset
# ----------------------------------------------------------

df.to_csv(OUTPUT_FILE,index=False)

print("Feature Engineering Completed")

print("\nCustomer Segments")

print(df["Customer_Segment"].value_counts())

print("\nProfit Categories")

print(df["Profit_Category"].value_counts())

print("\nOutput Saved")

print(OUTPUT_FILE)