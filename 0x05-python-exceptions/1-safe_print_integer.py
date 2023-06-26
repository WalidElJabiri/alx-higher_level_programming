#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".fornat(value))
        return (True)
    except TypeError:
        return (False)
    except ValueError:
        return (False)
