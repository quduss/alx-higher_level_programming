#!/usr/bin/python3
"""Square class definition with private attribute __size"""


class Square:
    """Square definition with priv attr __size"""
    def __init__(self, size=0):
        """initialize new square object
        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """retrieve size
        returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set size
        Args:
            value: new value of size
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate square area
        Returns:
            current square area
        """
        return self.__size ** 2

    def my_print(self):
        """print self"""
        if (self.size == 0):
            print()
        else:
            for x in range(self.size):
                for y in range(self.size):
                    print('#', end='')
                print()
