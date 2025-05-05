import pandas as pd
import re

# Load your filtered CSV
df = pd.read_csv("data\dataset_sephora_shampoo+conditioner.csv")

# Clean HTML tags from 'description' using regex
def clean_html(text):
    if pd.isnull(text):
        return ""
    return re.sub(r"<.*?>", "", text)

df["description"] = df["description"].apply(clean_html)

# Renamed columns for clarity
df = df.rename(columns={
    "title": "name",
    "categories/1": "category",
    "brand": "brand"
})

# Reorder and keep only necessary columns
final_df = df[["name", "category", "brand", "description"]]

# Save to a cleaned CSV
final_df.to_csv("cleaned_mane_box_data.csv", index=False)

print("Descriptions cleaned and saved to cleaned_mane_box_data.csv")