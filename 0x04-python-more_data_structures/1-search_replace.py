#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(my_list)):
        if search is my_list[i]:
            new_list[i] = replace
    return new_list
