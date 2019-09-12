#!/usr/bin/python3
if __name__ == "__main__":
        from sys import argv
        addition = 0
        for i in range(1, len(argv)):
                addition += int(argv[i])
        print("{}".format(addition))
