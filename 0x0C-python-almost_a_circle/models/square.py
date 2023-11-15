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

    @property
    def size(self):
        """public getter size for width or height"""
        return self.width

    @size.setter
    def size(self, value):
        """public setter size for width and height"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updating attributes of square instance with args or kwargs"""
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of a square"""
        dict_ = {}
        dict_["id"] = self.id
        dict_["size"] = self.size
        dict_["x"] = self.x
        dict_["y"] = self.y
        return dict_
