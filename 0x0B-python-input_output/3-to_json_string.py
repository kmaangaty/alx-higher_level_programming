#!/usr/bin/python3
""" Defines function that returns the JSON
    representation of an object (string)."""
import json


def to_json_string(my_obj):
    """function that returns the JSON
    representation of an object (string).

    Args:
        my_obj (obj): parameter of type obj.
    Returns:
        returns JSON representation of an object (string).
    """
    return json.dumps(my_obj)
