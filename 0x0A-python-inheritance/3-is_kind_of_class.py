#!/usr/bin/python3
"""
Module: 3-is_kind_of_class

Contains a function that checks if an object is an instance of a class,
or an instance of a class inherited from the specified class.

"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of a class or a
    subclass of the specified class; otherwise False.

    Args:
        obj: Any Python object.
        a_class: A Python class.

    Returns:
        bool: True if obj is an instance of a_class or its subclass,
        False otherwise.
    """
    return issubclass(type(obj), a_class)
