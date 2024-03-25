#!/usr/bin/python3

"""Defines a function to parse a JSON string into a Python data structure."""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be parsed.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    import json
    return json.loads(my_str)
