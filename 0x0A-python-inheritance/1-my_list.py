#!/usr/bin/python3
"""
File: 1-my_list.py
Description: a module that contains a superclass and its child class
Author: kaleab Shiferaw Girma(kalu-coder)
Date: 1st August
"""


class MyList(list):
    """
    a class that inherits from a list superclass
    """
    def print_sorted(self):
        """
        this method prints a sorted version of a list passed to it
        """
        sorted_list = sorted(self)
        print(sorted_list)
        del sorted_list
