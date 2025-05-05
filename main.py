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

def recommend_products(user, all_products, avoid_concerns):
    matches = []
    for product in all_products:
        if match_concerns(product.description, user.concerns):
            if not match_concerns(product.description, avoid_concerns):  # exclude unwanted concerns
                if not match_exclusions(product.description, user.exclusions):
                    if product.price <= user.budget:
                        matches.append(product)
    random.shuffle(matches)
    return matches

def run_mane_box():
    products = load_products()
    if not products:
        print("⚠️ Could not load product data.")
        return

    print("\n\n--- Welcome to The Mane Box ---")

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
    avoid_concerns = []

    # Granular questions
    if get_yes_no("Do you have color-treated hair? (yes/no): "):
        concerns.append("color-treated")
    else:
        avoid_concerns.append("color-treated")
    if get_yes_no("Do you have dandruff or scalp issues? (yes/no): "):
        concerns.append("dandruff")
        concerns.append("buildup")
    else:
        avoid_concerns.append("dandruff")
        avoid_concerns.append("buildup")

    if get_yes_no("Do you use heat styling tools regularly? (yes/no): "):
        concerns.append("heat damage")
    else:
        avoid_concerns.append("heat damage")

    if get_yes_no("Would you want more volume in your hair? (yes/no): "):
        concerns.append("volume")
    else:
        avoid_concerns.append("volume")

    if get_yes_no("Do you prefer clean or vegan products? (yes/no): "):
        concerns.append("vegan")
    else:
        avoid_concerns.append("vegan")

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
    raw_exclusions = input("Any product exclusions (sulfates, parabens, fragrances — comma-separated): ").strip().lower()

    if raw_exclusions in ["no", "n/a", "none", ""]:
        exclusions = []
    else:
        exclusions = [e.strip() for e in raw_exclusions.split(',') if e.strip()]

    # Build user + recommend
    user = User(name, hair_texture, hair_type, concerns, budget, exclusions)
    recommended = recommend_products(user, products, avoid_concerns)

    if not recommended:
        print("\n😔 Sorry, no matching products found within your preferences and budget.")
        return

    # Build the box
    box = SubscriptionBox(user)
    shampoos = [p for p in recommended if "shampoo" in p.category.lower()]
    conditioners = [p for p in recommended if "conditioner" in p.category.lower()]
    
    others = [
    p for p in recommended
    if not any(keyword in p.category.lower() for keyword in ["shampoo", "conditioner"]) and
       any(keyword in p.category.lower() for keyword in ["mask", "treatment", "leave-in", "serum", "spray", "oil", "combo", "2-in-1"])]
    

    for product in shampoos[:5]:
        box.add_product(product)
    for product in conditioners[:5]:
        box.add_product(product)
    for product in others[:5]:
        if product not in box.selected_products:
            box.add_product(product)

    box.display_box()
    print("💖 Thank you for using The Mane Box!")

if __name__ == "__main__":
    run_mane_box()