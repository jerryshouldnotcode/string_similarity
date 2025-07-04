import sys
import os
import unittest
from levenshtein_distance import levenshtein

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class TestLevenshtein(unittest.TestCase):
    def test_exact_match(self):
        self.assertEqual(levenshtein("kitten", "kitten"), 0)

    def test_single_edit(self):
        self.assertEqual(levenshtein("kitten", "sitten"), 1)

    def test_different_lengths(self):
        self.assertEqual(levenshtein("kitten", "kitchen"), 2)

    def test_empty_string(self):
        self.assertEqual(levenshtein("", "abc"), 3)

if __name__ == '__main__':
    unittest.main()