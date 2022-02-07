#!/usr/bin/python3
"""Module for Rectangle testing"""
import unittest
from models.rectangle import Rectangle


class RectangleTests(unittest.TestCase):
    """Class for Rectangle testing"""
    def test_initialization(self):
        """Initialization test
            Arguments:
                width (int)
                height (int)
                x (int)
                y (int)
        """
        # No x or y value
        r = Rectangle(4, 2)
        res_list = [2, 4, 0, 0, 1]
        rec_list = [r.height, r.width, r.x, r.y, r.id]
        self.assertAlmostEqual(rec_list, res_list)

        r2 = Rectangle(2, 2, 2, 2)
        res_list = [2, 2, 2, 2, 2]
        rec_list = [r2.height, r2.width, r2.x, r2.y, r2.id]
        self.assertAlmostEqual(rec_list, res_list)

    def test_initialization_values(self):
        """Initialization with wrong values
            Arguments:
                width (int)
                height (int)
                x (int)
                y (int)
        """
        # Invalid width
        pass
