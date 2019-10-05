#!/usr/bin/python3
"""
function that prints a new line when . or : or ? appear
Args: string
Return: string with the new line
"""


def text_indentation(text):
    """
    function that divides a matrix in an integer
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i - 1] in ".?:" and i > 0 and text[i] is " ":
            continue
        print(text[i], end="")
        if text[i] is "." or text[i] is "?" or text[i] is ":":
            print("\n")
