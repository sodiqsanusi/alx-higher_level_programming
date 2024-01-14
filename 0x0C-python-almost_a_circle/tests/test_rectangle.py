#!/usr/bin/python3

"""This module contains testcases for a Rectangle class"""
import unittest
from models.rectangle import Rectangle
import json


class TestRectangleInstances(unittest.TestCase):
    """
    Test cases for the rectangle class
    """
    def test_create_new_rectangle(self):
        """
        A testcase for creating a new rectangle
        """
        a = Rectangle(10, 15, 3, 3)
        self.assertEqual(a.id, 3)
        self.assertEqual(a.x, 3)
        b = Rectangle(5, 10, 2, 2, 30)
        self.assertEqual(b.id, 30)
