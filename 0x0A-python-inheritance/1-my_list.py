#!/usr/bin/python3

"""This module contains code that builds ona default Python Class"""


class MyList(list):
    """A custom subclass of list with added functionalities"""
    def print_sorted(self):
        """Prints the list in a sorted order, without changing it"""
        print(sorted(self))
