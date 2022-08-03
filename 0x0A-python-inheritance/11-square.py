#!/usr/bin/python3
"""
File: 11-square.py
Desc: a module that contains an area implemetation and str method.
Author: Kaleab Shiferaw Girma
Date: 3rd August 2022
"""
# importing a class from another module
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a square is a rectangle. thats why it square class inherited rectangle.
    """
    def __init__(self, size):
        """
        initializer method

        Args:
            size: size of a square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns:
            int: the area of a square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns:
            str: a square description: [Square] <width>/<height>
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
