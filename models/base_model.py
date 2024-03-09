#!/usr/bin/python3
""""Module that defines the Basemodel class"""


from uuid import uuid4
from datetime import datetime
import models

time_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """Parent class named Basemodel"""
 
    def __init__(self, *args, **kwargs):
        """Basemodel class constructor method
        Args:
            *args (tuple): Variable positional arguments (Not used).
            **kwargs (dict): Variable keyword arguments.
        """

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time_format)
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time_format)
            else:
                self.updated_at = datetime.now()
            if kwargs.get("id", None) is None:
                self.id = str(uuid4())
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
