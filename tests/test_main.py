import unittest
from product import Product
from utils import match_concerns, match_exclusions

class TestRegexMatching(unittest.TestCase):
    def test_concern_match(self):
        desc = "hydrating shampoo for dry curly hair"
        self.assertTrue(match_concerns(desc, ["dry", "curly"]))

    def test_exclusion_match(self):
        desc = "hydrating vegan shampoo"
        self.assertTrue(match_exclusions(desc, ["vegan"]))
