#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print integers of a list in reverse order
    Args:
        my_list: list of integers
    """
    if isinstance(my_list, list):
        range_ = len(my_list)
        for x in reversed(range(range_)):
            print("{:d}".format(my_list[x]))
