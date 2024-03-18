#!/usr/bin/python3
"""Test for Rectangle class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """testing Base class"""

    def test_instance(self):
        b1 = Base()
        self.assertIsInstance(b1, Base)

    def test_id(self):
        b2 = Base()
        self.assertEqual(b2.id, 1)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base(10)
        self.assertEqual(b4.id, 10)
