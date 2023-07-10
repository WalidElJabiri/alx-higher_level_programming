#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
module
"""


class Square(Rectangle):
    """square"""
    def __init__(self, size):
        """init"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
    def area(self):
        """area"""
        return self.__size ** 2
