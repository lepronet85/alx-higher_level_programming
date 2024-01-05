#!/usr/bin/python3



class LockedClass():
    """Class to prevent dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass

    def __setattr__(self, name, value):
        """Prevent dynamic attribute creation"""
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(name))
        super().__setattr__(name, value)
