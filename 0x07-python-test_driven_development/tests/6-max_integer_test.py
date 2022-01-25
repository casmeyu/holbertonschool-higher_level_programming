#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        #Valid test
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([-1, -2, -3]), -1)
        self.assertAlmostEqual(max_integer([0, 0, 0]), 0)
        self.assertAlmostEqual(max_integer([-1, 0, 3]), 3)

    def test_max_float(self):
        self.assertAlmostEqual(max_integer([0.0, 1.1, 2.2]), 2.2)
        self.assertAlmostEqual(max_integer([-3.4, -1.1, 2]), 2)

    def test_max_string(self):
        #invalid types
        self.assertRaises(TypeError, max_integer, [1, '2'])

    def text_max_int(self):
        #invalid types
        self.assertRaises(TypeError, max_integer, 1)
