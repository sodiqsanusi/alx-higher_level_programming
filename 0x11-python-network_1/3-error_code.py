#!/usr/bin/python3
"""
Take in a URL from the terminal, fetch it, and display the response
Manage HTTP errors that may come up
"""
import urllib.request
import urllib.error
import sys


def main():
    """
    This is the major function to run
    """
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            final = response.read().decode("utf-8")
            print(final)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
