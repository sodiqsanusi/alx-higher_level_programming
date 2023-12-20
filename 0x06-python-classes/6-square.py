#!/usr/bin/python3
"""Module for creating the Square class alongside setter, getter methods"""


class Square:
    """This is the definition of the class"""
    def __init__(self, size=0, position=(0, 0)):
        """init method for all instances of the class"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter method for the private size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method for the size private attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter function to get the position of the object instance"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter method to change the private instance position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square using the # symbol as a marker"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
