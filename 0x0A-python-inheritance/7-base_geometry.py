#!/usr/bin/python3
"""
    Module: 7-base_geometry
    Represents a base geometry
"""


class BaseGeometry:
    """
    Represents a base geometry class.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as a positive integer.

        Args:
            name (str): Name of the value.
            value (int): Value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not a positive integer.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
