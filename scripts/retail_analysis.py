import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the dataset
df = pd.read_csv("data/retail_data.csv")

# Basic cleaning (if needed)
df.dropna(subset=['Category', 'SubCategory', 'UnitPrice', 'UnitCost'], inplace=True)

# Add Profit column
df['Profit'] = (df['UnitPrice'] - df['UnitCost']) * df['UnitsSold']

# Correlation between inventory days and profit
correlation = df[['InventoryDays', 'Profit']].corr()
print("\nCorrelation Matrix:\n", correlation)

# Plot: Profit vs InventoryDays
sns.set(style='whitegrid')
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='InventoryDays', y='Profit', hue='Category', alpha=0.7)
plt.title('Profit vs Inventory Days by Category')
plt.savefig("output/profit_vs_inventory.png")
plt.close()

# Save slow-moving items
slow_movers = df[df['InventoryDays'] > df['InventoryDays'].quantile(0.75)]
slow_movers.to_csv("output/slow_movers.csv", index=False)

# Save overstocked and low-sale items
overstocked = df[(df['InventoryDays'] > 90) & (df['UnitsSold'] < df['UnitsSold'].quantile(0.25))]
overstocked.to_csv("output/overstocked_items.csv", index=False)

print("✅ Analysis complete. Output saved in /output folder.")
