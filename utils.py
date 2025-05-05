import re

# Expanded concern keywords mapping
CONCERN_KEYWORDS = {
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

# Match if a product description covers any of the user's concerns
def match_concerns(description, concerns):
    if not description:
        return False

    description = description.lower()
    for concern in concerns:
        keywords = CONCERN_KEYWORDS.get(concern, [])
        for keyword in keywords:
            if keyword in description:
                return True
    return False

# Match if a product description contains excluded terms
def match_exclusions(description, exclusions):
    if not description:
        return False

    for exclude in exclusions:
        pattern = re.compile(re.escape(exclude), re.IGNORECASE)
        if pattern.search(description):
            return True
    return False

# Identify all concerns a description targets (used for display)
def identify_concerns(description):
    found = []
    if not description:
        return found

    description = description.lower()
    for concern, keywords in CONCERN_KEYWORDS.items():
        for keyword in keywords:
            if keyword in description:
                found.append(concern)
                break
    return found