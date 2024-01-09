#!/usr/bin/python3

"""This module involves command line arguments, serialization and file I/O"""
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    lilac = []
    if os.path.exists("add_item.json"):
        lilac = load_from_json_file("add_item.json")
    argList = sys.argv[1:]
    lilac.extend(argList)
    save_to_json_file(lilac, "add_item.json")
