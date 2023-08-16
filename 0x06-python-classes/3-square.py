#!/usr/bin/python3
"""
square mpdule
"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """init"""
        self.__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area"""
        return self.__size ** 2
