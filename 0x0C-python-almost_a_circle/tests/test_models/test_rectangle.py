#!/usr/bin/python3
"""Unittest for base class"""


import unittest
import io
import sys
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_normal_rectangle_id_cases(self):
        self.assertEqual(Rectangle(10, 4).id, 3)
        self.assertEqual(Rectangle(1, 1, 1).id, 4)
        self.assertEqual(Rectangle(1, 1, 1, 1).id, 5)
        self.assertEqual(Rectangle(1, 1, 1, 1, 1).id, 1)
        self.assertEqual(Rectangle(1, 1, 1, 1, [1, 2]).id, [1, 2])
        self.assertEqual(Rectangle(1, 1, 1, 1, (1, 2)).id, (1, 2))
        self.assertEqual(Rectangle(1, 1, 1, 1, {1: 'hola'}).id, {1: 'hola'})
        self.assertEqual(Rectangle(1, 1, 1, 1, 'hola').id, 'hola')
        self.assertEqual(Rectangle(1, 1, 1, 1, True).id, True)
        self.assertEqual(Rectangle(1, 1, 1, 1, 1.5).id, 1.5)
        self.assertEqual(Rectangle(1, 1, 1, 1, None).id, 6)
        self.assertEqual(Rectangle(1, 1, 1, 0).id, 7)
        self.assertEqual(Rectangle(1, 1, 0, 1).id, 8)

    def test_rectangle_id_errors(self):
        self.assertRaises(TypeError, Rectangle, 1)
        self.assertRaises(TypeError, Rectangle, 0)
        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, 0, 10)
        self.assertRaises(ValueError, Rectangle, 10, -1)
        self.assertRaises(ValueError, Rectangle, -1, 10)
        self.assertRaises(ValueError, Rectangle, 1, 1, 1, -1)
        self.assertRaises(ValueError, Rectangle, 1, 1, -1, 1)
        self.assertRaises(TypeError, Rectangle, {1: 'hola'}, 1)
        self.assertRaises(TypeError, Rectangle, [1, 2], 1)
        self.assertRaises(TypeError, Rectangle, (1, 2), 1)
        self.assertRaises(TypeError, Rectangle, True, 1)
        self.assertRaises(TypeError, Rectangle, None, 1)
        self.assertRaises(TypeError, Rectangle, 3.4, 1)

    def test_rectangle_area_cases(self):
        self.assertEqual(Rectangle(10, 4).area(), 40)
        self.assertEqual(Rectangle(10, 4, 1, 1, 1).area(), 40)

    #def test_rectangle_display_cases(self):
        #self.assertEqual(Rectangle(2, 2).display(), '##\n##\n')

    def test_rectangle_update_cases(self):
        r1 = Rectangle(1, 1, 1, 1)
        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 5)
        self.assertEqual(r1.width, 5)

        r1.update(89, 3, 2)
        self.assertEqual(r1.height, 2)

        r1.update(3, 4, 5, 6)
        self.assertEqual(r1.x, 6)

        r1.update(4, 5, 6, 7, 8)
        self.assertEqual(r1.y, 8)

    def test_rectangle_update_kwargs_cases(self):
        r1 = Rectangle(1, 1, 1, 1)
        r1.update(id=89)
        self.assertEqual(r1.id, 89)

        r1.update(id=89, width=5)
        self.assertEqual(r1.width, 5)

        r1.update(id=89, width=3, height=2)
        self.assertEqual(r1.height, 2)

        r1.update(id=3, width=4, height=5, x=6)
        self.assertEqual(r1.x, 6)

        r1.update(id=4, width=5, height=6, x=7, y=8)
        self.assertEqual(r1.y, 8)
