#!/usr/bin/python3
"""Defines a function that appends a string to a text file."""
def append_write(filename="file_append.txt", text="This School is so cool!\n"):
    """Appends a string to a text file (UTF8) and returns the number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)