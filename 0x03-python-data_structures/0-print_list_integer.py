#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints elements in a list of integers

    Args:
        my_list: list of integers
    """
    for element in my_list:
        print("{:d}".format(element))
