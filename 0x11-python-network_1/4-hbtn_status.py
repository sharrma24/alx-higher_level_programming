#!/usr/bin/python3
"""Retrieves https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Response body:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))

