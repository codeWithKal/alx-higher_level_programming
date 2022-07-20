#!/usr/bin/python3
"""
File: 2-square.py
Description: defines a square
Author: kaleab shiferaw girma
Date: July 20 2022
"""


def __init__(self, size=0):
    """
    This class contains a definition of single
    private object called size, which is non negeive integer.
    """

    def __init__(self, size):
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raize TypeError("size must be an integer")
        self.__size = size
