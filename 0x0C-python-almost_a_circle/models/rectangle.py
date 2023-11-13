#!/usr/bin/python3
from models.base import Base
"""Rectangle class"""


class Rectangle(Base):
    """Rectangle class inheriting from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialise Rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set width"""
        self.__width = width

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        self.__height = height

    @property
    def x(self):
        """return x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set x"""
        self.__x = x

    @property
    def y(self):
        """return y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set y"""
        self.__y = y
