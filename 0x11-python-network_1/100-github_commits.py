#!/usr/bin/python3
"""This script displays the last 10 commits from a GitHub repository."""
import requests
import sys


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    response = requests.get(url)
    top_commits = response.json()[:10]
    for commit in top_commits:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print(f"{sha}: {author}")
