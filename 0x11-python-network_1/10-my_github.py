#!/usr/bin/python3
"""
Uses the GitHub API to display user ID.
Authentication is necessary
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    auth_key = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=auth_key)
    print(res.json().get("id"))
