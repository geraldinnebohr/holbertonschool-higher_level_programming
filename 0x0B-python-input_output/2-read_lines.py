#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    function that reads n lines of a text file (UTF8) and prints it to stdout
    """
    with open('my_file_0.txt', 'r', encoding='utf-8') as f:
        numberline = 0
        if nb_lines <= 0:
            data = f.read()
            print(data, end="")
        else:
            while numberline < nb_lines:
                print(f.readline(), end="")
                numberline += 1
