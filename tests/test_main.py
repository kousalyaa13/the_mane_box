import sys
import os
import pytest

# Add the parent directory (one level up from /tests) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from product import Product
from user import User
from main import recommend_products
from utils import identify_concerns

@pytest.fixture
def sample_products():
    return [
        Product(
            name="Hydrating Shampoo",
            category="shampoo",
            brand="BrandA",
            description="This shampoo deeply hydrates and nourishes dry hair.",
            price_tier="budget"
        ),
        Product(
            name="Color Safe Conditioner",
            category="conditioner",
            brand="BrandB",
            description="Great for color-treated hair with smoothing effect.",
            price_tier="mid-range"
        ),
        Product(
            name="Volume Boost Mask",
            category="mask",
            brand="BrandC",
            description="Adds volume and strengthens thin hair.",
            price_tier="premium"
        )
    ]

def test_recommend_products_with_concerns(sample_products):
    user = User(
        name="TestUser",
        texture="wavy",
        hair_type="medium",
        concerns=["dryness", "color-treated"],
        budget=50.0,
        exclusions=[]
    )
    results = recommend_products(user, sample_products, avoid_concerns=[])
    
    # Assert that we got results
    assert len(results) > 0

    # Assert that each recommended product matches at least one concern
    for product in results:
        matched = any(c in identify_concerns(product.description) for c in user.concerns)
        assert matched, f"{product.name} did not match any concerns"

def test_recommend_products_with_exclusions(sample_products):
    user = User(
        name="TestUser",
        texture="wavy",
        hair_type="medium",
        concerns=["dryness", "color-treated"],
        budget=50.0,
        exclusions=["color"]
    )
    results = recommend_products(user, sample_products, avoid_concerns=[])
    assert all("color" not in p.description.lower() for p in results)