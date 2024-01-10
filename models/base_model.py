#!/usr/bin/python3
"""
Module for BaseModel
"""


from datetime import datetime
import uuid
import models


class BaseModel:
    """ this is the BaseModel class """

    def __init__(self, *args, **kwargs):
        """Public instance attributes: common to the entire classes
        ARGS: 
              Args, and Kwargs
              Note: Warning: created_at and updated_at are strings in this dictionary
              but inside your BaseModel instance is working with datetime object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            dt = datetime.now()
            self.created_at = dt.isoformat()
            up_at = datetime.now()
            self.updated_at = up_at.isoformat()
        models.storage.new(self)

    def __str__(self):
        """The __str__ method to print classname, id, dictionary data """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now().isoformat()
        models.storage.save()

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
