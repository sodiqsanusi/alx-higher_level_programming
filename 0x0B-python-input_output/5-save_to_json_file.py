#!/usr/bin/python3

"""This module deals with desrialization and file I/O"""
import json


def save_to_json_file(my_obj, filename):
    """
    Serializes an object, then saves the gotten JSON data into a text file

    Args:
        my_obj (object): Object to be serialized
        filename (str): Name of file to save JSON into
    """
    lilac = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as createdFile:
        createdFile.write(lilac)
