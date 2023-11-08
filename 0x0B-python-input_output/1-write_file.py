#!/usr/bin/python3

"""write_file function"""


def write_file(filename="", text=""):
    """function that writes text to a file
    Args:
        filename: name of the file
        text: string to write to the file
    Returns:
        number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as a_file:
        x = a_file.write(text)
    return x
