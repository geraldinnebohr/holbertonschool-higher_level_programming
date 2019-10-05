#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_normal_cases(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([3, 1, 2, 5.4]), 5.4)
        self.assertEqual(max_integer([-2, 1, 5]), 5)
        self.assertEqual(max_integer(["hola", "chaito"]), "hola")
        self.assertEqual(max_integer(["Hola", "chaito"]), "chaito")
        self.assertEqual(max_integer([True, False]), True)
        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])
        self.assertEqual(max_integer([(1, 2), (3, 4)]), (3, 4))
        self.assertEqual(max_integer([1, True, False]), 1)
        self.assertEqual(max_integer(["a", "B", "c"]), "c")

    def test_errors(self):
        self.assertRaises(TypeError, max_integer, [1, "hola"])
        self.assertRaises(TypeError, max_integer, [1, [1, 2]])
        self.assertRaises(TypeError, max_integer, [1, (1, 2)])
        self.assertRaises(TypeError, max_integer, [{1, 2}, [3, 4]])
        self.assertRaises(TypeError, max_integer, [None, 1, 2])
        self.assertRaises(TypeError, max_integer, [None, None, None])
