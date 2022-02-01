#!/usr/bin/python3
"""This Script adds all its arguments to a list
    and saves them into a file
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = [arg for arg in sys.argv]

save_to_json_file(args[1:], 'add_item.json')
