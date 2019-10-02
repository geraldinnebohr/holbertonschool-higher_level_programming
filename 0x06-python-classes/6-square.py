#!/usr/bin/python3
class Square:
    """This is a Square class empty"""

    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

    def area(self):
        """This is a public instance method"""
        return self.__size * self.__size

    @property
    def size(self):
        """This is a public instance method"""
        return self.__size

    @size.setter
    def size(self, value):
        """This is a public instance method"""

        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """This is a public instance method"""
        return self.__position

    @size.setter
    def position(self, value):
        """This is a public instance method"""

        if \
           type(value) is not tuple or len(value) is not 2 or \
           type(value[0]) is not int or type(value[1]) is not int \
           or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """This is a public instance method"""

        if self.__size:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size, end="")
            print("")
        else:
            print("")
