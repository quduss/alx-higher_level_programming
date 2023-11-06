#!/usr/bin/python3

""" is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """ check if object is an instance of a_class
    Args:
        obj: object
        a_class: class
    Returns:
        True if obj is an instance otherwise false
    """
    return isinstance(obj, a_class)
