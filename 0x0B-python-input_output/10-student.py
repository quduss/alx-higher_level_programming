#!/usr/bin/python3

""" class Student definition"""


class Student:

    def __init__(self, first_name, last_name, age):
        """ initialise object with first_name, last_name
        and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return dictionary representation
        of instance
        Args:
            attrs: list of strings
        Returns:
            dictionary of only the attributes in the list otherwise
            all attributes are returned
        """
        if not (type(attrs) is list):
            return self.__dict__
        new_dict = {}
        real_dict = self.__dict__
        for i in attrs:
            if i in real_dict:
                new_dict[i] = real_dict[i]
        return new_dict
