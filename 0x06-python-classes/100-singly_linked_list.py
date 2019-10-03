#!/usr/bin/python3
class Node:
    """This is a Node class"""

    def __init__(self, data, next_node=None):
        """This is the __init__ method"""

        if type(data) is not int:
            raise TypeError('data must be an integer')
        elif next_node is None or is Node:
            raise TypeError('next_node must be a Node object')
        else:
            self._Node__data = data
            self._Node__next_node = next_node


    @property
    def data(self):
        return self._Node__data

    @data.setter
    def data(self, value):
        self.value = value

        if type(data) is not int:
            raise TypeError('data must be an integer')
        elif next_node is None or is Node:
            raise TypeError('next_node must be a Node object')
        else:
            self._Node__data = value

class 
