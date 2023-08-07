#!/usr/bin/python3
"""
square mpdule
"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """init"""
        self.__size = size

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size"""
        self.__size = value
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area"""
        return self.__size ** 2
