import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        with self.assertRaises(AssertionError):
            area(0)

    def test_area_positive(self):
        self.assertEqual(area(4), 16)

    def test_perimeter_zero(self):
        with self.assertRaises(AssertionError):
            perimeter(0)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(4), 16)
