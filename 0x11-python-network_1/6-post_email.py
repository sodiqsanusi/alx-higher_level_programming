#!/usr/bin/python3
"""
Use requests to make a POST to a provided url, passing to it an inputted email
"""
import requests
import sys


def main():
    """
    This is the main function of the program
    """
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    res = requests.post(url, data)
    print(res.text)


if __name__ == "__main__":
    main()
