#!/usr/bin/python3

""" Hello, This is a Rectangle class with private attributes. """


class Rectangle:
    """This is an empty class representing a rectangle"""
    def __init__(self, width=0, height=0):
        """This is an instance method that runs on object creation"""
        self.width = width
        self.height = height

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
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if (self.__height == 0) or (self.__width == 0):
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """Creating a string representation of the recatangle"""
        if (self.__width == 0) or (self.__height == 0):
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append("#") for j in range(self.__width)]
            if i != (self.__height - 1):
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """A string representation that can create a new instance with eval"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
