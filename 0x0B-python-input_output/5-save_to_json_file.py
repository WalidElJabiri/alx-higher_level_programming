#!/usr/bin/python3
"""
module
"""
import json


def save_to_json_file(my_obj, filename):
    """save to json file"""
    with open(filename, 'w') as fl:
        json.dump(my_obj, fl)
