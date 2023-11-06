#!/usr/bin/python3

""" inherits_from function"""


def inherits_from(obj, a_class):
    """ check if object's class inherits directly or indirectly
    from a_class
    Args:
        obj: object
        a_class: class
    Returns:
        True if obj's class inherits from a_class otherwise false
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
