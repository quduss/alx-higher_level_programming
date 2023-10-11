#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in list
    Args:
        my_list: list of integers
    Returns:
        sum of all unique integers
    """
    sum_ = 0
    for x in set(my_list):
        sum_ += x
    return sum_
