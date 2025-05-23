import streamlit as st
import pandas as pd

st.title("Sales Data Analyzer")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    if {'date', 'product', 'quantity', 'price'}.issubset(data.columns):
        data['revenue'] = data['quantity'] * data['price']

        st.subheader("Total Revenue per Product")
        revenue_per_product = data.groupby('product')['revenue'].sum().reset_index()
        st.dataframe(revenue_per_product)

        st.subheader("Sales Trend Over Time")
        trend = data.groupby('date')['revenue'].sum().reset_index()
        trend['date'] = pd.to_datetime(trend['date'])
        trend.sort_values('date', inplace=True)
        st.line_chart(trend.set_index('date'))

        st.subheader("Top 5 Best-Selling Products")
        top_products = revenue_per_product.sort_values('revenue', ascending=False).head(5)
        st.bar_chart(top_products.set_index('product'))
    else:
        st.error("CSV must contain date, product, quantity, and price columns")
else:
    st.info("Please upload a CSV file to begin analysis")
