#!/usr/bin/python3
"""
module
"""


class Student():
    """student class"""
    def __init__(self, fname, lname, age):
        """init"""
        self.first_name = fname
        self.last_name = lname
        self.age = age
    def to_json(self):
        """to json"""
        return self.__dict__
