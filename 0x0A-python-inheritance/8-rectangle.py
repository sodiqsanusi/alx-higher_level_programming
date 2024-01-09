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
