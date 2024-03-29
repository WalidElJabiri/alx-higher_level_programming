#!/usr/bin/python3
"""
module
"""
from models.base import Base


class Rectangle(Base):
    """.rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""                                                                                                      
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        def __str__(self):
            """str"""
            return "[Rectangle] ({}) {}/{} - {}/{}".format(
                    self.id, self.x, self.y, self.width, self.height)

