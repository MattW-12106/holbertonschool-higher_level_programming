#!/usr/bin/python3
"""
Write a class Student that defines a student by: 
(based on 10-student.py)
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_json(self):
        """Return the dictionary description with 
        simple data structure
        (list, dictionary, string, integer and boolean) 
        for JSON serialization
        of a Student instance (same as 8-class_to_json.py)
        """
        return self.__dict__
    
    def to_json(self, attrs=None):
        
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
    
    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance:
        (same as 10-student.py)
        """
        for key, value in json.items():
            setattr(self, key, value)