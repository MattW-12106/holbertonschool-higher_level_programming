#!/usr/bin/python3
"""This module provides a function to read and print the contents of a file."""
def read_file(filename="my_file_0.txt"):
    """Reads a file and prints its contents."""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")