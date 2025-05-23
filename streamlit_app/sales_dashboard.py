import streamlit as st
import pandas as pd

st.title("Simple Sales Dashboard")

uploaded_file = st.file_uploader("Upload Sales CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    required = {"date", "product", "quantity", "price"}
    if required.issubset(df.columns):
        df["date"] = pd.to_datetime(df["date"])
        df["revenue"] = df["quantity"] * df["price"]

        st.subheader("Revenue per Product")
        revenue = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
        st.bar_chart(revenue)

        st.subheader("Sales Trend")
        trend = df.groupby("date")["revenue"].sum().sort_index()
        st.line_chart(trend)

        st.subheader("Top 5 Products by Revenue")
        top5 = revenue.head(5)
        st.bar_chart(top5)
    else:
        st.error("CSV must contain date, product, quantity, and price columns")
else:
    st.info("Please upload a CSV file")
