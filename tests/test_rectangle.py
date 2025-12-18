import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        with self.assertRaises(AssertionError):
            area(0, 5)

    def test_area_positive(self):
        self.assertEqual(area(3, 4), 12)

    def test_perimeter_zero(self):
        with self.assertRaises(AssertionError):
            perimeter(0, 0)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 4), 14)
