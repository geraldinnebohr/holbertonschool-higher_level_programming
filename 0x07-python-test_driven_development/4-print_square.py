#!/usr/bin/python3
"""
function that prints a square in #
Args: size of the square - integer
Return: square printed
"""


def print_square(size):
    """
    function that prints a square in #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size < 0 and type(size) is float:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
