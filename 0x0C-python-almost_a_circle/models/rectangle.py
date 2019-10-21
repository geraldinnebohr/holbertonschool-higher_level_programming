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
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self._Rectangle__height):
            for j in range(self._Rectangle__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[0]
                if arg == 1:
                    self.width = args[1]
                if arg == 2:
                    self.height = args[2]
                if arg == 3:
                    self.x = args[3]
                if arg == 4:
                    self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y =kwargs["y"]

    def to_dictionary(self):
        my_dict = self.__dict__
        new_dict = {}
        new_dict["width"] = my_dict["_Rectangle__width"]
        new_dict["height"] = my_dict["_Rectangle__height"]
        new_dict["id"] = my_dict["id"]
        new_dict["x"] = my_dict["_Rectangle__x"]
        new_dict["y"] = my_dict["_Rectangle__y"]
        return new_dict
