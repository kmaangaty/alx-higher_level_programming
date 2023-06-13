#!/usr/bin/python3
"""Defines function that writes an Object to a text file,
 using a JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
 using a JSON representation.

    Args:
        my_obj (obj): parameter of type obj.
        filename (str): parameter of type str.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
