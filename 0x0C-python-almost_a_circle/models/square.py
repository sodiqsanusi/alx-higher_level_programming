#!/usr/bin/python3

"""This module contains the subclass Square inheriting from Rectangle"""
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """The class Square, inheriting from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        The instantiation method for the Square class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        A magic method that runs when str or print is called
        """
        return (
            f"[{type(self).__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}"
        )

    @property
    def size(self):
        """
        Getter method for the size of the Square instance
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        Setter method for the size of the Square instance
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
