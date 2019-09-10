#!/usr/bin/python3
import random
number = random.randint(-10, 10)
i = number
if i > 0:
    print("{} is positive".format(i))
elif i < 0:
    print("{} is negative".format(i))
else:
    print("{} is zero".format(i))
