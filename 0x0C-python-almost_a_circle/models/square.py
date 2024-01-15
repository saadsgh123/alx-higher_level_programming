#!/usr/bin/python3
# saadsgh123 <sdsghouri@gmail.com>
# square.py
"""Define the class Square that inherits from Rectangle"""

from models.rectangle import Rectangle
"""Defines a square class."""


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
            - 1st argument represents id attribute
            - 2nd argument represents size attribute
            - 3rd argument represents x attribute
            - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
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
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
