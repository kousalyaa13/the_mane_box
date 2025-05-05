import csv
import random
from user import User
from product import Product
from subscription_box import SubscriptionBox
from utils import match_concerns, match_exclusions

def load_products(filepath="data/cleaned_mane_box_data_with_price_tiers.csv"):
    products = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append(Product(
                name=row["name"],
                category=row["category"],
                brand=row["brand"],
                description=row["description"],
                price=float(row["price"])  # Now includes price
            ))
    return products

def recommend_products(user, all_products):
    matches = []
    for product in all_products:
        if match_concerns(product.description, user.concerns) and not match_exclusions(product.description, user.exclusions):
            if product.price <= user.budget:
                matches.append(product)
    random.shuffle(matches)  # Randomize output
    return matches

def run_mane_box():
    products = load_products()
    if not products:
        print("⚠️ Could not load product data.")
        return

    print("\n--- Welcome to The Mane Box ---")

    name = input("Enter your name: ").strip()

    valid_textures = ["straight", "wavy", "curly", "coily"]
    valid_types = ["fine", "medium", "thick"]

    while True:
        hair_texture = input("Hair texture (straight, wavy, curly, coily): ").lower().strip()
        if hair_texture in valid_textures:
            break
        print("❌ Invalid texture. Choose from: straight, wavy, curly, coily.")

    while True:
        hair_type = input("Hair type (fine, medium, thick): ").lower().strip()
        if hair_type in valid_types:
            break
        print("❌ Invalid type. Choose from: fine, medium, thick.")

    concerns = input("Hair concerns (e.g., dryness, frizz, split ends — comma-separated): ").lower().split(',')

    # specific new  questions
    if input("Is your hair color-treated? (yes/no): ").strip().lower() == "yes":
        concerns.append("color-safe")
    if input("Do you have dandruff or scalp issues? (yes/no): ").strip().lower() == "yes":
        concerns.append("dandruff")
    if input("Do you use heat styling tools regularly? (yes/no): ").strip().lower() == "yes":
        concerns.append("heat protection")
    if input("Do you want more volume in your hair? (yes/no): ").strip().lower() == "yes":
        concerns.append("volume")
    if input("Do you prefer clean or vegan products? (yes/no): ").strip().lower() == "yes":
        concerns.append("vegan")

    while True:
        try:
            budget = float(input("Max budget per product (in $): ").strip())
            break
        except ValueError:
            print("❌ Please enter a valid number (e.g., 20 or 15.99).")

    exclusions = input("Any product exclusions (e.g., sulfates, parabens — comma-separated): ").lower().split(',')

    user = User(name, hair_texture, hair_type, concerns, budget, exclusions)
    recommended = recommend_products(user, products)

    if not recommended:
        print("\n😔 Sorry, no matching products found within your preferences and budget.")
        return

    box = SubscriptionBox(user)
    shampoos = [p for p in recommended if "shampoo" in p.category.lower()]
    conditioners = [p for p in recommended if "conditioner" in p.category.lower()]

    for product in shampoos[:5]:
        box.add_product(product)
    for product in conditioners[:5]:
        box.add_product(product)

    box.display_box()
    print("💖 Thank you for using The Mane Box!")

if __name__ == "__main__":
    run_mane_box()