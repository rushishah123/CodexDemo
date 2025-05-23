# Streamlit Sales Dashboard

This simple Streamlit app allows you to upload a CSV file containing sales data and displays a few basic analytics:

- **Total revenue per product**
- **Sales trend over time** (line chart)
- **Top 5 best-selling products** (bar chart)

A sample CSV file named `sample_sales.csv` is included for demonstration. It contains 50 rows with the following columns:
`date`, `product`, `quantity`, and `price`.

To run the app:

```bash
pip install -r requirements.txt
streamlit run app.py
```
