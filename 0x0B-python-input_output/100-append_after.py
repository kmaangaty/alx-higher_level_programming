#!/usr/bin/python3
""" Defines a function that inserts a line of text to a file,
    after each line containing a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    Args:
        filename (str): parameter of type (str).
        search_string (str): parameter of type (str).
        new_string (str): parameter of type (str).
    """
    nas = ""
    with open(filename) as saf:
        for sat in saf:
            nas += sat
            if search_string in sat:
                nas += new_string
    with open(filename, "w") as dat:
        dat.write(nas)
