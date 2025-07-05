# Retail Business Performance & Profitability Analysis

## 📌 Project Objective
Analyze transactional retail data to:
- Identify profit-draining product categories
- Optimize inventory turnover
- Discover seasonal patterns in product sales

## 🧰 Tools & Technologies Used
- **SQL**: Data cleaning, category-wise profit analysis
- **Python (Pandas, Seaborn, Matplotlib)**: EDA, correlation analysis, charts
- **Streamlit**: Interactive dashboard with filters and visual insights
- **FPDF**: PDF report generation

## 📁 Folder Structure
```
Retail-Performance-Analysis/
├── data/
│   └── retail_data.csv
├── scripts/
│   └── retail_analysis.py
├── sql/
│   └── retail_analysis.sql
├── streamlit_app/
│   └── app.py
├── output/
│   ├── slow_movers.csv
│   ├── overstocked_items.csv
│   └── profit_vs_inventory.png
└── README.md
```

## 🔎 Key Features
- **Filterable Dashboard**: By Region, Category, and Season
- **Visuals**: Profit by Category, Inventory vs Profit, Seasonal Trends
- **Insights**: Slow-moving & overstocked products
- **Correlation**: Inventory Days ↔ Profitability

## 🚀 Getting Started
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit dashboard:
   ```bash
   streamlit run streamlit_app/app.py
   ```

## 📊 Deliverables
- ✅ Streamlit Dashboard
- ✅ SQL Queries (.sql)
- ✅ Python Analysis Script (.py)
- ✅ Summary Report (.pdf)
- ✅ Processed Data & Outputs (.csv)

## 📌 Conclusion
This project delivers deep insights into retail operations, enabling data-driven decisions to improve profit margins and inventory management.

