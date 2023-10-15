#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Delete keys with specific value
    Args:
        a_dictionary: dictionary input
        value: value of keys to be deleted
    Return:
        same dictionary
    """
    keys = list(a_dictionary)
    for key in keys:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
