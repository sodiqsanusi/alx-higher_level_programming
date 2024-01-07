#!/usr/bin/python3

"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """This is a test class building on a unittest field"""
    def test_getmaxint(self):
        """This tests the function for normal input"""
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([9, 0, -1, 4]), 9)
        self.assertAlmostEqual(max_integer([2, 2, 0, 1]), 2)
