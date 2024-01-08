#!/usr/bin/python3
"""
Module: 8-rectangle

Contains BaseGeometry and Rectangle classes.
"""


class BaseGeometry:
    """
    An empty class representing BaseGeometry.
    """
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    """
    Represents a Rectangle inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

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
            raise ValueError(f"{name} must be > 0")
