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
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
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
        created = self.created_at.isoformat()
        updated = self.updated_at.isoformat()
        obj_serialized = self.__dict__
        obj_serialized['__class__'] = self.__class__.__name__
        obj_serialized['created_at'] = created
        obj_serialized['updated_at'] = updated

        return obj_serialized
