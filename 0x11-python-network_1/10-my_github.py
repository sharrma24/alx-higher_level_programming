#!/usr/bin/python3
"""Utilizes the GitHub API to exhibit a GitHub ID using provided credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Applies Basic Authentication to retrieve the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))

