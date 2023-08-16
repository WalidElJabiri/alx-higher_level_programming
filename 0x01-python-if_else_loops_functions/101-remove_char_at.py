#!/usr/bin/python3
def remove_char_at(str, n):
    """remove char at n"""
    ms = list(str)
    if n < 0 or n > len(str):
        return str
    ms[n] = ""
    str = ''.join(ms)
    return str
