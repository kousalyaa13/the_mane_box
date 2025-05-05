from utils import identify_concerns

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
        
        # Identify 'Other' products
        others = [
            p for p in self.selected_products
            if all(x not in p.category.lower() for x in ["shampoo", "conditioner"]) or
               any(keyword in p.category.lower() for keyword in ["mask", "treatment", "leave-in", "serum", "spray", "oil", "combo", "2-in-1"])
        ]

        def print_section(title, products, tier_name):
            if products:
                print(f"\n{title} ({tier_name})")
                for p in products:
                    concerns = identify_concerns(p.description)
                    concern_text = f"  ➤ Targets: {', '.join(concerns)}" if concerns else "  ➤ Targets: General care"
                    print(f"- {p.brand} – {p.name}")
                    print(concern_text)

        print_section("🧴 Shampoos", shampoos, "within your budget")
        print_section("💧 Conditioners", conditioners, "within your budget")
        print_section("✨ Treatments & Styling", others, "within your budget")

        print("\n🧼 Enjoy your personalized hair care box!")