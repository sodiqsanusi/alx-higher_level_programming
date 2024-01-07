#!/usr/bin/python3

"""This module contains a function that prints a square"""


def print_square(size):
    """Prints a square of size inputed using the # character"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    print("\n".join([
            "".join(["#" for x in range(size)])
            for y in range(size)]))
