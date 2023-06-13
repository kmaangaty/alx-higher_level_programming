#!/usr/bin/python3
"""adds all arguments to a Python list,
 and then save them to a file"""

import sys

if __name__ == "__main__":
    stj = __import__('5-save_to_json_file').save_to_json_file
    lfj = __import__('6-load_from_json_file').load_from_json_file
    try:
        whd = lfj("add_item.json")
    except FileNotFoundError:
        whd = []
    whd.extend(sys.argv[1:])
    stj(whd, "add_item.json")
