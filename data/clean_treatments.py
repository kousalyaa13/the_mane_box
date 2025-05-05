import pandas as pd
import re

# Load the dataset
df = pd.read_csv("data/unformatted/sephora_treatments.csv", encoding="utf-8")

# Function to clean HTML and trailing clutter
def clean_text(raw_text):
    clean = re.sub(r'<[^>]+>', '', str(raw_text))  # Remove HTML tags
    clean = re.sub(r'\s+', ' ', clean).strip()     # Normalize whitespace

    # Remove patterns like: "in 8 oz", "in 8 oz / 240 ml", "Image 2", etc.
    clean = re.sub(
        r"in\s?\d+(\.\d+)?\s?(oz|ml|mL|g|oz\/ml)?(\s?\/\s?\d+\s?(mL|ml))?\s?(Image\s?\d+)?",
        "", clean, flags=re.IGNORECASE
    )
    clean = re.sub(r'Image\s*\d+', '', clean, flags=re.IGNORECASE)  # Remove stray "Image 2"
    clean = re.sub(r'\s+', ' ', clean).strip()  # Final cleanup
    return clean

# Apply text cleaning
df["description"] = df["description"].apply(clean_text)
df["title"] = df["title"].apply(clean_text)

# Format price from cents to dollars
df["price"] = df["price"].apply(lambda x: round(float(x) / 100, 2) if pd.notnull(x) else x)

# Save to cleaned CSV
df.to_csv("data/cleaned/cleaned_treatments.csv", index=False)
print("✅ Cleaned CSV saved")