#!/usr/bin/python3

""" append_write function"""


def append_write(filename="", text=""):
    """appends string at the end of a text file
    Args:
        filename: name of text file
        text: string to append to text file
    Returns:
        number of characters written
    """
    with open(filename, 'a', encoding='utf-8') as a_file:
        x = a_file.write(text)
    return x
