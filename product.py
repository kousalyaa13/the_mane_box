class Product:
    def __init__(self, name, category, brand, description, price=0):
        self.name = name
        self.category = category
        self.brand = brand
        self.description = description
        self.price = float(price)