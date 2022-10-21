#!/usr/bin/python3
"""
File: 1-hbtn_header.py
Description: a script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id variable
found in the header of the response.
Author: Kaleab Shiferaw Girma
"""
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        exit
    else:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.headers["X-Request-Id"])
