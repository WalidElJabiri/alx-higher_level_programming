#!/usr/bin/python3
"""
module
"""


def append_write(filename="", text=""):
    """append write"""
    with open(filename, 'a') as fl:
        return fl.write(text)
