#!/usr/bin/python3
import os.path
from sys import argv


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


def load_add_save():
    """
    script that adds all arguments to a Python list
    """
    li = []
    fi = 'add_item.json'
    lenght = len(argv)
    i = 1
    if os.path.isfile(fi):
        li = load_from_json_file(fi)
        while i < lenght:
            li.append(argv[i])
            save_to_json_file(li, fi)
            i += 1
    else:
        open(fi, 'w')
        save_to_json_file(li, fi)
        while i < lenght:
            li.append(argv[i])
            save_to_json_file(li, fi)
            i += 1

if __name__ == '__main__':
    load_add_save()
