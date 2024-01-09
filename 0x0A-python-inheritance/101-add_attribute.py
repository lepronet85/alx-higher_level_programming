#!/usr/bin/python3
"""
Module: 101-add_attribute

Contains a function add_attribute that adds a new attribute to
an object if possible.
"""

def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute will be added.
        attribute (str): The attribute name.
        value (any): The value to be assigned to the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
