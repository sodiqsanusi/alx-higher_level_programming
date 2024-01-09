#!/usr/bin/python3

"""This module works on a text file"""


def append_write(filename="", text=""):
    """
    Appends new text to an existing file, creates new file with text otherwise

    Args:
        filename (str): File to append to (or create)
        text (str): Text content to append to file
    """
    with open(filename, "a", encoding="utf-8") as openedFile:
        lilac = openedFile.write(text)
        return (lilac)
