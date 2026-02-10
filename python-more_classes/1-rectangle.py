#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """A class representing a rectangle."""
    def __init__(self, width=0, height=0):
        """ Initialize a Rectangle instance.
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
    @property
    def width(self):        
        """Get the width of the rectangle."""
        return self.__width
    @width.setter
    def height(self, value):
        """Set the height of the rectangle.
           value (int): The height value to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value