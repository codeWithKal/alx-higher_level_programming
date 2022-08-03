#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
File: 8-rectangle.py
Desc: a module containing a class Rectangle that inherits.
Author: Kaleab Shiferaw Girma
Date: 3rd August 2022
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class inherited from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantializer method

        Args:
            width: width of a rectangle
            heigh: height of a rectangle
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
