#!/usr/bin/python3

"""This module contains some OOP shit"""


def class_to_json(obj):
    """
    Returns the dict description of an object

    Args:
        obj (object): The object to return its description

    Return:
        (dict) The description of the object
    """
    return (obj.__dict__)
