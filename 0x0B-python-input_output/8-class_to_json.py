#!/usr/bin/python3

"""class_to_json function"""


def class_to_json(obj):
    """ returns dictionary representation of an object
    Args:
        obj: The corresponding object
    """
    return obj.__dict__
