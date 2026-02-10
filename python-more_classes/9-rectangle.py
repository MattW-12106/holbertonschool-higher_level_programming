#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """A class representing a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize a Rectangle instance.
            width: The width of the rectangle (default is 0).
            height: The height of the rectangle (default is 0).
            number_of_instances: The number of Rectangle instances (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):        
        """Get the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
           value = The width value to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):        
        """Get the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
           value = The height value to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height
    
    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """Return a string representation of the rectangle using '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width for _ in range(self.__height)])
    
    def __repr__(self):
        """Return a string representation of the rectangle that can be used to recreate the instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
    
    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area.
           rect_1 = The first rectangle to compare.
           rect_2 = The second rectangle to compare.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
    
    def square(cls, size=0):
        """Return a new Rectangle instance with width and height equal to size.
           size = The size of the square (default is 0).
        """
        return cls(size, size)