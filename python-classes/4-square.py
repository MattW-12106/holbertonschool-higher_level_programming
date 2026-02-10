#!/usr/bin/python3
"""Defines a square."""
class Square:
    """Creates a square with a given size."""

    def __init__(self, size=0):
        """Initializes a square with the given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size
    
    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value