#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers
    Args:
        matrix: matrix of integers
    """
    for j in range(len(matrix)):
        for k in range(len(matrix[j])):
            print("{:d}".format(matrix[j][k]), end="")
            if k != (len(matrix[j]) - 1):
                print(" ", end="")

        print("")
