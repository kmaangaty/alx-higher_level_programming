#!/usr/bin/python3
"""Raise a TypeError exception, with the message
    can't add new attribute if the object can’t have new attribute
    You are not allowed to use try/except"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): parameter of type (any).
        att (str): parameter of type (str).
        value (any): parameter of type (any).
    Raises:
        TypeError: TypeError exception, with the message
        can't add new attribute if the object can’t have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
