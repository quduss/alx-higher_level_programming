#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiating square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of square instance"""
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        return "[Square] ({}) {}/{} - {}".format(id, x, y, width)
