#!/usr/bin/python3
""" A module for Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Attributes and methods to define review """
    place_id = ""
    user_id = ""
    text = ""
