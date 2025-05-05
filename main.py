import csv
import random
from user import User
from product import Product
from subscription_box import SubscriptionBox
from utils import match_concerns, match_exclusions

def load_products(filepath):
    """
    Loads product data from a CSV file and returns a list of Product objects.
    
    Args:
        filepath (str): Path to the CSV file.

    Returns:
        list: List of Product objects.
    """
    products = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append(Product(
                name=row["name"],
                category=row["category"].lower(),
                brand=row["brand"],
                description=row["description"],
                price_tier=row.get("price_tier", "mid-range")
            ))
    return products

def recommend_products(user, all_products, avoid_concerns):
    """
    Filters products based on user's preferences and exclusions.
    
    Args:
        user (User): The user with preferences.
        all_products (list): All loaded products.
        avoid_concerns (list): Concerns to avoid.

    Returns:
        list: Filtered list of Product objects matching preferences.
    """
    matches = []
    for product in all_products:
        # Check if the product is within budget and matches the user's hair type and texture
        if match_concerns(product.description, user.concerns):
            if not match_concerns(product.description, avoid_concerns):
                if not match_exclusions(product.description, user.exclusions):
                    matches.append(product)
    # Shuffle the matches to randomize the order
    random.shuffle(matches)
    return matches

def run_mane_box():
    """
    Main function to run the Mane Box recommendation system.
    Gathers user input, filters products, and prints results.
    """
    print("\n\n--- Welcome to The Mane Box ---")

    # Load data
    main_products = load_products("data/cleaned_mane_box_data_with_price_tiers.csv")
    treatment_products = load_products("data/cleaned_treatments_data.csv")
    all_products = main_products + treatment_products

    name = input("Enter your name: ").strip()

    def get_valid_input(prompt, options):
        """Get a valid input from the user that matches available options."""
        while True:
            value = input(prompt).strip().lower()
            if value in options:
                return value
            print(f"❌ Invalid input. Choose from: {', '.join(options)}")

    def get_yes_no(prompt):
        """Get a yes or no input from the user."""
        while True:
            value = input(prompt).strip().lower()
            if value in ["yes", "no"]:
                return value == "yes"
            print("❌ Please enter 'yes' or 'no'.")

    # Hair details
    hair_texture = get_valid_input("Hair texture (straight, wavy, curly, coily): ", ["straight", "wavy", "curly", "coily"])
    hair_type = get_valid_input("Hair type (fine, medium, thick): ", ["fine", "medium", "thick"])

    concerns = []
    avoid_concerns = []

    # Granular preference filters
    if get_yes_no("Do you have color-treated hair? (yes/no): "):
        concerns.append("color-treated")
    else:
        avoid_concerns.append("color-treated")

    if get_yes_no("Do you have dandruff or scalp issues? (yes/no): "):
        concerns.extend(["dandruff", "buildup"])
    else:
        avoid_concerns.extend(["dandruff", "buildup"])

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

    # Additional custom concerns
    extra = input("Any other hair concerns you'd like to address? (dryness, frizz, oiliness, etc — comma-separated or 'N/A'): ").strip()
    if extra.lower() not in ["n/a", "none", "no"]:
        concerns += [c.strip().lower() for c in extra.split(",") if c.strip()]

    # Budget
    while True:
        try:
            budget = float(input("Max budget per product (in $): ").strip())
            break
        except ValueError:
            print("❌ Please enter a valid number (ex: 25, 45.50)")

    # Exclusions
    raw_exclusions = input("Any product exclusions (sulfates, parabens, fragrances, etc — comma-separated or 'N/A'): ").strip().lower()
    exclusions = [] if raw_exclusions in ["no", "n/a", "none", ""] else [e.strip() for e in raw_exclusions.split(',') if e.strip()]

    # Create user profile and get recommendations
    user = User(name, hair_texture, hair_type, concerns, budget, exclusions)
    recommended = recommend_products(user, all_products, avoid_concerns)

    if not recommended:
        print("\n😔 Sorry, no matching products found within your preferences and budget.")
        return

    # Categorize and fill subscription box
    box = SubscriptionBox(user)
    shampoos = [p for p in recommended if "shampoo" in p.category]
    conditioners = [p for p in recommended if "conditioner" in p.category]
    others = [
        p for p in recommended
        if not any(keyword in p.category for keyword in ["shampoo", "conditioner"]) and
           any(keyword in p.category for keyword in ["mask", "treatment", "leave-in", "serum", "spray", "oil", "combo", "2-in-1"])
    ]

    for product in shampoos[:3]:
        box.add_product(product)
    for product in conditioners[:3]:
        box.add_product(product)
    for product in others[:3]:
        if product not in box.selected_products:
            box.add_product(product)

    box.display_box()
    print("\n📦 Your Mane Box is curated with love and care to suit your unique hair needs.")
    print("💖 Thank you for using The Mane Box!")

if __name__ == "__main__":
    run_mane_box()