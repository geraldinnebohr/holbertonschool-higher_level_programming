#!/usr/bin/python3
"""
This function adds two integers
Args: two integers
Return: integer
"""


def add_integer(a, b=98):
    """
    Function that adds two integers
    """
    if (type(a) is int or type(a) is float):
        if (type(b) is int or type(b) is float):
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
