#!/usr/bin/python3
"""
File: base.py
Desc: a base for all other classes in this project.
Author: Kaleab Shiferaw Girma
Date: 08 August 2022
"""


class Base():
    """
    The base class for other polygons
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializer method for the the Base method

        Args:
            id(int): integer id by assumption
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
