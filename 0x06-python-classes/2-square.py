#!/usr/bin/python3
class Square:
    """This is a Square class empty"""

    def __init__(self, size=0):
        """This is the __init__ method"""

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size
