#!/usr/bin/env python3
import abc
"""define an abstract class shaped by the ABC module"""
class Shape(abc.ABC):
    """abstract class"""
    @abc.abstractmethod
    def area(self):
        """abstract method"""
        pass
    @abc.abstractmethod
    def perimeter(self):
        """abstract method"""
        pass
    
class Circle(Shape):
    """Circle class that inherits from Shape"""
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        """calculate area of the circle"""
        return 3.14 * self.radius ** 2
    def perimeter(self):
        """calculate perimeter of the circle"""
        return 2 * 3.14 * self.radius
class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        """calculate area of the rectangle"""
        return self.width * self.height
    def perimeter(self):
        """calculate perimeter of the rectangle"""
        return 2 * (self.width + self.height)
    
def shape_info(shape):
    """function that takes a shape object and prints its area and perimeter"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")