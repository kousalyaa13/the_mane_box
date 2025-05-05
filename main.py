import csv
import os
import re
from user import User
from product import Product
from subscription_box import SubscriptionBox
from utils import match_concerns, match_exclusions

def load_products(filepath="data\cleaned_mane_box_data.csv"):
    if not os.path.exists(filepath):
        print(f"Error: Product file not found at {filepath}")
        return []

    products = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            products.append(Product(
                row["name"],
                row["category"],
                row["brand"],
                row["description"]
            ))
    return products

def recommend_products(user, all_products):
    matches = []
    for product in all_products:
        if match_concerns(product.description, user.concerns) and not match_exclusions(product.description, user.exclusions):
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
            
            shampoos = [p for p in recommended if "shampoo" in p.category.lower()]
            conditioners = [p for p in recommended if "conditioner" in p.category.lower()]

            for product in shampoos[:5]:
                box.add_product(product)

            for product in conditioners[:5]:
                box.add_product(product)
            box.display_box()

        again = input("\nWould you like to create another box? (yes/no): ").lower().strip()
        if again != "yes":
            print("Thanks for using The Mane Box!")
            break

# Run the program
if __name__ == "__main__":
    run_mane_box()