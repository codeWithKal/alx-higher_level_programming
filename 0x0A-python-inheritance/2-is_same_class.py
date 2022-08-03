#!/usr/bin/python3
"""
File: 2-is_same_class.py
Description: a module containing a method checkes wheather
        a class is an instance of a_class or not
Author: Kaleab Shiferaw Girma
Date: August 3 2022
"""


def is_same_class(obj, a_class):
    """
    checkes if a given object is an instance of a class

    Args:
        obj(any): an object to be checked
        a_class(any): a class to be checked against
    """

    if isinstance(obj, a_class):
        return True
    return False
