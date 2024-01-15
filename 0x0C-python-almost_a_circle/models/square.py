#!/usr/bin/python3
# saadsgh123 <sdsghouri@gmail.com>
# square.py
"""Define the class Square that inherits from Rectangle"""
import sys

from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
                if len(args) > 2:
                    self.x = args[2]
                    if len(args) > 3:
                        self.y = args[3]

    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

            
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"


if __name__ == '__main__':
    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)