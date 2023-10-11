#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """square each value in a matrix
    Args:
        matrix: 2 dimensional array of integers
    Returns:
        new matrix with square values
    """
    return [[x ** 2 for x in row] for row in matrix]
