#!/usr/bin/python3
"""This Script adds all its arguments to a list
    and saves them into a file
"""
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    old_add = load_from_json_file('add_item.json')
    save_to_json_file(old_add + argv[1:], 'add_item.json')
except Exception as ex:
    save_to_json_file(argv[1:], 'add_item.json')
