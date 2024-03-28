#!/usr/bin/python3
"""
Use the urlib package to fetch a URL, display results on stdout
"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        pure = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(pure)))
        print("\t- content: {}".format(pure))
        print("\t- utf8 content: {}".format(pure.decode("utf-8")))
