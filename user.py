class User:
    def __init__(self, name, hair_texture, hair_type, concerns, budget, exclusions):
        """
        Initialize a User object with the following attributes:
        """
        self.name = name
        self.hair_texture = hair_texture
        self.hair_type = hair_type
        self.concerns = concerns
        self.budget = budget
        self.exclusions = exclusions
        self.history = []

    def update_preferences(self, hair_texture = None, hair_type = None, concerns = None, budget = None, exclusions = None):
        """
        Update the user's preferences.
        """
        if hair_texture:
            self.hair_texture = hair_texture
        if hair_type:
            self.hair_type = hair_type
        if concerns:
            self.concerns = concerns
        if budget:
            self.budget = budget
        if exclusions:
            self.exclusions = exclusions