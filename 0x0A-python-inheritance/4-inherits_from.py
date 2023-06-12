#!/usr/bin/python3
"""Defines one function that returns
True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class ;
otherwise False."""


def inherits_from(obj, a_class):
    """function that returns
    True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ;
    otherwise False.
    Args:
        obj (any): parameter of type (any).
        a_class (type): parameter of type (type).
    Returns:
        True if the object is an instance of a class that inherited
         (directly or indirectly) from the specified class ;
          otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
