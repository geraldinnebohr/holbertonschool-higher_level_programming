#!/usr/bin/python3
"""
Class that defines a rectangle with 2 attributes
"""


class Rectangle:
    """
    Rectangle class
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.__width is 0 or self.__height is 0:
            return ""
        form = []
        for i in range(self.__height):
            form.append("#" * self.__width)
            form.append("\n")
        form.pop()
        return ("".join(form))

    def __repr__(self):
        return ('Rectangle({}, {})'
                .format(str(self.__width), str(self.__height)))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
