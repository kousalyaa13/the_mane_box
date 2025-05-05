import pandas as pd

brand_price_map = {
    # Budget Tier
    "verb": (12, "budget"),
    "viori": (14, "budget"),
    "bondiboost": (14, "budget"),
    "pattern": (14, "budget"),
    "not your mother's": (12, "budget"),
    "shea": (13, "budget"),
    "l'oreal": (12, "budget"),
    "pantene": (9, "budget"),
    "garnier": (10, "budget"),
    "dove": (10, "budget"),
    "adwoa": (14, "budget"),
    "ceremonia": (14, "budget"),

    # Mid-Range Tier
    "amika": (26, "mid"),
    "briogeo": (28, "mid"),
    "ouai": (29, "mid"),
    "moroccanoil": (30, "mid"),
    "curlsmith": (30, "mid"),
    "living proof": (30, "mid"),
    "olaplex": (30, "mid"),
    "igk": (30, "mid"),
    "drybar": (28, "mid"),
    "fable & mane": (28, "mid"),
    "the ordinary": (22, "mid"),
    "the rootist": (22, "mid"),
    "function of beauty": (25, "mid"),

    # Premium Tier
    "kerastase": (42, "premium"),
    "oribe": (48, "premium"),
    "virtue": (40, "premium"),
    "rossano ferretti": (55, "premium"),
    "mizani": (38, "premium"),
    "color wow": (38, "premium"),
    "shu uemura": (45, "premium"),
    "act+acre": (36, "premium"),
    "necessaire": (36, "premium"),
    "dae": (35, "premium"),
    "crown affair": (38, "premium"),
    "roz": (38, "premium"),
    "the nue co.": (38, "premium"),
    "nutrafol": (42, "premium"),
    "guerlain": (50, "premium"),
    "ranavat": (50, "premium")
}

def estimate_price_and_tier(brand):
    brand_clean = brand.lower().strip()
    for key in brand_price_map:
        if key in brand_clean:
            return brand_price_map[key]
    return (25, "mid")  # Default fallback

# Load your cleaned CSV
df = pd.read_csv("data\cleaned_mane_box_data.csv")

# Apply price and tier estimation
df[["price", "price_tier"]] = df["brand"].apply(lambda b: pd.Series(estimate_price_and_tier(b)))

# Save new CSV
df.to_csv("cleaned_mane_box_data_with_price_tiers.csv", index=False)
print("✅ New file saved: cleaned_mane_box_data_with_price_tiers.csv")