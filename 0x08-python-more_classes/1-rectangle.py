#!/usr/bin/python3
# 1-rectangle.py
# saadsgh123 <sdsghouri@gmail.com
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a Rectangle"""

    def __init__(self, width=0, height=0):
        """ initialise a rectangle

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Get/Set  the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get/Set the height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
