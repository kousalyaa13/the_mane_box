from utils import identify_concerns

class SubscriptionBox:
    """
    Represents a personalized haircare subscription box for a user.
    
    Attributes:
        user (User): The user for whom the box is curated.
        selected_products (list): List of selected Product objects for the user.
    """
    
    def __init__(self, user):
        self.user = user
        self.selected_products = []

    def add_product(self, product):
        """
        Adds a product to the subscription box.

        Args:
            product (Product): The product to add to the box.
        """
        self.selected_products.append(product)

    def display_box(self):
        """
        Displays the curated haircare box organized by product category (Shampoo, Conditioner, Others).
        Also includes key concerns that each product addresses.
        """
        print(f"\n🎁 {self.user.name}'s Custom Mane Box:")

        # Categorize selected products
        shampoos = [p for p in self.selected_products if "shampoo" in p.category]
        conditioners = [p for p in self.selected_products if "conditioner" in p.category]
        others = [
            p for p in self.selected_products
            if p.category.lower() not in ["shampoo", "conditioner"]
        ]

        def print_section(title, products):
            """
            Prints a section of products with a category header and matching concerns.

            Args:
                title (str): Section title to display (e.g., Shampoos).
                products (list): List of Product objects for that category.
            """
            print(f"\n{title} (within your budget)")
            if not products:
                print("⚠️ No matching products found in this category.")
                return

            for p in products:
                concerns = identify_concerns(p.description)
                concern_text = f"       ➤ Targets: {', '.join(concerns)}" if concerns else "       ➤ Targets: General care"
                print(f"- {p.brand} – {p.name} (${p.price:.2f})")
                print(concern_text)

        # Display each category section
        print_section("🧴 Shampoos", shampoos)
        print_section("💧 Conditioners", conditioners)
        print_section("✨ Treatments & Styling", others)