#!/usr/bin/python3
"""defines a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size):
        """initializes size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size
    
    def __str__(self):
        """returns the string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)