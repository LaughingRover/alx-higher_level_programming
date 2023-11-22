#!/usr/bin/python3

"""
This script defines a Square class.

The Square class represents a square shape with a specified size and position,
providing methods for calculating its area and printing a visual representation

Attributes:
    __size (int): The size of each side of the square. Default is 0.
    __position (tuple): The position of the square,
    represented as a tuple of two positive integers. Default is (0, 0).

Properties:
    size (int): Getter and setter property for the size of the square.
    position (tuple): Getter and setter property for the position of the square

Methods:
    __init__(self, size=0, position=(0, 0)): Initializes a new instance of
    the Square class.
    area(self): Calculates and returns the area of the square.
    my_print(self): Prints a visual representation of the square.

Raises:
    TypeError: If the provided size is not an integer or
    if the provided position is not a tuple of two positive integers.
    ValueError: If the provided size is less than 0.
"""


class Square:

    """
    A class to represent a square.

    Attributes:
        __size (int): The size of each side of the square. Default is 0.
        __position (tuple): The position of the square,
        represented as a tuple of two positive integers. Default is (0, 0).

    Properties:
        size (int): Getter and setter property for the size of the square.
        position (tuple): Getter and setter property for
        the position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a new instance
        of the Square class.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints a visual representation of the square.

    Raises:
        TypeError: If the provided size is not an integer or
        if the provided position is not a tuple of two positive integers.
        ValueError: If the provided size is less than 0.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): The size of each side of the square. Default is 0.
            position (tuple): The position of the square,
            represented as a tuple of two positive integers. Default is (0, 0).

        Raises:
            TypeError: If the provided size is not an integer or
            if the provided position is not a tuple of two positive integers.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or len(position) != 2 or not all(
                isinstance(elem, int) and elem >= 0 for elem in position):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Getter property for the size of the square.

        Returns:
            int: The size of each side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter property for the size of the square.

        Parameters:
            value (int): The new size of each side of the square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter property for the position of the square.

        Returns:
            tuple: The position of the square as a tuple
            of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter property for the position of the square.

        Parameters:
            value (tuple): The new position of the square,
            represented as a tuple of two positive integers.

        Raises:
            TypeError: If the provided value is not
            a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(
                isinstance(elem, int) and elem >= 0 for elem in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a visual representation of the square.

        If the size is 0, prints an empty line. Otherwise,
        prints the square with the specified position.
        """
        length = self.__position[0]
        height = self.__position[1]
        if self.__size == 0:
            print()
        else:
            for i in range(height):
                print()
            for i in range(self.__size):
                if length > 0:
                    print(" " * length, end="")
                print("#" * self.__size)
