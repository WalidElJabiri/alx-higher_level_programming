#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry
"""
module
"""


class Rectangle(BaseGeometry):
    """rectangle"""
    def __init__(self, width, height):
        """init"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """area"""
        return self.__width * self.__height
    def __str__(self):
        """str"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
