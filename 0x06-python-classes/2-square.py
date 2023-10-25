#!/usr/bin/python3
"""Square class definition with private attribute __size"""


class Square:
    """Square definition with priv attr __size"""
    def __init__(self, size=0):
        """initialize new square object
        Args:
            size: size of the square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
