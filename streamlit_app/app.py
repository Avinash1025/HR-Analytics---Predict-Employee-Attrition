import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and preprocess data
@st.cache_data
def load_data():
    df = pd.read_csv("data/retail_data.csv")
    df['Profit'] = (df['UnitPrice'] - df['UnitCost']) * df['UnitsSold']
    df['ProfitMargin'] = (df['UnitPrice'] - df['UnitCost']) / df['UnitPrice']
    return df

df = load_data()

# Sidebar filters
st.sidebar.title("Filters")
region_filter = st.sidebar.multiselect("Select Region(s)", df['Region'].unique(), default=df['Region'].unique())
category_filter = st.sidebar.multiselect("Select Category", df['Category'].unique(), default=df['Category'].unique())
season_filter = st.sidebar.multiselect("Select Season", df['Season'].unique(), default=df['Season'].unique())

# Apply filters
filtered_df = df[
    df['Region'].isin(region_filter) &
    df['Category'].isin(category_filter) &
    df['Season'].isin(season_filter)
]

st.title("Retail Performance & Profitability Dashboard")
st.markdown("### Overview")
st.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")
st.metric("Average Inventory Days", f"{filtered_df['InventoryDays'].mean():.2f} days")
st.metric("Top Profit Category", filtered_df.groupby('Category')['Profit'].sum().idxmax())

# Bar chart: Profit by Category
st.markdown("### Profit by Category")
category_profit = filtered_df.groupby('Category')['Profit'].sum().sort_values()
fig1, ax1 = plt.subplots()
category_profit.plot(kind='barh', color='skyblue', ax=ax1)
ax1.set_xlabel("Profit")
ax1.set_title("Total Profit by Category")
st.pyplot(fig1)

# Scatter plot: Inventory Days vs Profit
st.markdown("### Inventory Days vs Profit")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_df, x='InventoryDays', y='Profit', hue='Category', ax=ax2)
ax2.set_title('Inventory Days vs Profit')
st.pyplot(fig2)

# Line chart: Units Sold Over Time
st.markdown("### Units Sold Over Time")
filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])
time_series = filtered_df.groupby(pd.Grouper(key='Date', freq='M'))['UnitsSold'].sum()
fig3, ax3 = plt.subplots()
time_series.plot(ax=ax3)
ax3.set_title("Monthly Units Sold")
ax3.set_ylabel("Units Sold")
ax3.set_xlabel("Month")
st.pyplot(fig3)

# Display slow-moving products
st.markdown("### Slow-Moving Products (Top 10)")
slow_movers = filtered_df[filtered_df['InventoryDays'] > filtered_df['InventoryDays'].quantile(0.75)]
st.dataframe(slow_movers[['ProductName', 'Category', 'InventoryDays', 'Profit']].sort_values(by='InventoryDays', ascending=False).head(10))
