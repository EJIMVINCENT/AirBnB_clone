#!/usr/bin/python3
"""a class User that inherits from BaseModel"""

from models.base_model import BaseModel
import models


class User(BaseModel):
    """Defines attributes a user has"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
