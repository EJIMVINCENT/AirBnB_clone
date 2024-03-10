#!/usr/bin/python3
"""A class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines the attributes of a City class"""

    state_id = ""
    name = ""
