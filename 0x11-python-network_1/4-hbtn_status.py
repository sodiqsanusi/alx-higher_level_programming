#!/usr/bin/python3
"""
Fetch a defined URL using the requests Python package
"""
import requests


def main():
    """
    This is the main function for the program
    """
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url).text
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))


if __name__ == "__main__":
    main()
