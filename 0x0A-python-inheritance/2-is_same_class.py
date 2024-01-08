#!/usr/bin/python3

"""This module contains a function that checks if an object is a subclass"""


def is_same_class(obj, a_class):
    """Checks if a specified object is a subcclass of a specified class"""
    return (type(obj) is a_class)
