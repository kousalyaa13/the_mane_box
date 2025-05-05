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

    def get_valid_input(prompt, options):
        while True:
            value = input(prompt).strip().lower()
            if value in options:
                return value
            print(f"❌ Invalid input. Choose from: {', '.join(options)}")

    def get_yes_no(prompt):
        while True:
            value = input(prompt).strip().lower()
            if value in ["yes", "no"]:
                return value == "yes"
            print("❌ Please enter 'yes' or 'no'.")

    hair_texture = get_valid_input("Hair texture (straight, wavy, curly, coily): ", ["straight", "wavy", "curly", "coily"])
    hair_type = get_valid_input("Hair type (fine, medium, thick): ", ["fine", "medium", "thick"])

    concerns = []

    # Granular questions
    if get_yes_no("Is your hair color-treated? (yes/no): "):
        concerns.append("color-treated")
    if get_yes_no("Do you have dandruff or scalp issues? (yes/no): "):
        concerns.append("dandruff")
    if get_yes_no("Do you use heat styling tools regularly? (yes/no): "):
        concerns.append("heat damage")
    if get_yes_no("Would you want more volume in your hair? (yes/no): "):
        concerns.append("volume")
    if get_yes_no("Do you prefer clean or vegan products? (yes/no): "):
        concerns.append("vegan")

    # Ask for any additional concerns
    extra = input("Any other hair concerns you'd like to address? (dryness, frizz, oiliness — comma-separated): ")
    concerns += [c.strip().lower() for c in extra.split(",") if c.strip()]

    # Budget
    while True:
        try:
            budget = float(input("Max budget per product (in $): ").strip())
            break
        except ValueError:
            print("❌ Please enter a valid number (ex: 20 or 15.99).")

    # Exclusions
    exclusions = input("Any product exclusions (sulfates, parabens, fragrances — comma-separated): ").lower().split(',')

    # Build user + recommend
    user = User(name, hair_texture, hair_type, concerns, budget, exclusions)
    recommended = recommend_products(user, products)

    if not recommended:
        print("\n😔 Sorry, no matching products found within your preferences and budget.")
        return

    # Build the box
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