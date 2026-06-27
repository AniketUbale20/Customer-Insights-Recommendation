# ==========================================================
# Project : Customer Insights & Recommendation Project
# Author  : Aniket Ubale
# File    : eda.py
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ----------------------------------------------------------
# Project Paths
# ----------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET = BASE_DIR / "Output" / "Cleaned_Customer_Data.csv"
IMAGE_DIR = BASE_DIR / "Images"

IMAGE_DIR.mkdir(exist_ok=True)

# ----------------------------------------------------------
# Load Data
# ----------------------------------------------------------

df = pd.read_csv(DATASET)

print("="*60)
print("Exploratory Data Analysis Started")
print("="*60)

# ----------------------------------------------------------
# Basic Information
# ----------------------------------------------------------

print(df.head())
print(df.shape)
print(df.columns)

# ----------------------------------------------------------
# Style
# ----------------------------------------------------------

plt.style.use("ggplot")

# ----------------------------------------------------------
# 1. Sales by State
# ----------------------------------------------------------

plt.figure(figsize=(10,6))

(df.groupby("State")["Amount"]
   .sum()
   .sort_values(ascending=False)
   .plot(kind="bar"))

plt.title("Sales by State")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(IMAGE_DIR/"sales_by_state.png")
plt.close()

# ----------------------------------------------------------
# 2. Profit by State
# ----------------------------------------------------------

plt.figure(figsize=(10,6))

(df.groupby("State")["Profit"]
   .sum()
   .sort_values(ascending=False)
   .plot(kind="bar",color="green"))

plt.title("Profit by State")
plt.tight_layout()
plt.savefig(IMAGE_DIR/"profit_by_state.png")
plt.close()

# ----------------------------------------------------------
# 3. Sales by Category
# ----------------------------------------------------------

plt.figure(figsize=(8,6))

(df.groupby("Category")["Amount"]
   .sum()
   .plot(kind="pie",autopct="%1.1f%%"))

plt.ylabel("")
plt.title("Sales by Category")
plt.savefig(IMAGE_DIR/"sales_category.png")
plt.close()

# ----------------------------------------------------------
# 4. Profit by Category
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

(df.groupby("Category")["Profit"]
   .sum()
   .plot(kind="bar"))

plt.title("Profit by Category")
plt.tight_layout()
plt.savefig(IMAGE_DIR/"profit_category.png")
plt.close()

# ----------------------------------------------------------
# 5. Top Customers
# ----------------------------------------------------------

plt.figure(figsize=(12,6))

(df.groupby("CustomerName")["Amount"]
   .sum()
   .sort_values(ascending=False)
   .head(10)
   .plot(kind="bar"))

plt.title("Top 10 Customers")
plt.tight_layout()
plt.savefig(IMAGE_DIR/"top_customers.png")
plt.close()

# ----------------------------------------------------------
# 6. Top Products
# ----------------------------------------------------------

plt.figure(figsize=(10,6))

(df.groupby("Sub-Category")["Amount"]
   .sum()
   .sort_values(ascending=False)
   .head(10)
   .plot(kind="bar"))

plt.title("Top Products")
plt.tight_layout()
plt.savefig(IMAGE_DIR/"top_products.png")
plt.close()

# ----------------------------------------------------------
# 7. Payment Mode
# ----------------------------------------------------------

plt.figure(figsize=(7,7))

(df.groupby("PaymentMode")["Amount"]
   .sum()
   .plot(kind="pie",autopct="%1.1f%%"))

plt.ylabel("")
plt.title("Payment Mode")
plt.savefig(IMAGE_DIR/"payment_mode.png")
plt.close()

# ----------------------------------------------------------
# 8. Monthly Sales
# ----------------------------------------------------------

month_order=[
"January","February","March","April",
"May","June","July","August",
"September","October","November","December"
]

if "Month" in df.columns:

    df["Month"]=pd.Categorical(
        df["Month"],
        categories=month_order,
        ordered=True
    )

plt.figure(figsize=(10,5))

(df.groupby("Month")["Amount"]
   .sum()
   .plot(marker="o"))

plt.title("Monthly Sales Trend")
plt.grid(True)

plt.tight_layout()
plt.savefig(IMAGE_DIR/"monthly_sales.png")
plt.close()

# ----------------------------------------------------------
# 9. Monthly Profit
# ----------------------------------------------------------

plt.figure(figsize=(10,5))

(df.groupby("Month")["Profit"]
   .sum()
   .plot(marker="o",color="green"))

plt.title("Monthly Profit Trend")

plt.grid(True)

plt.tight_layout()

plt.savefig(IMAGE_DIR/"monthly_profit.png")

plt.close()

# ----------------------------------------------------------
# 10. Profit Distribution
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(df["Profit"],bins=25)

plt.title("Profit Distribution")

plt.tight_layout()

plt.savefig(IMAGE_DIR/"profit_distribution.png")

plt.close()

# ----------------------------------------------------------
# 11. Amount Distribution
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(df["Amount"],bins=25)

plt.title("Sales Distribution")

plt.tight_layout()

plt.savefig(IMAGE_DIR/"sales_distribution.png")

plt.close()

# ----------------------------------------------------------
# 12. Correlation Heatmap
# ----------------------------------------------------------

numeric=df.select_dtypes(include="number")

corr=numeric.corr()

plt.figure(figsize=(8,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(IMAGE_DIR/"correlation_heatmap.png")

plt.close()

# ----------------------------------------------------------
# 13. Quantity Analysis
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

(df.groupby("Category")["Quantity"]
   .sum()
   .plot(kind="bar"))

plt.title("Quantity by Category")

plt.tight_layout()

plt.savefig(IMAGE_DIR/"quantity_category.png")

plt.close()

# ----------------------------------------------------------
# 14. Order Type
# ----------------------------------------------------------

plt.figure(figsize=(7,7))

(df.groupby("Order_Type")["Amount"]
   .sum()
   .plot(kind="pie",autopct="%1.1f%%"))

plt.ylabel("")

plt.title("Order Type")

plt.savefig(IMAGE_DIR/"order_type.png")

plt.close()

# ----------------------------------------------------------
# 15. Profit Margin
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

plt.boxplot(df["Profit"])

plt.title("Profit Box Plot")

plt.savefig(IMAGE_DIR/"profit_boxplot.png")

plt.close()

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\n========== EDA SUMMARY ==========\n")

print("Total Sales :",df["Amount"].sum())

print("Total Profit :",df["Profit"].sum())

print("Average Order Value :",round(df["Amount"].mean(),2))

print("Highest Sale :",df["Amount"].max())

print("Highest Profit :",df["Profit"].max())

print("\nTop State")

print(df.groupby("State")["Amount"].sum().idxmax())

print("\nTop Category")

print(df.groupby("Category")["Amount"].sum().idxmax())

print("\nTop Payment Mode")

print(df.groupby("PaymentMode")["Amount"].sum().idxmax())

print("\nEDA Completed Successfully")

print(f"\nCharts Saved in : {IMAGE_DIR}")