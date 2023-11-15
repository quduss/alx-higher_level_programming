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

    @classmethod
    def save_to_file(cls, list_objs):
        """save the json representation of a list the dictionary
        representation of each instances in list_objs"""
        if list_objs is None:
            string = "[]"
        else:
            list_dict = [x.to_dictionary() for x in list_objs]
            string = cls.to_json_string(list_dict)
        name = cls.__name__
        with open("{}.json".format(name), 'w', encoding='utf-8') as file:
            file.write(string)
