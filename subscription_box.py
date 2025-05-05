from utils import identify_concerns  # if using separate file

class SubscriptionBox:
    def __init__(self, user):
        self.user = user
        self.selected_products = []

    def add_product(self, product):
        self.selected_products.append(product)

    def display_box(self):
        print(f"\n🎁 {self.user.name}'s Custom Mane Box:")

        shampoos = [p for p in self.selected_products if "shampoo" in p.category.lower()]
        conditioners = [p for p in self.selected_products if "conditioner" in p.category.lower()]
        others = [p for p in self.selected_products if p not in shampoos + conditioners]

        def print_section(title, products):
            if products:
                print(f"\n{title}")
                for p in products:
                    concerns = identify_concerns(p.description)
                    print(f"- {p.name} ({p.brand})")
                    if concerns:
                        print(f"  ➤ Targets: {', '.join(concerns)}")
                    else:
                        print("  ➤ Targets: General hair care")

        print_section("🧴 Shampoos:", shampoos)
        print_section("💧 Conditioners:", conditioners)
        print_section("✨ Other Products:", others)

        print("\n🧼 Enjoy your hair care picks!")
        print("💖 Thank you for using The Mane Box!")