#!/usr/bin/python3
"""
awedesfs
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor method
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        __str__ method
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """
        update method
        """
        if args is not None and len(args) > 0:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[0]
                if arg == 1:
                    self.size = args[1]
                if arg == 2:
                    self.x = args[2]
                if arg == 3:
                    self.y = args[3]
        else:
                for key, value in kwargs.items():
                    if key == "size":
                        self.size = value
                    if key == "width":
                        self.id = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """
        to_dictionary method
        """
        my_dict = self.__dict__
        new_dict = {}
        new_dict["size"] = my_dict["_Rectangle__width"]
        new_dict["id"] = my_dict["id"]
        new_dict["x"] = my_dict["_Rectangle__x"]
        new_dict["y"] = my_dict["_Rectangle__y"]
        return new_dict
