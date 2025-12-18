import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        with self.assertRaises(AssertionError):
            area(0)

    def test_area_positive(self):
        self.assertEqual(area(5), math.pi * 25)

    def test_perimeter_zero(self):
        with self.assertRaises(AssertionError):
            perimeter(0)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(5), 2 * math.pi * 5)
