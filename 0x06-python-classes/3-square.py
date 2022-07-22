#!/usr/bin/python3

"""
file: 3-square.py
Description: this script defines a square and raises execptions
of TypeError and ValueError.
Author: Kaleab shiferaw girma
Date: july 22 2022
"""


class Square():
    """
    this class defines a square based on the size attribute passed
    to its constructors.
    It also had a method called area that squares its size.
    """

    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            rase TypeError("size must be an integer")

    def area(self):
        """
        this method square the value passed as size to the object"
        """

        return(self.__size ** 2)
