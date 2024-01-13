#!/usr/python/bin

"""A module containing a base class to be used in other modules"""
import json


class Base:
    """
    Acts as a base class with other classes building on it

    Attributes:
        __nb_objects (int): Class attribute acting as an id count
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization method for the Base class

        Args:
            id (obj): An identification number for the class instance
                Defaults to None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries into its JSON string representation

        Args:
            list_dictionaries (list): The list to be converted to JSON string

        Returns:
            str: A JSON string representation of the given list parameter
        """

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string represention of an object to a file

        Args:
            list_objs (obj): List whose JSON representation will be saved
        """

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to its object representation

        Args:
            json_string (str): The JSON string to be converted

        Returns:
            (obj): The correspoding object rep of the JSON string provided
        """

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of class with attributes from arguments provided

        Args:
            **dictionary: Keyword arguments, used to create new instance
        """
