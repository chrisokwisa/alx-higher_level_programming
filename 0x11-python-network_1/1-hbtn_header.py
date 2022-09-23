#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL displays the value of the X-Request-Id variable in header"""
import urllib.request
from sys import argv

if __name__ = "__main__":
    with urllib.request.urlopen(agrv[1]) as response:
        print(response.headers.get('X-Request-Id'))
