#!/usr/bin/python3
"""Unittest for base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_normal_id_cases(self):
        self.assertEqual(Base(3).id, 3)
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(None).id, 2)
        self.assertEqual(Base(-12).id, -12)
        self.assertEqual(Base((1, 2)).id, (1, 2))
        self.assertEqual(Base([1, 3]).id, [1, 3])
        self.assertEqual(Base({1: 'hola'}).id, {1: 'hola'})
        self.assertEqual(Base(True).id, True)

    def test_id_errors(self):
        self.assertRaises(TypeError, Base, extra=0)
        self.assertRaises(TypeError, Base, 3, 4)
        self.assertRaises(TypeError, Base, "hola", 3)
        self.assertRaises(TypeError, Base, [1, 2], 3)
        self.assertRaises(TypeError, Base, (1, 2), 3)
        self.assertRaises(TypeError, Base, True, False)
        self.assertRaises(TypeError, Base, {1: 'hola'}, 1)
        self.assertRaises(TypeError, Base, None, None)
