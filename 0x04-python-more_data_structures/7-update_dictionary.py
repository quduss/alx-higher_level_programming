#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replace or adds key/value in a dictionary
    Args:
        a_dictionary: dictionary input
        key: key input
        value: value input
    Returns:
        same dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
