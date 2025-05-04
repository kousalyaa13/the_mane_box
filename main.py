import csv
import os
import re
from user import User
from product import Product
from subscription_box import SubscriptionBox
from utils import match_concerns, match_exclusions

def load_products(filepath="data/products.csv"):
    if not os.path.exists(filepath):
        print(f"Error: Product file not found at {filepath}")
        return []

    products = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not row["price"] or not row["name"]:  # skip incomplete rows
                continue
            try:
                price = float(row["price"])
            except ValueError:
                print(f"Skipping product with invalid price: {row}")
                continue

            products.append(Product(
                row["name"],
                row["category"],
                row["brand"],
                price,
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

def run_mane_box():
    products = load_products()
    if not products:
        return

    while True:
        print("\n--- Welcome to The Mane Box ---")

        name = input("Enter your name: ")
        hair_texture = input("Hair texture (straight, wavy, curly, coily): ").lower().strip()
        hair_type = input("Hair type (fine, medium, thick): ").lower().strip()
        concerns = [c.strip() for c in input("Hair concerns (comma-separated): ").lower().split(',')]
        try:
            budget = float(input("Max budget for individual products: $").strip())
        except ValueError:
            print("Invalid budget input. Please enter a valid number.")
            continue
        exclusions = [e.strip() for e in input("Any exclusions (e.g., sulfate-free, vegan)? (comma-separated): ").lower().split(',')]

        user = User(name, hair_texture, hair_type, concerns, budget, exclusions)
        recommended = recommend_products(user, products)

        if not recommended:
            print("\nSorry, no matching products found for your preferences.")
        else:
            box = SubscriptionBox(user)
            for product in recommended[:3]:  # Limit to 3 products
                box.add_product(product)
            box.display_box()

        again = input("\nWould you like to create another box? (yes/no): ").lower().strip()
        if again != "yes":
            print("Thanks for using The Mane Box!")
            break

# Run the program
if __name__ == "__main__":
    run_mane_box()