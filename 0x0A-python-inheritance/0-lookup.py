#!/usr/bin/python3

"""
file: 0-lookup.py
Description: a module containing a method that returns every
attributes and methods of a function.
Author: Kaleab Shiferaw Girma
Date: August 1 2022
"""


def lookup(obj):
    """
    lookup - a method that returns attributes and methods of an object

    Args:
        obj: an object that is passed to the method
    Returns:
        list: a list of available attributes and methods the object has
    """
    return dir(obj)
