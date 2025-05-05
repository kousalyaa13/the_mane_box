import re

# Mapping of user concern categories to relevant keywords for text matching
concern_keywords = {
    "dryness": ["dry", "hydrating", "moisture", "moisturizing", "nourish", "nourishing", "quench", "parched"],
    "frizz": ["frizz", "smoothing", "smooth", "anti-frizz", "flyaways", "humidity", "tame", "control"],
    "dandruff": ["dandruff", "flaky", "flakes", "scalp", "itchy", "itch", "scalp care", "scalp health", "clarifying"],
    "split ends": ["split ends", "damage", "damaged", "repair", "restorative", "renew", "revive", "fortify"],
    "hair loss": ["hair loss", "thinning", "thin", "volume", "strengthen", "strength", "breakage", "regrowth", "falling hair"],
    "color-treated": ["color-safe", "color treated", "preserve color", "fade protection", "color protection", "highlight", "dyed"],
    "curly": ["curl", "curly", "coils", "define curls", "curl enhancing", "bounce", "twist", "kinky"],
    "straight": ["straight", "sleek", "smooth", "straighten", "flat", "polished"],
    "volume": ["volume", "volumizing", "lift", "bounce", "body", "fuller", "thickening"],
    "oily": ["oily", "oil control", "greasy", "oiliness", "balancing", "purifying", "refresh"],
    "heat damage": ["heat protection", "thermal", "blow dry", "heat damage", "hot tools", "iron", "protectant"]
}

def match_concerns(description, concerns):
    """
    Check if the product description matches any of the user's hair concerns.

    Args:
        description (str): The text description of the product.
        concerns (list of str): List of concern keywords from the user.

    Returns:
        bool: True if any concern keyword is found in the description, else False.
    """
    if not description:
        return False

    description = description.lower()
    # Check if any of the user's concerns are in the description
    for concern in concerns:
        keywords = concern_keywords.get(concern, [])
        for keyword in keywords:
            if keyword in description:
                return True
    return False

def match_exclusions(description, exclusions):
    """
    Check if the product description includes any excluded ingredients or terms.

    Args:
        description (str): The text description of the product.
        exclusions (list of str): List of ingredient or feature keywords to avoid.

    Returns:
        bool: True if any exclusion is found in the description, else False.
    """
    if not description:
        return False
    
    for exclude in exclusions:
        # Use regex to match whole words only
        # re.escape is used to escape any special characters in the exclusion term
        pattern = re.compile(re.escape(exclude), re.IGNORECASE)
        if pattern.search(description):
            return True
    return False

def identify_concerns(description):
    """
    Identify all hair concerns a product description targets for display purposes.

    Args:
        description (str): The text description of the product.

    Returns:
        list of str: Concerns identified based on keyword presence in the description.
    """
    found = []
    # Check if description is empty or None
    if not description:
        return found

    description = description.lower()
    # Check for each concern category
    for concern, keywords in concern_keywords.items():
        for keyword in keywords:
            # Use regex to match whole words only
            if keyword in description:
                found.append(concern)
                break 
    return found