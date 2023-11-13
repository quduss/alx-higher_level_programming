import unittest
from models.base import Base

class TestRectangle(unittest.TestCase):
    """testing rectangle"""
    def test_init(self):
        """testing instantiation"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(1)
        self.assertEqual(b2.id, 1)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(-1)
        self.assertEqual(b4.id, -1)
        b5 = Base()
        self.assertEqual(b5.id, 2)
        b6 = Base()
        self.assertEqual(b6.id, 3)
        b6.id = 4
        self.assertEqual(b6.id, 4)
    def test_isBase(self):
        b7 = Base()
        self.assertTrue(type(b7) is Base)
