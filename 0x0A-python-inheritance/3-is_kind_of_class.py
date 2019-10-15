#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    function if an object is an instance or a inherited class
    """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
