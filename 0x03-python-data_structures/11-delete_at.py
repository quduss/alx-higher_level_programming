#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """delete item at index
    Args:
        my_list: list of integers
    Returns:
        modified list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    if len(my_list) == 0:
        return my_list
    del my_list[idx]
    return my_list
