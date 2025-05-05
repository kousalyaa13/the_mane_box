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

        if shampoos:
            print("\n🧴 Shampoos:")
            for product in shampoos:
                print(f"- {product.name} ({product.brand})")

        if conditioners:
            print("\n💧 Conditioners:")
            for product in conditioners:
                print(f"- {product.name} ({product.brand})")

        if others:
            print("\n✨ Other Products:")
            for product in others:
                print(f"- {product.name} ({product.brand})")

        print("\n🧼 Enjoy your hair care picks!")
        print("💖 Thank you for using The Mane Box!")