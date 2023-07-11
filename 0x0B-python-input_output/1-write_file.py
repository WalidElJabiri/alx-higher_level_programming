#!/usr/bin/python3
"""
module
"""


def write_file(filename="", text=""):
    """write file"""
    with open(filename, 'r') as fl:
        return fl.write(text)
