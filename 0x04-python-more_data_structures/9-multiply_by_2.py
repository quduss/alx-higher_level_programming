#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """multiply values in dictionary by 2
    Args:
        a_dictionary: dictionary input
    Returns:
        new dictionary with modified values
    """
    return {key: a_dictionary[key] * 2 for key in list(a_dictionary)}
