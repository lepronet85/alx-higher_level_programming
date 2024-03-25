#!/usr/bin/python3

"""Defines a function to convert an object to its JSON representation."""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    import json
    return json.dumps(my_obj)
