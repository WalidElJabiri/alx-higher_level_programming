#!/usr/bin/python3
"""
module
"""
import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename, 'r') as fl:
        return json.load(fl)
