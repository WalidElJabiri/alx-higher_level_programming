#!/usr/bin/python3
"""
module
"""
def read_file(filename=""):
    """read file"""
    with open(filename, 'r') as fl:
        print(fl.read(), end="")
 
