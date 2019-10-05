#!/usr/bin/python3
"""
function that concatenates 2 strings and print them
Args: 2 strings
Return: new string with the concatenated strings 3016377761
"""


def say_my_name(first_name, last_name=""):
    """
    function that divides a matrix in an integer
    """
    if type(first_name) is str:
        if type(last_name) is str:
            print("My name is {} {}".format(first_name, last_name))
        else:
            raise TypeError("last_name must be a string")
    else:
        raise TypeError("first_name must be a string")
