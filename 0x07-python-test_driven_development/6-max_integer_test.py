#!/usr/bin/python3
"""this file Defines Unittests for max_integer function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This is Unittests for TestMaxInteger class that test
    for max_integer function By using Unittests."""

    def test_ordered_list(self):
        """ordered list"""
        self.assertEqual(max_integer([10, 12, 14, 16]), 16)

    def test_string(self):
        """Test a string."""
        string = "Ahmed"
        self.assertEqual(max_integer(string), 'm')

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Ahmed", "not", "my", "name"]
        self.assertEqual(max_integer(strings), "not")

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        self.assertEqual(max_integer([2.53, 16.7, -11, 14, 35]), 35)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([49]), 49)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([16, 125, 311, 82, 90]), 311)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([7.49, 5.25, -11.111, 8.64, 9.81]), 9.81)


if __name__ == '__main__':
    unittest.main()
