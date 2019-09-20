#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    mul = 0
    add = 0
    div = 0
    for i in my_list:
        mul = i[0] * i[1]
        add += mul
        div += i[1]
    return add / div
