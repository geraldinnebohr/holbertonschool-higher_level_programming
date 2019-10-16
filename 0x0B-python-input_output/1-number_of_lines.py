#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    function that returns the number of lines of a text file
    """
    with open('my_file_0.txt', 'r', encoding='utf-8') as f:

        numberline = 0

        while True:
            line = f.readline()
            if not line:
                break
            numberline += 1
        return numberline
