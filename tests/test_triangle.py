import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        with self.assertRaises(AssertionError):
            area(0, 5)

    def test_area_positive(self):
        self.assertEqual(area(3, 4), 6)

    def test_perimeter_zero(self):
        with self.assertRaises(AssertionError):
            perimeter(0, 0, 0)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
