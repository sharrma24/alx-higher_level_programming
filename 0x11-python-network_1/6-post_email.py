#!/usr/bin/python3
"""Dispatches a POST request to a specified URL with a provided email.

Usage: ./6-post_email.py <URL> <email>
  - Presents the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)

