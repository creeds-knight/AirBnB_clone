#!/usr/bin/python3
""" A module for the users """
from models.base_model import BaseModel


class User(BaseModel):
    """ A class that defines attributes and methods for a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
