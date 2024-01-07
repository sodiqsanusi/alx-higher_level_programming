#!/usr/bin/python3

"""This module contains a function that adds integers"""


def add_integer(a, b=98):
    """Add two integers, make type checks and a type conversion first"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
