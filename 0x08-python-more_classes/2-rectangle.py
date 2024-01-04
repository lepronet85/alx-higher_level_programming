#!/usr/bin/python3


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the Rectangle."""
        return getattr(self, '_Rectangle__width', 0)

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        setattr(self, '_Rectangle__width', value)

    @property
    def height(self):
        """Gets the height of the Rectangle."""
        return getattr(self, '_Rectangle__height', 0)

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        setattr(self, '_Rectangle__height', value)

    def area(self):
        """Returns the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        return 2 * (self.width + self.height) if self.width and
    self.height else 0
