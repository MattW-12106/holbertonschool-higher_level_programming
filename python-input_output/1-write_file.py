#!/usr/bin/python3
"""
This module provides a function to write a string to a text file 
and return the number of characters written.
"""
def write_file(filename="my_first_file.txt", text="This School is so cool!\n"):
    """Writes a string to a text file and returns the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)