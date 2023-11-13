#!/usr/bin/python3
from models.rectangle import Rectangle
from models.base import Base
import unittest

"""unittest for Rectangle class"""


class TestRectangle(unittest.TestCase):
    """testing rectangle class"""

    def test_init(self):
        """test instantiation"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_errors(self):
        """testing errors"""
        with self.assertRaises(TypeError):
            r4 = Rectangle()
        with self.assertRaises(TypeError):
            r4 = Rectangle(1)
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 2, 3, 4, 5, 6)
        r4 = Rectangle(2, 2, 0, 0, 0)
        with self.assertRaises(AttributeError):
            x = r4.__width
        with self.assertRaises(AttributeError):
            x = r4.__height
        with self.assertRaises(AttributeError):
            x = r4.__x
        with self.assertRaises(AttributeError):
            x = r4.__y

    def test_class(self):
        """testing if Rectangle is from Base"""
        self.assertTrue(issubclass(Rectangle, Base))
        r5 = Rectangle(2, 3, 0, 0, 0)
        self.assertTrue(isinstance(r5, Rectangle))
        self.assertTrue(isinstance(r5, Base))
