#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find biggest integer in a list
    Args:
        my_list: list of integers
    Returns:
        The biggest integer
    """
    if len(my_list) == 0:
        return None
    max_ = my_list[0]
    for c in my_list:
        if c > max_:
            max_ = c
    return max_
