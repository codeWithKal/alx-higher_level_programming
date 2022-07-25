#!/usr/bin/python3
"""
File: 1-rectangle.py
Desc: a module containing a class for defining a rectangle with
    width and height.
Author: Kaleab Shiferaw Girma
Date: July 25 2022
"""


class Rectangle():
    """
    a class containg getter and setter methods for height and width attribute
    of the class
    """
    def __init__(self, width=0, height=0):
        """
        initializer method
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        getter method for height attribute
        """
        return(self.__height)

    @height.setter
    def height(self, value):
        """
        a setter method for height attribute a class
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """
        a getter method for width attribute
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """
        a setter method for width attribute of a rectangle class
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")
