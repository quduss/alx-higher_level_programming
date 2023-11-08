#!/usr/bin/python3

"""save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """writes an object to a text file
    Args:
        my_obj: corresponding object
        filename: name of text file
    """
    with open(filename, 'w', encoding='utf-8') as a_file:
        import json
        json.dump(my_obj, a_file)
