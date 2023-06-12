#!/usr/bin/python3
"""function that returns True if the object is exactly an
instance of the specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an
    instance of the specified class ; otherwise False..
    Args:
        obj (any): parameter of type (any).
        a_class (type): parameter of type (type).
    Returns:
        True if the object is exactly an
        instance of the specified class ;
        otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
