#!/usr/bin/env python3
"""serialize and deserialize custom Python objects using the pickle module"""
import pickle

class CustomObject:
    def __init__(self,name, age, is_student):
        """initialize the object's attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """display the object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename):
        """serialize the object to a pickle file"""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
    
    @classmethod
    def deserialize(cls, filename):
        """deserialize an object from a pickle file"""
        with open(filename, 'rb') as f:
            try:
                return pickle.load(f)
            except (pickle.UnpicklingError, FileNotFoundError):
                return None
        