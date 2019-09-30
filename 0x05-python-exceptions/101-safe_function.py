#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as ne:
        sys.stderr.write("Exception: " + str(ne) + "\n")
        return None
