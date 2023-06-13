#!/usr/bin/python3
def no_c(string):
    new = [x for x in string if x != 'C' and x != 'c']
    return ("".join(new))
