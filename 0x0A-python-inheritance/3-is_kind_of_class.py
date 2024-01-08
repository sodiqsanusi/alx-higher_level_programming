#!/usr/bin/python3

"""This module contains a function that checks an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class or parent classes of a_class"""
    return (isinstance(obj, a_class))
