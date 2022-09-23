#!/usr/bin/python3
"""sends a request to the URL and displays
the body of the respons (decoded in utf-8)
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {:}".format(e.code))
