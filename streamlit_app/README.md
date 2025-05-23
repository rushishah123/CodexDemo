# Streamlit Sales Dashboard

This enhanced Streamlit app analyzes company sales data and provides several interactive visualizations.

Features:
- **Total revenue per product**
- **Sales trend over time**
- **Top 5 best-selling products**
- **Revenue by region**
- **Profit by category**

Sample datasets are included:
- `sample_sales.csv` – simple example with 50 rows.
- `sample_sales_generated.csv` – generated via `generate_sample_csv.py` (also 50 rows).
- `company_sales.csv` – a larger file with 200 rows containing `region`, `category`, `price` and `cost` columns.

You can run the lightweight dashboard using `sales_dashboard.py`:
```bash
streamlit run sales_dashboard.py
```

To run the app:
```bash
pip install -r requirements.txt
streamlit run app.py
```
