#!/usr/bin/python3
"""
File: 3-error_code.py
Description: a script that handles an HttpError
Author: Kaleab shiferaw Girma
"""
from urllib import request
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        try:
            with urllib.request.urlopen(url) as data:
                print(data.read().decode('utf-8'))
        except Exception as e:
            print("Error code: {}".format(e.code()))
