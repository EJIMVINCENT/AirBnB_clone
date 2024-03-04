#!/usr/bin/python3
""""Module that defines the Basemodel class"""


from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Parent class named Basemodel"""

    def __init__(self, *args, **kwargs):
        """Basemodel class constructor method"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(value,  '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,  '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'id':
                    self.id = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns class objects' visualization"""
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates the updated_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method for basic serialization"""

        obj_serialized = self.__dict__
        obj_serialized['__class__'] = self.__class__.__name__
        obj_serialized['created_at'] = self.created_at.isoformat()
        obj_serialized['updated_at'] = self.updated_at.isoformat()
        return obj_serialized
