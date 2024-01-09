#!/usr/bin/python3

"""This module works on JSON manipulation"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object

    Args:
        my_obj (object): An object to be serialized, can be any data type

    Return:
        (string) A JSON string representation of the object
    """
    lilac = json.dumps(my_obj)
    return (lilac)
