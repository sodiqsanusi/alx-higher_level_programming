#!/usr/bin/python3

"""This module contains a function that prints names based on input"""


def say_my_name(first_name, last_name):
    """The function prints a name based on the parameter inputs"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
