#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """
    fdff
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(width))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(width))
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(height))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(height))
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(x))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(x))
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(y))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(y))
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self._Rectangle__width):
            for j in range(self._Rectangle__height):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(super().__init__(id),
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)
