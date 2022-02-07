#!/usr/bin/python3
"""Module for Base tests"""
import unittest
from models.base import Base

class BaseTests(unittest.TestCase):
    """Class for testing the Base Model"""
    def test_initialization(self):
        """Test for basic initialization of base class"""
        a = Base()
        self.assertAlmostEquals(a.id, 1)
        b = Base(4)
        self.assertAlmostEquals(b.id, 4)
        b.id = -4
        self.assertAlmostEquals(b.id, -4)
        c = Base()
        self.assertAlmostEquals(c.id, 3)
