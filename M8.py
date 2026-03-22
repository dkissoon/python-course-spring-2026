import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("sales_data.csv")

# Show the first 5 rows
print(df.head())

# Show basic info
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Make sure Sales and Quantity are numbers
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

# Remove rows with invalid numbers
df = df.dropna()

# Find average sales
average_sales = df["Sales"].mean()

# Find total quantity sold
total_quantity = df["Quantity"].sum()

print("Average Sales:", average_sales)
print("Total Quantity Sold:", total_quantity)

# Group by category and add total sales
sales_by_category = df.groupby("Category")["Sales"].sum()
print(sales_by_category)

# Bar chart
plt.figure()
sales_by_category.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Scatter plot
plt.figure()
plt.scatter(df["Quantity"], df["Sales"])
plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")

# Show both charts
plt.show()