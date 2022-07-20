#!/usr/bin/python3

"""
File: 1-square.py
description: a module to define a square with initialization of size
Author: Kaleab Shiferaw Girma
Date: July 20 2022
"""


class Square():
    """
    This class can be initialized to an square object with its own 'size'
    """
    def __init__(self, size):
        self.__size = size
