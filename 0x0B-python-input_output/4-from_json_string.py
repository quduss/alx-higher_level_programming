#!/usr/bin/python3

"""from_json_string function"""


def from_json_string(my_str):
    """converts json string representation to object
    Args:
        my_str: json string representatiom
    Returns:
        object(Python data structure)
    """
    import json
    return json.loads(my_str)
