#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find multiples of 2 in list
    Args:
        my_list: list of integers
    Returns:
        new list of either of True of False values with respect to the integer
    """
    new_list = []
    if len(my_list) == 0:
        return new_list
    for c in my_list:
        if c % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
