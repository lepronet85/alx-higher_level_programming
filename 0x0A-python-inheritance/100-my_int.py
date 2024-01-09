#!/usr/bin/python3
"""
Module: 100-my_int

Contains a class MyInt that inherits from int, inverting the == 
and != operators.
"""


class MyInt(int):
    """
    A class representing MyInt, inheriting from int.
    """

    def __eq__(self, other):
        """
        Override == operator to invert behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override != operator to invert behavior.
        """
        return super().__eq__(other)
