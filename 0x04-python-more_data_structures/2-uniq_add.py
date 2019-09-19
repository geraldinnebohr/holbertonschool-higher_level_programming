#!/usr/bin/python3
def uniq_add(my_list=[]):
    copy = my_list.copy()
    unique = set(copy)
    result = sum(unique)
    return result
