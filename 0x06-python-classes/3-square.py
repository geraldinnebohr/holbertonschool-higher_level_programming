#!/usr/bin/python3
class Square:
    """This is a Square class empty"""

    def __init__(self, size=0):
        """This is the __init__ method"""

        if type(size) is not int:
            raise ValueError('size must be >= 0')
        elif size < 0:
            raise TypeError('size must be an integer')
        else:
            self._Square__size = size

    def area(self):
        """This is a public instance method"""
        return self._Square__size * self._Square__size
