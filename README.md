# 💇‍♀️ The Mane Box

**The Mane Box** is a personalized hair care recommendation system built in Python. It builds a custom selection of shampoos, conditioners, and treatments based on the user's hair profile, concerns, budget, and preferences for clean beauty. The Mane Box is designed to simulate the experience of a personalized subscription box as it uses a keyword-matching algorithm to recommend relevant products from real-world datasets.

---

# 📦 Features

- 💁‍♀️ Custom recommendations based on:
  - Hair texture and type
  - Common concerns (dryness, frizz, dandruff, etc.)
  - Heat styling habits
  - Hair coloring
  - Preference for clean or vegan products
  - Product exclusions (sulfates, parabens, fragrances)
  - Budget sensitivity

- 🧴 Recommends your top:
  - Three shampoos  
  - Three conditioners  
  - Three masks/treatments/styling products

- 📊 Works with real-world data from curated CSVs pulled from the Sephora API
- 🧪 Tested using `pytest` to validate product recommendation logic

---
# 🚀 How to Run

1. **Install dependencies**  
   _None required beyond Python’s standard library._

2. **Run the app**:
   ```bash
   python main.py
   ```

---
# 🧠 Behind the Scenes
- Natural language processing (NLP) using regex and keyword detection to identify product benefits and exclusions.
- Data cleaning through Pandas organization to strip HTML tags from scraped data.
- Price tiers (budget, mid-range, premium) used for filtering without displaying actual prices.
- Randomized selection ensures variety in recommendations.

---
# 🔍 Future Improvements
- Add a web-based interface (React, Flask)
- Expand to seasonal boxes or long-term hair goals
- Save user history for tailored future suggestions