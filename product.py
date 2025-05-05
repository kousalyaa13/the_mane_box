class Product:
    def __init__(self, name, category, brand, description, price):
        self.name = name
        self.category = category
        self.brand = brand
        self.description = description
        self.price = float(price)

    def __str__(self):
        return f"{self.name} ({self.category}) by {self.brand} — ${self.price:.2f}\\n  ➤ {self.description}"