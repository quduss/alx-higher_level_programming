#!/usr/bin/python3

"""Adding properties to Rectangle class"""


class Rectangle:
    """Adding private insatnce attr width and height
    Adding properties to retrive and set width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Rectangle instance creation
        Args:
            width: width of instance
            height: height of instance
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        a = self.print_symbol
        hashes = [str(a) * self.width for x in range(self.height)]
        return "\n".join(hashes)

    def __repr__(self):
        """canonical string representation of object"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """method that deletes instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """method to get the bigger rectangle of the two
        Args:
            rect_1: rectangle object 1
            rect_2: rectangle object 2
        Returns:
            the bigger rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """creates new instance with same width and height as size
        Args:
            size: width and height of new instance
        Returns:
            new instance
        """
        return cls(size, size)
