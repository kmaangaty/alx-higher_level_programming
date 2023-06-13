#!/usr/bin/python3
"""Defines function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”
    Args:
        filename (str): parameter of type str.
    Returns:
        json object.
    """
    with open(filename) as file:
        return json.load(file)
