#!/usr/bin/python3

"""Test cases for the Base class module"""
import unittest
from models.base import Base
import json


class TestBaseModules(unittest.TestCase):
    """
    Test cases for the Base class
    """
    def test_create_new_base(self):
        """
        Creates a new base without a defualt id
        """
        b = Base()
        self.assertEqual(b.id, 1)
        c = Base()
        self.assertEqual(c.id, 2)

    def test_create_new_base_withid(self):
        """
        Creates a new base with a specified ID
        """
        b = Base(12)
        self.assertEqual(b.id, 12)
        c = Base(1)
        self.assertEqual(c.id, 1)
        d = Base(-22)
        self.assertEqual(d.id, -22)
