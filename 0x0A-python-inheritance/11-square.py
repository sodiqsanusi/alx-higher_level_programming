#!/usr/bin/python3

"""This module works on extending function of class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """The class that acts as subclass to another subclass"""
    def __init__(self, size):
        """Instantiation method of the Rectangle class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def __str__(self):
        """Magic method that runs when print and str are called"""
        return ("[Square] {}/{}".format(self.__width, self.__height))
