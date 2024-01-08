#!/usr/bin/python3
"""
Module: 2-is_same_class

Contains a function that returns True if the object is
exactly an instance of the specified class; otherwise False.

"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the
    specified class; otherwise False.

    Args:
        obj: Any Python object.
        a_class: A Python class.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
