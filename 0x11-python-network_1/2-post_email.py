#!/usr/bin/python3
"""
File: 2-post_email.py
Desc: a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8)
Author: Kaleab Shiferaw Girma
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        data = byte(parse.urlencode([('email', email)]), 'utf-8')
        with request.urlopen(url, data=data) as response:
            print(response.read().decode('utf-8'))

