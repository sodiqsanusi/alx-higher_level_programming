#!/usr/bin/python3

"""Writes a string to a text file, returns number of characters written"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as createdFile:
        lilac = createdFile.write(text)
        return (lilac)
