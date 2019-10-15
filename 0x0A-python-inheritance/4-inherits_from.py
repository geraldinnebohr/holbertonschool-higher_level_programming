#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class that/
    inherited (directly or indirectly) from the specified class
    """
    if isinstance(obj, a_class) and type(obj) is a_class:
        return False
    return True
