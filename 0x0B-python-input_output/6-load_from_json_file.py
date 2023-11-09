#!/usr/bin/python3

"""load_from_json_file function definition"""


def load_from_json_file(filename):
    """creates an object from a JSON file
    Args:
        filename: name of .json file
    Returns:
        object decoded from the json file
    """
    with open(filename, 'r', encoding='utf-8') as a_file:
        import json
        return json.load(a_file)
