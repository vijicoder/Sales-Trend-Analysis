"""Project 03: Customer Sales Trend Analysis (synthetic practice data)."""
from pathlib import Path
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent
(ROOT / "data").mkdir(exist_ok=True)
(ROOT / "charts").mkdir(exist_ok=True)

rng = np.random.default_rng(2026)
n_orders, n_customers = 2400, 300
dates = pd.date_range("2025-01-01", "2025-12-31", freq="D")
ids = np.arange(1001, 1001 + n_customers)
weights = rng.lognormal(0, 0.65, n_customers)
weights /= weights.sum()
order_dates = pd.to_datetime(rng.choice(dates, n_orders))
customer_ids = rng.choice(ids, n_orders, p=weights)
categories = ["Electronics", "Fashion", "Home", "Books"]
picked_categories = rng.choice(categories, n_orders, p=[.27, .36, .22, .15])
m = order_dates.month
season = np.select([m == 11, m == 12, np.isin(m, [5, 6]), np.isin(m, [1, 2])],
                   [1.45, 1.30, 1.12, .92], default=1.0)
base = pd.Series(picked_categories).map(
    {"Electronics": 2600, "Fashion": 950, "Home": 1700, "Books": 450}
).to_numpy()
amount = np.round(rng.gamma(2.1, base / 2.1) * season, 2)

orders = pd.DataFrame({
    "order_id": [f"ORD{i:05d}" for i in range(1, n_orders + 1)],
    "order_date": order_dates, "customer_id": customer_ids,
    "category": picked_categories, "amount": amount
}).sort_values("order_date").reset_index(drop=True)

# Basic data quality checks.
print("Dataset shape:", orders.shape)
print("Missing values:\\n", orders.isna().sum())
print("Duplicate order IDs:", orders.order_id.duplicated().sum())

# Feature engineering: extract useful date parts.
orders["month"] = orders.order_date.dt.to_period("M").astype(str)
orders["month_name"] = orders.order_date.dt.strftime("%b")
orders["weekday"] = orders.order_date.dt.day_name()
orders["quarter"] = orders.order_date.dt.to_period("Q").astype(str)
orders.to_csv(ROOT / "data" / "ecommerce_orders_synthetic.csv", index=False)

# Monthly trend and month-over-month percentage change.
monthly = orders.groupby("month").agg(revenue=("amount", "sum"),
                                      orders=("order_id", "count"))
monthly["mom_growth_pct"] = monthly.revenue.pct_change() * 100
print("\\nMonthly trend:\\n", monthly.round(2))
best_month = monthly.revenue.idxmax()

ax = monthly.revenue.plot(marker="o", figsize=(10, 5),
                          title="Monthly e-commerce revenue")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (synthetic units)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(ROOT / "charts" / "01_monthly_revenue_trend.png", dpi=160)
plt.close()

# Category groupby and month-by-category pivot table.
category_summary = orders.groupby("category").amount.agg(
    total_revenue="sum", average_order_value="mean", order_count="count"
).sort_values("total_revenue", ascending=False)
category_summary["revenue_share_pct"] = (
    category_summary.total_revenue / orders.amount.sum() * 100
)
pivot = pd.pivot_table(orders, values="amount", index="month",
                       columns="category", aggfunc="sum", fill_value=0)
print("\\nCategory summary:\\n", category_summary.round(2))
print("\\nMonthly category pivot:\\n", pivot.round(2))

category_summary.total_revenue.sort_values().plot(
    kind="barh", figsize=(8, 5), title="Revenue by product category")
plt.xlabel("Revenue (synthetic units)")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(ROOT / "charts" / "02_revenue_by_category.png", dpi=160)
plt.close()

# Top 10% customer revenue contribution (Pareto-style analysis).
spend = orders.groupby("customer_id").amount.sum().sort_values(ascending=False)
top_n = math.ceil(len(spend) * 0.10)
top_share = spend.head(top_n).sum() / orders.amount.sum() * 100
print(f"\\nTop {top_n} customers contribute {top_share:.1f}% of revenue.")

top10 = spend.head(10)
top10.sort_values().plot(kind="barh", figsize=(8, 5),
                         title="Top 10 customers by total spend")
plt.xlabel("Customer spend (synthetic units)")
plt.ylabel("Customer ID")
plt.tight_layout()
plt.savefig(ROOT / "charts" / "03_top_customers.png", dpi=160)
plt.close()

# Monthly category heatmap.
fig, ax = plt.subplots(figsize=(11, 6))
image = ax.imshow(pivot.values, aspect="auto")
ax.set_xticks(range(len(pivot.columns)), pivot.columns, rotation=25, ha="right")
ax.set_yticks(range(len(pivot.index)), pivot.index)
ax.set_title("Monthly revenue by product category")
ax.set_xlabel("Category")
ax.set_ylabel("Month")
fig.colorbar(image, ax=ax, label="Revenue (synthetic units)")
fig.tight_layout()
fig.savefig(ROOT / "charts" / "04_month_category_heatmap.png", dpi=160)
plt.close(fig)

# Export summary tables for checking and reuse.
monthly.to_csv(ROOT / "monthly_revenue_summary.csv")
category_summary.to_csv(ROOT / "category_summary.csv")
pivot.to_csv(ROOT / "monthly_category_pivot.csv")
top10.rename("total_spend").to_csv(ROOT / "top_10_customers.csv")
print("Analysis complete. Open business_brief.md for the findings and recommendations.")
