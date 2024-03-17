#!/usr/bin/python3
"""A class that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Define the attributes of a Review class"""

    place_id = ""
    user_id = ""
    text = ""
