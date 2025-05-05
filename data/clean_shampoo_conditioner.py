import pandas as pd
import re

# Load the dataset
df = pd.read_csv("data/unformatted/sephora_shampoo+conditioner.csv", encoding="utf-8")

# Function to clean HTML and unwanted text
def clean_text(raw_text):
    clean = re.sub(r'<[^>]+>', '', str(raw_text))  # Remove HTML tags
    clean = re.sub(r'\s+', ' ', clean).strip()     # Normalize whitespace
    clean = re.sub(
        r"in\s?\d+(\.\d+)?\s?(oz|ml|mL|g|oz\/ml)?(\s?\/\s?\d+\s?(mL|ml))?\s?(Image\s?\d+)?",
        "", clean, flags=re.IGNORECASE
    )
    clean = re.sub(r'Image\s*\d+', '', clean, flags=re.IGNORECASE)  # Stray Image mentions
    clean = re.sub(r'\s+', ' ', clean).strip()  # Final whitespace clean
    return clean

# Clean relevant fields
df["description"] = df["description"].apply(clean_text)
df["name"] = df["name"].apply(clean_text)

# Format price from cents to dollars
df["price"] = df["price"].apply(lambda x: round(float(x) / 100, 2) if pd.notnull(x) else x)

# Save cleaned file
df.to_csv("data/cleaned/cleaned_shampoo+conditioner.csv", index=False)
print("✅ Cleaned CSV saved")