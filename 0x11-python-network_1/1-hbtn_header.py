#!/usr/bin/python3
"""
Take in a URL from the terminal, fetch it, and display a value of
one of its header variables
"""
import urllib.request
import sys


def main():
    """
    This is the major function to run
    """
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        final = headers.get("X-Request-Id")
        print(final)


if __name__ == "__main__":
    main()
