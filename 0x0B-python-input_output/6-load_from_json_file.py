#!/usr/bin/python3

"""This module deals with file I/O and deserialization of JSON data"""
import json


def load_from_json_file(filename):
    """
    Deserialize data gotten from JSON file

    Args:
        filename (str): Name of JSON filepath

    Return:
        (object) Deserialized data gotten from JSON file
    """
    with open(filename, "r", encoding="utf-8") as openedFile:
        readData = openedFile.read()
        lilac = json.loads(readData)
        return (lilac)
