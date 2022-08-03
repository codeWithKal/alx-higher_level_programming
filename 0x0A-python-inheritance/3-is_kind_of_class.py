#!/usr/bin/python3
"""
file: 3-is_kind_of_class.py
Description: a function that returns True if the object
    is an instance of, or if the object is an instance of
    a class that inherited from, the specified class ; otherwise False
Author: Kaleab Shiferaw Girma
Date: Aug 3 2022
"""


def is_kind_of_class(obj, a_class):
    """
    Description: checkes if obj is an instance of a class or the
        inherent class.
    Args:
        obj(any): an object to be passed to the method

        a_class(any): a class for which an object is tested if
            it is an instance or not.
    Returns:
        bool: True if obj is an instance of a_class; false otherwise.
    """
    return isinstance(obj, a_class)
