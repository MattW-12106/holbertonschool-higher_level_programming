#!/usr/bin/python3
"""defines an empty class BaseGeometry"""
class BaseGeometry:
    """
    >>> bg = BaseGeometry()
    >>> bg.area()
    Traceback (most recent call last):
    Exception: area() is not implemented

    >>> bg.integer_validator("width", 10)
    >>> bg.integer_validator("width", 0)
    Traceback (most recent call last):
    ValueError: width must be greater than 0

    >>> bg.integer_validator("width", -3)
    Traceback (most recent call last):
    ValueError: width must be greater than 0

    >>> bg.integer_validator("width", "4")
    Traceback (most recent call last):
    TypeError: width must be an integer
    """
    def area(self):
        """raises an exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))