#!/usr/bin/python3
class Square:
    """
    Create a square with default size:
    >>> s = Square()
    >>> isinstance(s, Square)
    True

    Create a square with a given size:
    >>> s = Square(5)
    >>> isinstance(s, Square)
    True

    Private attribute exists:
    >>> hasattr(s, "_Square__size")
    True
    """
    def __init__(self, size=0):
        self.__size = size