#!/usr/bin/python3
"""
file: 7-base_geometry.py
Description: a module that validates a value
Author: Kaleab Shiferaw Girma
Date: 3rd August 2022
"""


class BaseGeometry():
    """
    a class containing method that validates a value in addition to the
    methods already defined in 6-base_geometry.
    """
    def area(self):
        """
        A methods that throws an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        a method that validates a value

        Args:
            name(string): first parameter
            value(int): integer parameter
        Returns:
            Nothing.
        """
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("{} must be greater that 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))
