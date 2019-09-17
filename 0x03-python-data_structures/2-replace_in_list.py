#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    for i in range(len(my_list)):
        if i == idx:
            my_list.insert(i + 1, element)
            my_list.remove(i + 1)
            return my_list
    return my_list
