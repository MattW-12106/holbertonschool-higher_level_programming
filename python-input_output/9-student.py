#!/usr/bin/python3
"""Write a class Student that defines a student"""
class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initialize the Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}