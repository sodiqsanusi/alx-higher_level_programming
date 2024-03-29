#!/usr/bin/python3
"""
Use requests to make a GET, if error occurs handle it
"""
import requests
import sys


def main():
    """
    This is the main function of the program
    """
    url = sys.argv[1]
    res = requests.get(url)
    if (res.status_code >= 400):
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)


if __name__ == "__main__":
    main()
