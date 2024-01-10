#!/usr/bin/python3
"""
Module for BaseModel
"""


import uuid
from datetime import datetime


class BaseModel:
    """ this is the BaseModel class """

    def __init__(self, *args, **kwargs):
        """Public instance attributes: common to the entire classes
        ARGS: Args, and Kwargs cautionary parameters
        """

        self.id = str(uuid.uuid4())
        dt = datetime.today()
        self.created_at = dt.isoformat()
        up_at = datetime.today()
        self.updated_at = up_at.isoformat()

    def __str__(self):
        """The __str__ method to print classname, id, dictionary data """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        self.data_collection = {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        return (self.data_collection)


if __name__ == "__main__":
    newobj = BaseModel()
    # print(newobj.to_dict())
