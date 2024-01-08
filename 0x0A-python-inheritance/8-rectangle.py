#!/usr/bin/python3

"""Contains a minimal class with two public methods"""


class BaseGeometry():
    """This class contains some functions that builds on mathematics"""
    def area(self):
        """Main function is to raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates a value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Builds on the baseclass to extend functionalities"""
    def __init__(self, width, height):
        """The instantiation method for the class"""
        super().integer_validation("width", width)
        super().integer_validation("height", height)
        self.__width = width
        self.__height = height
