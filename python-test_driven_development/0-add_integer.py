#!/usr/bin/python3
"""Adds two integers.

Prototype: def add_integer(a, b=98)
"""
def add_integer(a, b=98):
    """Adds two integers.

    >>> add_integer = __import__('0-add_integer').add_integer
    >>> add_integer("a", 1)
    Traceback (most recent call last):
    TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()