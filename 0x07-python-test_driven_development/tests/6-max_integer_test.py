#!/usr/bin/python3
"""
    unittest module for max_integer() function
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer() function test cases"""

    def test_pos_int_list(self):
        """list parameter comprises positive integers only"""
        self.assertEqual(max_integer([4, 1, 2, 5, 3, 7]), 7)

    def test_neg_int_list(self):
        """list parameter comprises negative integers only"""
        self.assertEqual(max_integer([-4, -1, -2, -5, -3, -7]), -1)

    def test_pos_neg_int(self):
        """list parameter comprises both positive and negative integers only"""
        self.assertEqual(max_integer([-7, -4, 0, 2, 4]), 4)

    def test_empty_list(self):
        """list parameter comprises of an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_float_list(self):
        """list parameter comprises positive floating point numbers only"""
        self.assertEqual(max_integer([2.73, 2.45, 2.12, 2.88, 2.36]), 2.88)

    def test_neg_float_list(self):
        """list parameter comprises negative floating point numbers only"""
        self.assertEqual(max_integer([-2.73, -2.45, -2.12, -2.88, -2.36]), -2.12)

    def test_int_float_list(self):
        """
            list parameter comprises both positive and negative floating point
            numbers only
        """
        self.assertEqual(max_integer([2.73, -2.45, 2.12, -2.88, 2.36]), 2.73)

    def test_neg_pos_float_int(self):
        """
            list parameter comprises positive and negative integers and
            floating point numbers
        """
        self.assertEqual(max_integer([-2.45, 1, 0.92, -1, 2.64, -2, 1.35, -2.88, 0, -1.79]), 2.64)

    def test_string(self):
        """string argument passed to the list parameter"""
        self.assertEqual(max_integer("oesophagus"), 's')

    def test_type_error(self):
        """mixed data type list passed to the list parameter"""
        self.assertRaises(TypeError, max_integer, [3, "bee"])


