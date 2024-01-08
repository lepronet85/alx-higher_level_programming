#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        list: List object containing attributes and methods of the object.
    """
    return dir(obj)
