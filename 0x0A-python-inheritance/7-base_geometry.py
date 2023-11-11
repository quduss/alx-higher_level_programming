#!/usr/bin/python3

"""BaseGeometry class definition"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """ calculates area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ raises exception if value is not an integer or <= 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if not (value > 0):
            raise ValueError("{} must be greater than 0".format(name))
