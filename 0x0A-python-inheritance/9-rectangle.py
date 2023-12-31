#!/usr/bin/python3

"""BaseGeometry class definition"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """instantiating with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes area of Rectangle instance"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of Rectangle instance"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
