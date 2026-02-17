#!/usr/bin/python3

class Student:
    """Defines a student by first name, last name and age."""
    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}