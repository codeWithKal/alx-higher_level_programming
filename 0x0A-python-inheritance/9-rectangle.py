#!/usr/bin/python3
"""
File: 9-rectangle
Desc: a module that implements area to calculate area
Author: kaleab Shiferaw Girma
Date: 3rd August 2022
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Represents a geometry object.
    '''
    def __init__(self, width, height):
        '''Initializes a new Rectangle geometry
        object with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        '''
        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        a method that computes an area of a rectangle

        Returns:
            int: the area of a rectangle.
        """
        return self.__width * self.__height

    def str(self):
        """
        string representation of a geometry

        Returns:
            str: a rectangle description [Rectangle] <width>/<height>
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
