#!/usr/bin/python3

"""Defines a function for writing text files."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number
    of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
