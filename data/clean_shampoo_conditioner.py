import pandas as pd
import re

# Load dataset using raw string or forward slashes to avoid escape errors
df = pd.read_csv(r"data\imported datasets\dataset_sephora_shampoo+conditioner.csv", encoding="utf-8")

# Show column names if unsure
print("Columns in CSV:", df.columns)

# Function to clean HTML and unwanted suffixes
def clean_text(text):
    if pd.isnull(text):
        return ""
    text = re.sub(r"<.*?>", "", str(text))  # remove HTML
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(
        r"in\s?\d+(\.\d+)?\s?(oz|ml|g)?(\s?\/\s?\d+\s?(ml|oz|g))?\s?(Image\s?\d+)?",
        "", text, flags=re.IGNORECASE
    )
    text = re.sub(r"Image\s*\d+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Adjust these to match your CSV
df["description"] = df["description"].apply(clean_text)
df["name"] = df["name"].apply(clean_text)  # only if 'name' is correct

# Rename columns if needed
df = df.rename(columns={
    "categories/1": "category",
    "brand": "brand"
})

# Keep only necessary columns (adjust if needed)
final_df = df[["name", "category", "brand", "description"]]

# Save to new CSV
final_df.to_csv("data/cleaned_mane_box_data.csv", index=False)
print("Cleaned CSV saved as 'data/cleaned_mane_box_data.csv'")