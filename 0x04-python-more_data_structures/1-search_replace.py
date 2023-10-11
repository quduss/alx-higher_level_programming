#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replace search elements with replace
    Args:
        my_list: list of integers
        search: value to replace
        replace: new value to replace with
    Returns:
        new list with replaced values
    """
    new_list = []
    for x in my_list:
        if x == search:
            new_list.append(replace)
        else:
            new_list.append(x)
    return new_list
