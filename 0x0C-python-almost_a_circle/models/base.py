#!/usr/bin/python3

"""Base Class"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation with id attribute"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        import json
        return json.dumps(list_dictionaries)
