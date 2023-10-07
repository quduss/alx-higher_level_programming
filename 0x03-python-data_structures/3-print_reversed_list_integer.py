#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print integers of a list in reverse order
    Args:
        my_list: list of integers
    """
    start = len(my_list) - 1
    stop = -1
    for x in range(start, stop, -1):
        print("{:d}".format(my_list[x]))
