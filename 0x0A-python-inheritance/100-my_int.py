#!/usr/bin/python3

"""This module builds on the int standard class"""


class MyInt(int):
    """This is a custom modification of the int class"""
    def __eq__(self, __value):
        """Dunder method for the == operator"""
        return (super().__ne__(__value))

    def __ne__(self, __value):
        """Dunder method for the != operator"""
        return (super().__eq__(__value))
