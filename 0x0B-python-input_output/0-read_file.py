#!/usr/bin/python3

"""This module reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Opens a text file encoded in utf-8, prints to stdout"""
    with open(filename, "r", encoding="utf-8") as openedFile:
        lilac = openedFile.read()
        print(lilac, end="")
