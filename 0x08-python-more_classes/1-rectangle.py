#!/usr/bin/python3

""" Hello, This is a Rectangle class with private attributes. """


class Rectangle:
    """This is an empty class representing a rectangle"""
    def __init__(self, width=0, height=0):
        """This is an instance method that runs on object creation"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter Method for the private instance attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter method for private instance value width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Setter Method for the private instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter method for the private instance height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
