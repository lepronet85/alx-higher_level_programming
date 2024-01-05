#!/usr/bin/python3


class LockedClass:
    """A class that allows only 'first_name' attribute assignment."""

    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """Set attribute 'first_name', disallowing any other attribute."""
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                     .format(name))
        self.__dict__[name] = value
