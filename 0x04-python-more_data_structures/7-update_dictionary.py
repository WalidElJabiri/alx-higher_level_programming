#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return (a_dictionary)
def print_sorted_dictionary(a_dictionary):
    sor = list(a_dictionary.keys())
    sor.sort()
    for x in sor:
        print("{}: {}".format(x, a_dictionary[x]))
