#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry
"""
module
"""


class Rectangle(BaseGeometry):
    """rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
