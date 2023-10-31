#!/usr/bin/python3
"""print_square function definition"""


def print_square(size):
    """prints a square with #
    Args:
        size: size of the square
    """
    if (type(size) is not int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()
