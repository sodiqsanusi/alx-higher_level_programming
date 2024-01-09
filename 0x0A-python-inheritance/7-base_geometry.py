#!/usr/bin/python3

"""Contains a minimal class with two public methods"""


class BaseGeometry():
    """This class contains some functions that builds on mathematics"""
    def area(self):
        """Main function is to raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates a value, is the"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
