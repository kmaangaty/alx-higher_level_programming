#!/usr/bin/python3
"""Defines a class MyInt"""


class MyInt(int):
    """represent a class MyInt"""

    def __eq__(self, value):
        """MyInt is a rebel. MyInt has == and != operators inverted"""
        return self.real != value

    def __ne__(self, value):
        """MyInt is a rebel. MyInt has == and != operators inverted"""
        return self.real == value
