#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """return x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """return y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """computes area of rectangle instance"""
        return self.width * self.height

    def display(self):
        """display self with hashes to stdout"""
        for h in range(self.y):
            print()
        for i in range(self.height):
            for w in range(self.x):
                print(" ", end='')
            for j in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """string representation of instance"""
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, width, height)
