#!/usr/bin/python3
"""
File: 2-square.py
Description: defines a square
Author: kaleab shiferaw girma
Date: July 20 2022
"""


class Square():
    """
    This class contains a definition of single
    private object called size, which is non negeive integer.
    """

    def __init__(self, size):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
