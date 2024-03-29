#!/usr/bin/python3
"""
Sends a request to the URL, displays the value of a header variable
"""
import requests
import sys


def main():
    """
    This is the main function for the program
    """
    url = sys.argv[1]
    res = requests.get(url)
    headers = res.headers
    print(headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
