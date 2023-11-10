#!/usr/bin/python3

"""Adds all command line arguments to a python list
and save to a json file"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    x = load_from_json_file('add_item.json')
    import sys
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            x.append(sys.argv[i])
    save_to_json_file(x, 'add_item.json')
except FileNotFoundError:
    x = []
    import sys
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            x.append(sys.argv[i])
    save_to_json_file(x, 'add_item.json')
