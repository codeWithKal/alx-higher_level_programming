#!/usr/bin/python3
"""
File: 5-square.py
Description: addition to 4-square.py and prints the square
Author: kaleab shiferaw girma
Date: july 22 2022
"""


class Square():
    """
    this class contains constructor, getter methods and setters
    in addition to square painter
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        getter method
        """
        return(self.__size)

    @self.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >=0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        A method that returns the current square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        prints the square:
        """
        if self.__size == 0:
            print("")

        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end=" ")
                print("")
