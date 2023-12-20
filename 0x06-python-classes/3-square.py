#!/usr/bin/python3
"""Creating the class Square and filling it according to the tasks"""


class Square:
    """Definition of the Square class"""
    def __init__(self, size=0):
        """The init method for all instances of the class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the current square area"""
        return (self.__size ** 2)
