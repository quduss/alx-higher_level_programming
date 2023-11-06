#!/usr/bin/python3

""" is_same_class function"""


def is_same_class(obj, a_class):
    """ check if object is an instance of a_class
    Args:
        obj: object
        a_class: class
    Returns:
        True if obj is an instance otherwise false
    """
    return type(obj) is a_class
