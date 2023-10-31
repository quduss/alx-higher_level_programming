#!/usr/bin/python3
"""add_integer() function definiton"""


def add_integer(a, b=98):
    """Adds two integer
    Args:
        a: integer a
        b: integer b
    Returns:
        addition of a and b
    """
    if not (type(a) is int or type(a) is float):
        raise TypeError("a must be an integer")
    if not (type(b) is int or type(b) is float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
