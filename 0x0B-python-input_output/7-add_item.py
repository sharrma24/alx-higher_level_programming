#!/usr/bin/python3
"""Append command-line arguments to an existing Python list and save the updated list to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []
    
    new_items = sys.argv[1:]
    updated_items = existing_items + new_items
    save_to_json_file(updated_items, "add_item.json")


