#!/usr/bin/python3

"""Writes a string to a text file, returns number of characters written"""


def write_file(filename="", text=""):
    """
    Writes to a file, overwrite existing content or creates new file

    Args:
        filename (str): Name of file to create/overwrite
        text (str): Text content to put into the newly created file

    Return:
        (int) The number of characters written into the file
    """
    with open(filename, "w", encoding="utf-8") as createdFile:
        lilac = createdFile.write(text)
        return (lilac)
