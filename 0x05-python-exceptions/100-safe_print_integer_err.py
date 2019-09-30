#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as ne:
        sys.stderr.write("Exception: " + str(ne) + "\n")
        return False
