import pandas as pd
import re

# Load the dataset
df = pd.read_csv("data\imported datasets\dataset_sephora_treatments.csv", encoding="utf-8")

# Function to remove HTML and unwanted trailing phrases from text
def clean_text(raw_text):
    clean = re.sub(r'<[^>]+>', '', str(raw_text))  # remove HTML tags
    clean = re.sub(r'\s+', ' ', clean).strip()     # remove extra spaces

    # Remove patterns like:
    # "in 8 oz", "in 8 oz / 240 ml", "in 6 oz Image 2", "Image 2" at the end
    clean = re.sub(
        r"in\s?\d+(\.\d+)?\s?(oz|ml|mL|g|oz\/ml)?(\s?\/\s?\d+\s?(mL|ml))?\s?(Image\s?\d+)?",
        "", clean, flags=re.IGNORECASE
    )
    clean = re.sub(r'Image\s*\d+', '', clean, flags=re.IGNORECASE)  # catch stray "Image 2"
    clean = re.sub(r'\s+', ' ', clean).strip()  # tidy up extra spaces again
    return clean

# Clean the 'description' and optionally the 'name' fields
df["description"] = df["description"].apply(clean_text)
df["name"] = df["name"].apply(clean_text)

# Define brand tiers
premium_brands = ["Oribe", "Kérastase", "OUAI", "Gisou", "K18 Biomimetic Hairscience"]
midrange_brands = ["amika", "Briogeo", "Function of Beauty PRO", "Drybar"]
affordable_brands = ["Verb", "The Ordinary"]

# Assign price tiers based on brand
def assign_price_tier(brand):
    if brand in premium_brands:
        return "premium"
    elif brand in midrange_brands:
        return "mid-range"
    elif brand in affordable_brands:
        return "affordable"
    else:
        return "mid-range"

df["price_tier"] = df["brand"].apply(assign_price_tier)

# Save cleaned CSV
df.to_csv("data/cleaned_treatments_data.csv", index=False)
print("Cleaned CSV saved as 'cleaned_treatments_data.csv'")