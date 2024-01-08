#!/usr/bin/python3

"""This module contains a function that gets all the attributes of an object"""


def lookup(obj):
    """Returns a list of available attributes of an object"""
    return (dir(obj))
