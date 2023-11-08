#!/usr/bin/python3

""" to_json_string function"""


def to_json_string(my_obj):
    """get the JSON representation of an object
    Args:
        my_obj: the corresponding object
    Returns:
        JSON representation of my_obj
    """
    import json
    return json.dumps(my_obj)
