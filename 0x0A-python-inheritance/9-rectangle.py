#!/usr/bin/python3


"""A module with a class that models geometric shapes."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of the base geometry shape"""

    def __init__(self, width, height):
        """The instanstiation method of the subclass"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """An overridden function that calculates area"""
        return (self.__width * self.__height)

    def __str__(self):
        """A magic method that runs when str or print is called"""
        return (f"[{type(self).__name__}] {self.__width}/{self.__height}")
