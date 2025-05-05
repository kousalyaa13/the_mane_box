class SubscriptionBox:
    def __init__(self, user):
        self.user = user
        self.selected_products = []

    def add_product(self, product):
        self.selected_products.append(product)

    def display_box(self):
        print(f"\n{self.user.name}'s Mane Box:")
        for product in self.selected_products:
            print(f"- {product.name} ({product.category}) by {product.brand}")
        print("\nEnjoy your personalized hair care products!")