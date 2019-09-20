#!/usr/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    for i in roman_string:
        if i is "I":
            i = 1
        if i is "V":
            i = 5
        if i is "X":
            i = 10
        if i is "L":
            i = 50
        if i is "C":
            i = 100
        if i is "D":
            i = 500
        if i is "M":
            i = 1000
        add = sum(roman_string[i])
    return add
