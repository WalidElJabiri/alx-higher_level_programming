#!/usr/bin/python3
def read_file(filename=""):
    """read file"""
    with open(filename, "r") as f:
        print(f.read(), end="")
 
