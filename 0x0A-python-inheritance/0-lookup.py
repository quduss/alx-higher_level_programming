#!/usr/bin/python3

""" My lookup function"""


def lookup(obj):
    """ lists all available attributes and methods of an object
    Args:
        obj: the object involved
    Returns:
        a list object
    """
    return dir(obj)
