#!/usr/bin/python3
"""say_my_name function definition"""


def say_my_name(first_name, last_name=""):
    """function that prints name
    Args:
        first_name: first name
        last_name: last name
    Returns:
        full name
    """
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
