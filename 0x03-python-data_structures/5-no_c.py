#!/usr/bin/python3
def no_c(my_string):
    empty = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            empty = empty + i
    return empty
