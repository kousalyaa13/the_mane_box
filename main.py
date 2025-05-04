import csv
import re
from user import User
from product import Product
from subscription_box import SubscriptionBox
from utils import match_concerns, match_exclusions

def load_products(filepath="data/products.csv"):
    products = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append(Product(
                row["name"],
                row["category"],
                row["brand"],
                float(row["price"]),
                row["description"]
            ))
    return products

def recommend_products(user, all_products):
    matches = []
    for product in all_products:
        if match_concerns(product.description, user.concerns) and not match_exclusions(product.description, user.exclusions):
            if product.price <= user.budget:
                matches.append(product)
    return matches

name = input("Enter your name: ")
hair_type = input("Hair type (curly, straight, wavy, color-treated): ").lower()
concerns = input("Hair concerns (comma-separated): ").lower().split(',')
budget = float(input("Max budget for individual products: $"))
exclusions = input("Any exclusions (e.g., sulfate-free, vegan)? (comma-separated): ").lower().split(',')

user = User(name, hair_type, concerns, budget, exclusions)
products = load_products()
recommended = recommend_products(user, products)

box = SubscriptionBox(user)
for product in recommended[:3]:  # Limit to 3–4 items
    box.add_product(product)
box.display_box()
