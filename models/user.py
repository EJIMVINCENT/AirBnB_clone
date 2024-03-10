#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv


class User(BaseModel):
    """Representation of a user """
 
    email = ""
    password = ""
    first_name = ""
    last_name = ""
