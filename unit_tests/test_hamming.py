import sys
import os
import unittest
from hamming_distance import hamming

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class TestHamming(unittest.TestCase):
    def test_exact_match(self):
        self.assertEqual(hamming("kitten", "kitten"), 0)

    def test_single_edit(self):
        self.assertEqual(hamming("kitten", "sitten"), 1)

    def test_different_lengths(self):
        self.assertEqual(hamming("glued", "booed"), 3)

    def test_empty_string(self):
        self.assertEqual(hamming("", ""), 0)

if __name__ == '__main__':
    unittest.main()
