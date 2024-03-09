#!/usr/bin/python3
""""Module that defines the Basemodel class"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Parent class named Basemodel"""
 
    def __init__(self, *args, **kwargs):
        """Basemodel class constructor method
        Args:
            *args (tuple): Variable positional arguments (Not used).
            **kwargs (dict): Variable keyword arguments.
        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns class objects' visualization"""
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates the updated_at attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Method for basic serialization"""
        if isinstance(self.created_at, str):
            created = self.created_at
        else:
            created = self.created_at.isoformat()
        if isinstance(self.updated_at, str):
            updated = self.updated_at
        else:
            updated = self.updated_at.isoformat()
        obj_serialized = self.__dict__
        obj_serialized['__class__'] = self.__class__.__name__
        obj_serialized['created_at'] = created
        obj_serialized['updated_at'] = updated
        return obj_serialized
