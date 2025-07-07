import sys
import os
import unittest
from ratcliff_obershelp import ratcliff_obershelp

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class TestRatcliffObershelp(unittest.TestCase):
    def test_exact_match(self):
        self.assertEqual(ratcliff_obershelp("hello", "hello"), 1.0)

    def test_partial_match(self):
        score = ratcliff_obershelp("hello", "hallo")
        self.assertTrue(0.5 < score < 1.0)

    def test_no_match(self):
        self.assertEqual(ratcliff_obershelp("abc", "xyz"), 0.0)

    def test_case_sensitivity(self):
        score = ratcliff_obershelp("Hello", "hello")
        self.assertTrue(0 < score < 1.0)

    def test_empty_string(self):
        self.assertEqual(ratcliff_obershelp("", ""), 1.0)
        self.assertEqual(ratcliff_obershelp("abc", ""), 0.0)

if __name__ == '__main__':
    unittest.main()
