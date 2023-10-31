#!/usr/bin/python3
"""matrix_divided function definition"""

string = "matrix must be a matrix (list of lists) of integers/floats"


def matrix_excep():
    raise TypeError(string)


def row_excep():
    raise TypeError("Each row of the matrix must have the same size")


def matrix_divided(matrix, div):
    """function that divides all elements in matrix
    Args:
        matrix: matrix argument
        div: integer or float to divide the matrix
    Returns:
        new list with the results of the division
    """
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if not (type(matrix) is list and len(matrix) > 0):
        matrix_excep()
    for list_ in matrix:
        if not (type(list_) is list and len(list_) > 0):
            matrix_excep()
    for list_ in matrix:
        for elem in list_:
            if not (type(elem) is int or type(elem) is float):
                matrix_excep()
    len_1 = len(matrix[0])
    for list_ in matrix:
        if len(list_) != len_1:
            row_excep()
    div = float(div)
    return [[round(x / div, 2) for x in row] for row in matrix]
