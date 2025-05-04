class SubscriptionBox:
    def __init__(self, user):
        self.user = user
        self.selected_products = []

    def add_product(self, product):
        self.selected_products.append(product)

    def total_price(self):
        return sum(p.price for p in self.selected_products)

    def display_box(self):
        print(f"\n{self.user.name}'s Mane Box:")
        for product in self.selected_products:
            print(f"- {product.name} ({product.category}) by {product.brand} - ${product.price}")
        print(f"Total: ${self.total_price():.2f}")