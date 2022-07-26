#!/usr/bin/python3
"""
File: 0-add_integer.py
Description: a module to add integers
Author: kaleab shiferaw girma
date: july 26 2022
"""


def add_integer(a, b=98):
    """
    a method that adds two integers

    Args:
        a: the first integer
        b: the second integer
    Returns:
        the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
