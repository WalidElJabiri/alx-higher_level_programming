#!/usr/bin/python3
def print_reversed_list_integer(my_list):
    my_list.reverse()
    i = 0
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))