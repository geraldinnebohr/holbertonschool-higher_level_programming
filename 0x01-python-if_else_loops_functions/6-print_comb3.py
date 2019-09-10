#!/usr/bin/python3
for i in range(0, 9):
    i + 1
    for j in range(1, 10):
        if j > i:
            if i == 8:
                print("{}{}".format(i, j))
            else:
                print("{}{}, ".format(i, j), end="")
