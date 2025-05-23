import csv
import random
from datetime import datetime, timedelta

random.seed(42)
products = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett"]

start_date = datetime(2024, 1, 1)
rows = []
for i in range(50):
    date = start_date + timedelta(days=i)
    product = random.choice(products)
    quantity = random.randint(1, 10)
    price = random.randint(10, 100)
    rows.append([date.strftime("%Y-%m-%d"), product, quantity, price])

with open("sample_sales_generated.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "product", "quantity", "price"])
    writer.writerows(rows)

print("Generated sample_sales_generated.csv with 50 rows")
