#!/usr/bin/python3
"""
File: 0-hbtn_status
Description: a script that fetches https://alx-intranet.hbtn.io/status
Author: Kaleab Shiferaw Girma
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        if response.readable():
            data = response.read()
            print ("Body response:")
            print ("\t - type: {}".format(type(data)))
            print ("\t -content: {}".format(data))
            print ("\t -utf8 content: {}".format(data.decode("utf=8")))
