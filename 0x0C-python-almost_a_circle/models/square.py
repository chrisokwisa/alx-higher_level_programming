#!/usr/bin/python3
""" Module for square class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class constructor and methods """

    def __init__(self, size, x=0, y=0, id=None):
        """ Init for square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ __str__ method """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.height)

    @property
    def size(self):
        """ Size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) > 0:
            for i, args in enumerate(args):
                if i == 0:
                    self.id = args
                if i == 1:
                    self.size = args
                if i == 2:
                    self.x = args
                if i == 3:
                    self.y = args
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ To_dictionary method """
        return (
                {"id": self.id,
                 "size": self.size,
                 "x": self.x,
                 "y": self.y
                 }
               )
