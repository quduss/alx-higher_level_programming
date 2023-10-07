#!/usr/bin/python3

def no_c(my_string):
    """remove character c and C from string
    Args:
        my_string: string input
    Returns:
        new string without c and C
    """
    new_string = ""
    for char in my_string:
        if char not in "cC":
            new_string += char
    return new_string
