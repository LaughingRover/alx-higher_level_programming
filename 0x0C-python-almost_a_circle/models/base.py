#!/usr/bin/python3
"""
models Package

This package contains base classes for managing common attributes across
various classes in the project.

Submodules:
    base: Defines the Base class, a foundation for managing unique identifiers.
"""


class Base:
    """
    Base class for managing id attribute in all future classes.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of the
        number of objects created.

    Methods:
        __init__(self, id=None): Class constructor.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor for initializing Base instances.

        Args:
            id (int, optional): An integer representing the id of the instance.
            Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
