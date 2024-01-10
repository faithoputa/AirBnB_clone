#!/usr/bin/python3
"""
Module for BaseModel
"""


import uuid
from datetime import datetime


class BaseModel:
    """ this is the BaseModel class """

    def __init__(self, *args, **kwargs):
        """Public instance attributes: common to the entire classes"""
        self.id = str(uuid.uuid4())
        dt = datetime(2017, 6, 14, 22, 31, 3, 285259)
        self.created_at = dt.isoformat()
        up_at = datetime(2017, 6, 14, 22, 31, 3, 285259)
        self.updated_at = up_at.isoformat()
        self.data_collection = {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def __str__(self):
        """The __str__ method to print classname, id, dictionary data """
        return (f"[<class name>] (<self.id>) <self.__dict__>:to be printed here")

    def save(self):
        pass


if __name__ == "__main__":
    newobj = BaseModel()
    print(newobj.data_collection)
