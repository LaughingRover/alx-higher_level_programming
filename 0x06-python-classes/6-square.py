#!/usr/bin/python3

class Square:

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and len(value) == 2 and all(elements >= 0 for elements in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        length = self.__position[0]
        height = self.__position[1]
        if self.__size == 0:
            print()
        else:
            for i in range(height):
                print()
            for i in range(self.__size):
                if length > 0:
                    print("_" * length, end="")
                print("#" * self.__size)

