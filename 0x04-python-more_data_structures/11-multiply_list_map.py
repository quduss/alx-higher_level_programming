#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """multiply list by number
    Args:
        my_list: list input
        number: number input
    Returns:
        new list with modified values
    """
    if len(my_list) == 0:
        return []
    return list(map(lambda x: x * number, my_list))
