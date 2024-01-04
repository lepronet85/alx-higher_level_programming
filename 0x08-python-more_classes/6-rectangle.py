#!/usr/bin/python3
"""Rectangle Class Module"""


class Rectangle:
    """Defines a rectangle and its properties."""

    number_of_instances = 0  # Number of Rectangle instances

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the Rectangle.

        Returns:
            int: The perimeter of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = ""
        for i in range(self.__height):
            rect += '#' * self.__width
            if i != self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message upon deletion of a Rectangle instance."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
