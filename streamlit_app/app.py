import streamlit as st
import pandas as pd

st.title("Sales Data Analyzer")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    required = {"date", "product", "quantity", "price"}
    if required.issubset(data.columns):
        data["date"] = pd.to_datetime(data["date"])
        data["revenue"] = data["quantity"] * data["price"]
        if "cost" in data.columns:
            data["profit"] = data["quantity"] * (data["price"] - data["cost"])
        else:
            data["profit"] = data["revenue"]

        st.sidebar.header("Filters")
        min_d, max_d = data["date"].min(), data["date"].max()
        start_date, end_date = st.sidebar.date_input("Date range", [min_d, max_d])
        if isinstance(start_date, tuple):
            start_date, end_date = start_date
        mask = (data["date"] >= pd.to_datetime(start_date)) & (
            data["date"] <= pd.to_datetime(end_date)
        )
        filtered = data.loc[mask]

        st.subheader("Total Revenue per Product")
        revenue_per_product = (
            filtered.groupby("product")["revenue"].sum().reset_index()
        )
        st.dataframe(revenue_per_product)

        if "region" in data.columns:
            st.subheader("Revenue by Region")
            region_rev = filtered.groupby("region")["revenue"].sum().reset_index()
            st.bar_chart(region_rev.set_index("region"))

        if "category" in data.columns:
            st.subheader("Profit by Category")
            cat_profit = filtered.groupby("category")["profit"].sum().reset_index()
            st.bar_chart(cat_profit.set_index("category"))

        st.subheader("Sales Trend Over Time")
        trend = filtered.groupby("date")["revenue"].sum().reset_index()
        trend.sort_values("date", inplace=True)
        st.line_chart(trend.set_index("date"))

        if "category" in data.columns:
            st.subheader("Revenue by Category Over Time")
            cat_trend = (
                filtered.groupby(["date", "category"])["revenue"].sum().reset_index()
            )
            cat_pivot = cat_trend.pivot(
                index="date", columns="category", values="revenue"
            ).fillna(0)
            cat_pivot.index = pd.to_datetime(cat_pivot.index)
            cat_pivot.sort_index(inplace=True)
            st.area_chart(cat_pivot)

        st.subheader("Top 5 Products by Profit")
        top_profit = (
            filtered.groupby("product")["profit"].sum().reset_index()
            .sort_values("profit", ascending=False)
            .head(5)
        )
        st.bar_chart(top_profit.set_index("product"))
    else:
        st.error(
            "CSV must contain at least date, product, quantity, and price columns"
        )
else:
    st.info("Please upload a CSV file to begin analysis")
