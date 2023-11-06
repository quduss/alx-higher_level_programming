#!/usr/bin/python3

""" MyList class"""


class MyList(list):
    """child class that inherits from list class"""

    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
