#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    lis = list(new_dir.keys())

    for x in lis:
        new_dir[x] *= 2
    return (new_dir)
        
def print_sorted_dictionary(a_dictionary):
    sor = list(a_dictionary.keys())
    sor.sort()

    for x in sor:
        print("{}: {}".format(x, a_dictionary[x]))

