#!/usr/bin/python3
"""
file: 7-base_geometry.py
Description: a module that validates a value
Author: Kaleab Shiferaw Girma
Date: 3rd August 2022
"""


class BaseGeometry:
    '''The base class for all geometry objects.
    '''
    def area(self):
        '''Computes the area of this geometry.

        Returns:
            float: The area of this geometry object.
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates an object expected to be a positive and
        non-zero integer object.

        Args:
            name (str): The name of the integer value.
            value (int): The object to validate.
        '''
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
