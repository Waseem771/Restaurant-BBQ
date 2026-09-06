"""Generate synthetic BBQ restaurant data to seed the database.

This script creates the 5 CSV files needed by load_data.py:
  - branches.csv
  - products.csv
  - customers.csv
  - orders.csv
  - order_items.csv

Run from project root:
  python generate_seed_data.py

Creates files in: ./dataset/
"""
from __future__ import annotations

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np


# Configuration
DATASET_DIR = Path(__file__).parent / "dataset"
DATASET_DIR.mkdir(exist_ok=True)

BRANCHES = [
    {"id": 1, "name": "Main Branch", "city": "Karachi", "popularity": 1.2},
    {"id": 2, "name": "North Branch", "city": "Lahore", "popularity": 1.0},
    {"id": 3, "name": "Downtown Branch", "city": "Islamabad", "popularity": 0.9},
]

PRODUCTS = [
    {"id": 1, "name": "BBQ Platter Mix", "category": "Platters", "price": 2500, "cost": 1100, "pop": 1.5},
    {"id": 2, "name": "Chicken Tikka", "category": "Main Course", "price": 1500, "cost": 650, "pop": 1.2},
    {"id": 3, "name": "Biryani", "category": "Rice Dishes", "price": 1200, "cost": 520, "pop": 1.1},
    {"id": 4, "name": "Seekh Kabab", "category": "Main Course", "price": 1800, "cost": 750, "pop": 1.3},
    {"id": 5, "name": "Nihari", "category": "Curry", "price": 1100, "cost": 480, "pop": 0.9},
    {"id": 6, "name": "Haleem", "category": "Curry", "price": 1300, "cost": 550, "pop": 1.0},
    {"id": 7, "name": "Shami Kabab", "category": "Appetizer", "price": 600, "cost": 240, "pop": 0.8},
    {"id": 8, "name": "Samosa Platter", "category": "Appetizer", "price": 500, "cost": 180, "pop": 0.7},
    {"id": 9, "name": "Lassi", "category": "Beverages", "price": 300, "cost": 80, "pop": 0.6},
    {"id": 10, "name": "Chai", "category": "Beverages", "price": 150, "cost": 40, "pop": 0.5},
    {"id": 11, "name": "Raita", "category": "Sides", "price": 200, "cost": 60, "pop": 0.4},
    {"id": 12, "name": "Naan", "category": "Bread", "price": 100, "cost": 30, "pop": 1.1},
    {"id": 13, "name": "Roti", "category": "Bread", "price": 80, "cost": 20, "pop": 0.9},
    {"id": 14, "name": "Dessert Plate", "category": "Desserts", "price": 400, "cost": 150, "pop": 0.7},
]

FIRST_NAMES = ["Ahmed", "Ali", "Fatima", "Sara", "Hassan", "Zainab", "Omar", "Aisha", "Rashid", "Layla"]
LAST_NAMES = ["Khan", "Ahmed", "Hassan", "Ali", "Ibrahim", "Mohammad", "Abdullah", "Malik", "Hussain", "Farooq"]

START_DATE = datetime(2026, 1, 1)
END_DATE = datetime(2026, 9, 30)


def generate_branches():
    """Write branches.csv"""
    path = DATASET_DIR / "branches.csv"
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["branch_id", "branch_name", "city", "popularity_weight"])
        writer.writeheader()
        for branch in BRANCHES:
            writer.writerow({
                "branch_id": branch["id"],
                "branch_name": branch["name"],
                "city": branch["city"],
                "popularity_weight": branch["popularity"],
            })
    print(f"✅ {path.name} ({len(BRANCHES)} rows)")


def generate_products():
    """Write products.csv"""
    path = DATASET_DIR / "products.csv"
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["product_id", "product_name", "category", "unit_price", "unit_cost", "popularity_weight"])
        writer.writeheader()
        for product in PRODUCTS:
            writer.writerow({
                "product_id": product["id"],
                "product_name": product["name"],
                "category": product["category"],
                "unit_price": product["price"],
                "unit_cost": product["cost"],
                "popularity_weight": product["pop"],
            })
    print(f"✅ {path.name} ({len(PRODUCTS)} rows)")


def generate_customers(count: int = 600):
    """Write customers.csv"""
    path = DATASET_DIR / "customers.csv"
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["customer_id", "customer_name", "phone", "signup_date"])
        writer.writeheader()
        for i in range(1, count + 1):
            first = random.choice(FIRST_NAMES)
            last = random.choice(LAST_NAMES)
            phone = f"0{random.randint(3000000000, 3999999999)}"
            signup = (START_DATE + timedelta(days=random.randint(0, 270))).strftime("%Y-%m-%d")
            writer.writerow({
                "customer_id": i,
                "customer_name": f"{first} {last}",
                "phone": phone,
                "signup_date": signup,
            })
    print(f"✅ {path.name} ({count} rows)")


def generate_orders_and_items(order_count: int = 19615):
    """Write orders.csv and order_items.csv"""
    orders_path = DATASET_DIR / "orders.csv"
    items_path = DATASET_DIR / "order_items.csv"

    orders_data = []
    items_data = []
    item_id = 1

    for order_id in range(1, order_count + 1):
        # Random date in range
        days_offset = random.randint(0, (END_DATE - START_DATE).days)
        order_date = (START_DATE + timedelta(days=days_offset)).strftime("%Y-%m-%d")

        # Weighted by day of week (weekends busier)
        dow = (START_DATE + timedelta(days=days_offset)).weekday()
        is_weekend = dow >= 4  # Friday, Saturday

        # Branch & customer
        branch_id = random.choices(
            [1, 2, 3],
            weights=[1.2, 1.0, 0.9],
            k=1
        )[0]
        customer_id = random.randint(1, 600)

        # Items per order (1-5, weighted)
        item_count = random.choices([1, 2, 3, 4, 5], weights=[10, 20, 30, 25, 15])[0]

        order_total = 0
        for _ in range(item_count):
            product = random.choice(PRODUCTS)
            qty = random.randint(1, 3)
            discount_pct = random.choices([0, 5, 10], weights=[80, 15, 5])[0]

            unit_price = product["price"]
            line_total = qty * unit_price * (1 - discount_pct / 100)
            order_total += line_total

            items_data.append({
                "order_item_id": item_id,
                "order_id": order_id,
                "product_id": product["id"],
                "quantity": qty,
                "unit_price": unit_price,
                "discount_pct": discount_pct,
                "line_total": round(line_total, 2),
            })
            item_id += 1

        orders_data.append({
            "order_id": order_id,
            "order_date": order_date,
            "branch_id": branch_id,
            "customer_id": customer_id,
            "total_amount": round(order_total, 2),
        })

    # Write orders
    with open(orders_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["order_id", "order_date", "branch_id", "customer_id", "total_amount"])
        writer.writeheader()
        writer.writerows(orders_data)
    print(f"✅ {orders_path.name} ({len(orders_data)} rows)")

    # Write order items
    with open(items_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["order_item_id", "order_id", "product_id", "quantity", "unit_price", "discount_pct", "line_total"])
        writer.writeheader()
        writer.writerows(items_data)
    print(f"✅ {items_path.name} ({len(items_data)} rows)")


def main():
    print("\n🍖 Generating BBQ Restaurant Seed Data\n")
    print(f"📁 Output directory: {DATASET_DIR}\n")

    generate_branches()
    generate_products()
    generate_customers()
    generate_orders_and_items()

    print("\n✅ All CSV files generated successfully!")
    print(f"\nNext step: python run.py")


if __name__ == "__main__":
    main()
