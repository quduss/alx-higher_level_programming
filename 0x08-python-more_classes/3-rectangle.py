#!/usr/bin/python3

"""Adding properties to Rectangle class"""


class Rectangle:
    """Adding private insatnce attr width and height
    Adding properties to retrive and set width and height"""

    def __init__(self, width=0, height=0):
        """Rectangle instance creation
        Args:
            width: width of instance
            height: height of instance
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """width getter property"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter property
        Args:
            value: new width value to set instance
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter property
        Args:
            value: new height value to set instance
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area method"""
        return self.width * self.height

    def perimeter(self):
        """perimeter method"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """string representation of object"""
        if self.width == 0 or self.height == 0:
            return ""
        hashes = ["#" * self.width for x in range(self.height)]
        return "\n".join(hashes)
