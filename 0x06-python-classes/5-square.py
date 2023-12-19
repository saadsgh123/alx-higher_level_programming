#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """ Initialize a new square object

        Args:

            size (int): The size of the new square.
        """

        self.__size = size

    def area(self):
        return self.__size * self.__size

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

    def my_print(self):
        if self.__size > 0:
            for i in range(self.size):
                for i in range(self.__size):
                    print("{}".format("#"),end="")
                print("")
        else:
            print("")
