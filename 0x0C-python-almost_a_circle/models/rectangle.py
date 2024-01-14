#!/usr/bin/python3

"""This module contains the class Rectangle, with parent class Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting the Base class attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation method for the Rectangle class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter function for the width private attribute
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter method for the width private attribute
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height private attribute
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter method for the height private attribute
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the private attribute x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Setter method for the private attribute x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the private attribute y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Setter method for the private attribute y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            (int) Area of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Prints a string representation of the rectangle to stdout
        """
        for b in range(self.__y):
            print()
        for i in range(self.__height):
            for t in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        A magic method that runs when str or print is called
        """
        return (
            f"[{type(self).__name__}] ({self.id}) "
            f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
        )

    def update(self, *args):
        """
        Updates the attributes of the instance based on the args given
        """
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
