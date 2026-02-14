#!/usr/bin/python3
"""defines an empty class BaseGeometry"""
class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """raises an exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")