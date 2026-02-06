#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix."""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix_divided(matrix, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    >>> matrix_divided(matrix, "3")
    Traceback (most recent call last):
    TypeError: div must be a number
    >>> matrix_divided([[1, 2], [3, 4, 5]], 2)
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size
    >>> matrix_divided([[1, 2], [3, "4"]], 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix_divided(matrix, float('inf'))
    Traceback (most recent call last):
    TypeError: div must be a number
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(element / div, 2) for element in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testmod()