#!/usr/bin/python3
"""
File: 4-inherits_from.py
Description: a module containing a function that returns
    True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified
    class ; otherwise False.
Author: Kaleab Shiferaw Girma
Date: 3rd August 2022
"""


def inherits_from(obj, a_class):
    """
    Description - a function that returns
        True if the object is an instance of a class that
        inherited (directly or indirectly) from the specified

    Args:
        obj(any): an object to be tested
        a_class(any): a class for which an object is tested against

    Returns:
        bool: True if 'obj' is an inheritance of 'a_class'
    """
    return issubclass(obj.__class__, a_class) and (type(obj) is not a_class)
