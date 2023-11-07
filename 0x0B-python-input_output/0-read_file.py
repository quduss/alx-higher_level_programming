#!/usr/bin/python3

""" My read_file function"""


def read_file(filename=""):
    """reads a text file and prints to stdout
    Args:
        filename: name of text file to read
    """
    with open(filename, encoding='UTF-8') as a_file:
        print(a_file.read())
