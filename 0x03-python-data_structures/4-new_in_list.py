#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """replace element at index
    Args:
        my_list: list of elements
        idx: idx of element to be replaced
        element: new element to be put at index
    Returns:
        modified copy of the list
    """
    my_list_copy = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_list_copy
    my_list_copy[idx] = element
    return my_list_copy
