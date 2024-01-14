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
