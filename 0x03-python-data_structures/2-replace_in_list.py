#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replace element at index function
    Args:
        my_list: list of elements
        idx: index of element to replace
        element: new element to put at index
    Returns:
        modified list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
