#!/usr/bin/python3
""" Creating a class with a provate attribute and an optional one"""


class Square:
    """The definition of the class itself"""
    def __init__(self, size=0):
        """The init method for each object gotten from the class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
