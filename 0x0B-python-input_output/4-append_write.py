#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    function that appends a string at end of text file (UTF8)
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
