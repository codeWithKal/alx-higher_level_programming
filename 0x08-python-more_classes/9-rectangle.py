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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializer method
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        computes an area of a rectangle
        """
        return(self.__width * self.__height)

    def perimeter(self):
        """
        computes the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return(0)
        return(2 * (self.__width + self.__height))

    def __str__(self):
        """
        a str method for printing a rectangle with #
        """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        else:
            s = str(self.print_symbol)
            w = self.width
            h = self.height
            res = map(lambda x: (s * w) + ('\n' * (x != h - 1)), range(h))
            return ''.join(list(res))

    def __repr__(self):
        """
        a method for representing an instance in string
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
        destructor of object method
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns the biggest rectangle based on the area.
        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        Returns:
            Rectangle: The biggest rectangle based on the area.
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        A method that initialize a new rectangle object with size

        Args:
            size: to be assigned to height and width
        Returns:
            the new rectangle
        """
        return(Rectangle(size, size))
