#!/usr/bin/python3

"""This module contains a class definition"""


class Student:
    """Defines a Student object blueprint"""
    def __init__(self, first_name, last_name, age):
        """Instatiation method for the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dict representatino of the class instance"""
        if type(attrs) is not list:
            return (self.__dict__)
        lilac = {}
        for attr in attrs:
            if attr in self.__dict__.keys():
                lilac[attr] = self.__dict__[attr]
        return (lilac)

    def reload_from_json(self, json):
        """Replaces all attribute values of an instance"""
        for (key, value) in json.items():
            setattr(self, key, value)
