# Project 03 – Customer Churn / Sales Trend Analysis

## Business question
Which months and categories generate the most revenue, how concentrated is revenue among high-value customers, and what practical actions could a manager test?

## Dataset note
This project uses **generated synthetic practice data**, not real company sales or real customer records. It contains 2,400 fictional orders, 300 fictional customer IDs, four categories, and dates from January to December 2025. Revenue is in arbitrary synthetic units. A fixed random seed makes it reproducible.

## Requirements covered
- Date extraction: month, month name, weekday, and quarter.
- Monthly revenue and month-over-month growth using `pct_change()`.
- Category analysis using `groupby()` and a month-by-category `pivot_table()`.
- Top 10% customer revenue contribution (Pareto-style check).
- Four charts and a one-page business brief with three data-based recommendations.
- Basic data checks for shape, missing values, and duplicate order IDs.

## Run in Google Colab
1. Open https://colab.research.google.com/
2. Upload `Project_03_Customer_Sales_Analysis.ipynb`.
3. Select Runtime → Run all.

## Run locally
```bash
pip install -r requirements.txt
python analysis.py
```

## Files
- `Project_03_Customer_Sales_Analysis.ipynb` – explained notebook.
- `analysis.py` – standalone Python script.
- `data/ecommerce_orders_synthetic.csv` – generated dataset.
- `charts/` – revenue trend, category revenue, top customers, and category heatmap.
- `business_brief.md` and `business_brief.pdf` – one-page business summary.
- CSV summaries – monthly, category, pivot, and customer results.

## Limitation
Revenue is not profit. Costs, discounts, returns, and marketing costs are not included. Recommendations are hypotheses to test, not guaranteed outcomes.
