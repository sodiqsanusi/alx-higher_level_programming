#!/usr/bin/python3

"""Contains a function that checks if an object is explicitly a subclass"""


def inherits_from(obj, a_class):
    """Checks if object is an explicit subclass of a_class, not instance"""
    if (type(obj) is a_class):
        return (False)
    return (isinstance(obj, a_class))
