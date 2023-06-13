#!/usr/bin/python3
""" Defines a function that appends a string at the
    end of a text file (UTF8) and returns the number of characters added."""


def append_write(filename="", text=""):
    """ unction that appends a string at the end of a text file
        (UTF8) and returns the number of characters added:

        Prototype: def append_write(filename="", text=""):
        If the file doesn’t exist, it should be created

    Args:
        filename (str): parameter of type str.
        text (str): parameter of type str.
    Returns:
        returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
