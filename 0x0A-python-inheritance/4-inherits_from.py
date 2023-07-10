#!/usr/bin/python3
"""
module
"""
def inherits_from(obj, a_class):
    """inherits from"""
    return False if type(obj) is a_class else isinstance(obj, a_class)
