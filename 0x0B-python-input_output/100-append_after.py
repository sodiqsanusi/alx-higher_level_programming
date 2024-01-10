#!/usr/bin/python3

"""This module contains some file manipulation"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a
    specific string

    Args:
        filename (str): Filename of text file to read an append to
        search_string (str): String to be used as search substring
        new_string (str): The string to be appended after the search_string
    """
    with open(filename, "r", encoding="utf-8") as openedFile:
        textData = openedFile.readlines()
    lilac = []
    for line in textData:
        lilac.append(line)
        if (line.find(search_string) >= 0):
            lilac.append(new_string)

    with open(filename, "w", encoding="utf-8") as newFile:
        newFile.writelines(lilac)
