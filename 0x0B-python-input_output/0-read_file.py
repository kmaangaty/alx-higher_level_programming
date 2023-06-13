#!/usr/bin/python3
"""Defines function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): parameter of type str.
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
