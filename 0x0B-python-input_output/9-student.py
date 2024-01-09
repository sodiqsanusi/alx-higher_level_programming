#!/usr/bin/python3

"""This module contains a class definition"""


class Student:
    """Defines a Student object blueprint"""
    def __init__(self, first_name, last_name, age):
        """Instatiation method for the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dict representatino of the class instance"""
        return (self.__dict__)
