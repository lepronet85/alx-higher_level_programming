#!/usr/bin/python3

"""Defines a function for appending text to a file."""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8) and returns
    the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
