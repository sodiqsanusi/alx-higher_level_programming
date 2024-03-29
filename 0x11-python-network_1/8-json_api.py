#!/usr/bin/python3
"""
Take in a latter, and send as a POST request. display gotten result as JSON
"""
import requests
import sys


def main():
    """
    This is the main function for the program
    """
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {"q": letter}
    res = requests.post(url, data)
    try:
        res.raise_for_status()
        json_res = res.json()
        if len(json_res) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json_res['id'], json_res['name']))
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
