#!/usr/bin/python3

def element_at(my_list, idx):
    """retrieve element at index
    Args:
        my_list: list of element
        idx: index of element to be retrieved
    Returns:
        The element at idx
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
