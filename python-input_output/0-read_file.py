#!/usr/bin/python3
"""This module provides a function to read and print the contents of a file."""
def read_file(filename="my_file_0.txt"):
    """Reads a file and prints its contents."""
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents)