#!/usr/bin/python3
"""
file: 4-hbtn_status.py
Description: A script that uses requests module to fetch a website
Author: Kaleab Shiferaw Girma
"""
import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
