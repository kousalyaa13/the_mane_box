import pandas as pd
import re

# Load the dataset
df = pd.read_csv("data\dataset_sephora_treatments.csv", encoding="utf-8")

# Function to remove HTML tags
def clean_html(raw_html):
    clean_text = re.sub(r'<[^>]+>', '', str(raw_html))  # remove HTML tags
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # remove extra spaces
    return clean_text

# Clean the description column
df["description"] = df["description"].apply(clean_html)

# Define brand tiers
premium_brands = ["Oribe", "Kérastase", "OUAI", "Gisou", "K18 Biomimetic Hairscience"]
midrange_brands = ["amika", "Briogeo", "Function of Beauty PRO", "Drybar"]
affordable_brands = ["Verb", "The Ordinary"]

def assign_price_tier(brand):
    if brand in premium_brands:
        return "premium"
    elif brand in midrange_brands:
        return "mid-range"
    elif brand in affordable_brands:
        return "affordable"
    else:
        return "mid-range"

# Apply price tier classification
df["price_tier"] = df["brand"].apply(assign_price_tier)

# Save cleaned file
df.to_csv("cleaned_treatments_data.csv", index=False)
print("✅ Cleaned CSV saved as 'cleaned_treatments_data.csv'")
