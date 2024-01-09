#!/usr/bin/python3

"""This module works with deserialization of a JSON string"""
import json


def from_json_string(my_str):
    """
    Convert a JSON string to its representative object (Deserialization)

    Args:
        my_str (string): JSON string to be deserialized

    Return:
        (object) The object representation of the JSON string
    """
    lilac = json.loads(my_str)
    return (lilac)
