class Product:
    """
    Represents a haircare product with relevant details for recommendation.
    """
    def __init__(self, name, category, brand, description, price=0.0, price_tier="mid-range"):
        self.name = name
        self.category = category
        self.brand = brand
        self.description = description
        self.price = float(price)
        self.price_tier = price_tier