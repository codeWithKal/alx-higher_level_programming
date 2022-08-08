#!/usr/bin/python3
"""
File: rectangle.py
Desc: a module that inherits from Base class and defines a rectangle.
Author: Kaleab Shiferaw Girma
Date: August 08 2022
"""
from .base import Base


class Rectangle(Base):
    """
    A class that inherits from Base Class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        an intializer class for rectangle class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        a getter method for width attribute
        """
        return self.__width

    @property
    def height(self):
        """
        a getter method for height property
        """
        return self.__height

    @property
    def x(self):
        """
        a getter method for the horizontal value of a rectangle
        """
        return self.__x

    @property
    def y(self):
        """
        A method that returns the vertical value of a rectangle
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        a setter method for width attribute

        Args:
            value(int): a new value to be assigned to width
        """
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        a setter method for height attribute of a rectangle

        Args:
            value(int): a new value to be assigned to height attribute
        """
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("Height must be > 0")
        else:
            raise TypeError("Height must be an integer")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        a setter method for x value of a rectangle.

        Args:
            value: a new value of a x
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @y.setter
    def y(self, value):
        """
        a setter method for y value of a rectangle.

        Args:
            value: a new value to be assigned to variable y

        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """
        A method that computes and returns an area of a rectangl.

        Returns(int): area of a rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        a method that prints a rectangle with a character of '#'.
        """
        h_off = ' ' * self.x
        h_val = '#' * self.width
        print('\n' * self.y, end='')
        print('{:s}{:s}\n'.format(h_off, h_val) * self.height, end='')

    def __str__(self):
        """
        an overridded __str__ method

        Returns: a string frommated expression of
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        args = (self.id, self.x, self.y, self.width, self.height)
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(*args)

    def update(self, *args, **kwargs):
        """Updates the attributes of this polygon.
        Args:
            args (tuple): A tuple of non-keyword arguments.
            kwargs (dict): A dictionary of keyword arguments.
        """
        attrs = ('id', 'width', 'height', 'x', 'y')
        for key, val in zip(attrs, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Creates a dictionary representation of this polygon.
        Returns:
            dict: A dictionary representation of this polygon.
        """
        res = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return res
