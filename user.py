class User:
    """
    Represents a user of The Mane Box with personalized hair preferences and needs.
    """
    
    def __init__(self, name, texture, hair_type, concerns, budget, exclusions):
        self.name = name
        self.texture = texture
        self.hair_type = hair_type
        self.concerns = [c.strip().lower() for c in concerns if c.strip()]
        self.exclusions = [e.strip().lower() for e in exclusions if e.strip()]
        self.budget = float(budget)