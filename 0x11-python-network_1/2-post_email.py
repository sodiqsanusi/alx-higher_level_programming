#!/usr/bin/python3
"""
Take a URL and an email. sending the email as data to the URL using urllib POST
"""
import urllib.request
import urllib.parse
import sys


def main():
    """
    The main function in the program
    """
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        pure = response.read().decode("utf-8")
        print(pure)


if __name__ == "__main__":
    main()
