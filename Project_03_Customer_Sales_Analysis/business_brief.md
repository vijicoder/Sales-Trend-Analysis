# Customer Sales Trend Analysis — Business Brief

## Context
This project analyses a **generated synthetic e-commerce dataset** with 2,400 fictional orders from 293 fictional customer IDs across four categories, covering January–December 2025. No real customer data was used. Revenue is measured in arbitrary synthetic units, not real currency.

## Key findings
- **Total revenue:** 3,694,802.89 across 2,400 orders; average order value: 1,539.50.
- **Monthly trend:** December had the highest revenue (431,544.80); March had the lowest (240,161.71).
- **Category performance:** Electronics ranked first, contributing 45.8% of revenue.
- **Customer concentration:** The top 10% of customers (30 customers) contributed 31.8% of revenue.
- Month-over-month growth is calculated with `pct_change()`. January has no previous month, so its growth is blank.

## Recommendations
1. **Prepare for the peak month:** Plan stock and campaign capacity ahead of December. Check more years of data before assuming this seasonal pattern repeats.
2. **Monitor the leading category:** Electronics contributes 45.8% of revenue. Check stock availability, profit margin, and return rate before increasing investment.
3. **Test a retention offer:** The top 10% of customers contribute 31.8% of revenue. Test a modest loyalty offer and compare repeat purchases and incremental revenue against a control group.

## Next steps
Add product costs, discounts, returns, and marketing channels to measure profit rather than revenue. Validate the patterns using multiple years of permissioned real data.

## Data note
**Generated / synthetic practice data.** Customer IDs and order values are fictional. A fixed random seed makes the dataset reproducible. Results demonstrate an analysis workflow and are not claims about a real business.
