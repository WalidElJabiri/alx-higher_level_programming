#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    
    if idx >= 0 and idx < len(my_list):
        new = my_list.copy()
        new[idx] = new_element
        return new
    return (my_list)
