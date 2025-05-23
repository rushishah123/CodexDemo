"""Utility script for generating simple sales reports."""

from __future__ import annotations

import datetime
import os
from pathlib import Path
from typing import Tuple

import matplotlib.pyplot as plt
import pandas as pd

OUTPUT_CSV = Path("output.csv")
BARGRAPH_PNG = Path("bargraph.png")
LAST_30_DAYS_CSV = Path("last_30_days.csv")
DAILY_PNG = Path("daily.png")
TAXED_CSV = Path("taxed.csv")
SUMMARY_CSV = Path("summary.csv")


def compute_total_revenue(file_path: str) -> pd.DataFrame:
    """Aggregate revenue per product and save a bar chart."""
    df = pd.read_csv(file_path)
    totals = df.groupby("Product")["Revenue"].sum().reset_index()
    totals.columns = ["ProductName", "TotalRev"]
    totals.to_csv(OUTPUT_CSV, index=False)

    plt.bar(totals["ProductName"], totals["TotalRev"])
    plt.savefig(BARGRAPH_PNG)
    return totals

def get_most_profitable_product(file_path: str) -> Tuple[str, float]:
    """Return the most profitable product and its revenue."""
    df = pd.read_csv(file_path)
    grouped = df.groupby("Product")["Revenue"].sum()
    return grouped.idxmax(), grouped.max()

def filter_last_30_days(file_path: str) -> pd.DataFrame:
    """Filter the sales data to the last 30 days."""
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])
    last_month = datetime.datetime.now() - datetime.timedelta(days=30)
    filtered = df[df["Date"] >= last_month]
    filtered.to_csv(LAST_30_DAYS_CSV, index=False)
    return filtered

def plot_sales(file_path: str) -> None:
    """Generate a daily revenue plot."""
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])
    daily = df.groupby("Date")["Revenue"].sum().sort_index()
    daily.plot()
    plt.title("Daily Revenue")
    plt.savefig(DAILY_PNG)

def calculate_tax_and_net(file_path: str) -> pd.DataFrame:
    """Calculate tax and net revenue for each row."""
    df = pd.read_csv(file_path)
    df["Tax"] = df["Revenue"] * 0.18
    df["Net"] = df["Revenue"] - df["Tax"]
    df.to_csv(TAXED_CSV, index=False)
    return df


def generate_product_summary(file_path: str) -> pd.DataFrame:
    """Generate summary statistics per product."""
    df = pd.read_csv(file_path)
    summary = df.groupby("Product")["Revenue"].agg(["sum", "count", "mean"])
    summary.to_csv(SUMMARY_CSV)
    return summary

def main(file_path: str = "salesdata.csv") -> None:
    """Run a simple reporting workflow on the given CSV file."""
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    print("File exists. Proceeding.")
    compute_total_revenue(file_path)
    filter_last_30_days(file_path)
    plot_sales(file_path)
    get_most_profitable_product(file_path)
    calculate_tax_and_net(file_path)
    generate_product_summary(file_path)


if __name__ == "__main__":
    main()
