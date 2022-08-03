#!/usr/bin/python3
"""
File: 10-square.py
Desc: a module containing a class that inherits from Rectangle class
Author: Kaleab Shiferaw Girma
Date 3rd August 2022
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a square class that inherits from a Rectangle superclass.
    """
    def __init__(self, size):
        """
        initializer method for class square

        Args:
            size(int): size of a square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        a method that computes area of a square.

        Returns:
            int: the area of a square.
        """
        return self.__size ** 2
