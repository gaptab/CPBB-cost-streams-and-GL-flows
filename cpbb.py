# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# data
data = {
    "Product": ["Personal Loan", "Personal Loan", "Personal Loan", "Credit Card", "Credit Card", "Business Loan", "Business Loan"],
    "Cost Category": ["Direct Cost", "Indirect Cost", "Fixed Cost", "Variable Cost", "Direct Cost", "Indirect Cost", "Fixed Cost"],
    "Cost Description": [
        "Interest Paid", "Marketing Campaign", "Loan Processing Software",
        "Payment Processing Fee", "Cashback/Rewards Expense",
        "Branch Operating Expense", "Trade Finance Platform"
    ],
    "Amount (USD)": [50000, 5000, 15000, 2000, 10000, 20000, 30000],
    "GL Account Code": [4110, 5120, 5310, 4120, 4130, 5130, 5320],
    "Transaction Date": [
        "2024-12-01", "2024-12-02", "2024-12-03", "2024-12-04", 
        "2024-12-05", "2024-12-06", "2024-12-07"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Group by Product and Cost Category
grouped = df.groupby(["Product", "Cost Category"])["Amount (USD)"].sum()

# Convert grouped data to a DataFrame for easier viewing
grouped_df = grouped.reset_index()

# Display the grouped DataFrame
print(grouped_df)

# Sort by Product and Amount
sorted_df = grouped_df.sort_values(by=["Product", "Amount (USD)"], ascending=[True, False])

print(sorted_df)


# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=grouped_df, x="Product", y="Amount (USD)", hue="Cost Category")
plt.title("Cost Breakdown by Product and Cost Category")
plt.xlabel("Product")
plt.ylabel("Total Cost (USD)")
plt.legend(title="Cost Category")
plt.show()

# Calculate total cost
total_cost = df["Amount (USD)"].sum()
print(f"Total Cost: {total_cost}")

# Add contribution percentage
df["Contribution (%)"] = (df["Amount (USD)"] / total_cost) * 100

# Display the updated DataFrame
print(df)

# Define a threshold for high-cost areas (e.g., 10%)
threshold = 10

# Filter for high-cost areas
high_cost_areas = df[df["Contribution (%)"] > threshold]

print(high_cost_areas)

# Group by Cost Category and calculate total contribution
category_contribution = df.groupby("Cost Category")["Amount (USD)"].sum().reset_index()

# Add contribution percentage for each category
category_contribution["Contribution (%)"] = (category_contribution["Amount (USD)"] / total_cost) * 100

print(category_contribution)

# Plot a pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_contribution["Contribution (%)"], labels=category_contribution["Cost Category"], 
        autopct='%1.1f%%', startangle=90, colors=["#FF9999", "#66B3FF", "#99FF99", "#FFCC99"])
plt.title("Contribution by Cost Category")
plt.show()

df.to_csv("cost_trends.csv", index=False)