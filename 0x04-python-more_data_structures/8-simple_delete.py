#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes key from dictionary
    Args:
        a_dictionary: dictionary input
        key: key input
    Returns:
        same dictionary
    """
    if key in dictionary:
        del a_dictionary[key]
    return a_dictionary
