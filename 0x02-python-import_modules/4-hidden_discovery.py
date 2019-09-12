#!/usr/bin/python3
import hidden_4
names = dir(hidden_4)
for i in range(len(names)):
    if names[i][0:2] != "__":
        print("{}".format(names[i]))
