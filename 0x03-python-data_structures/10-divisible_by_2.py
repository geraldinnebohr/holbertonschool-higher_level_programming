#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy = my_list[:]
    for i in range(0, len(my_list)):
        if copy[i] % 2 == 0:
            copy[i] = True
        else:
            copy[i] = False
    return copy
