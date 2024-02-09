#!/usr/bin/python3
""" A Model for the AirBnB console that defines all common
    attributes and methods for the other classes
    methods include:-save
                    -to_dict
                    -str
                    -init
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """ The class basemodel contains definitions and attributes
         that are common to all the classes """
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        """ A method to manipulate the __str__ output of the base model"""
        cn = self.__class__.__name__
        return "[{}] ({}) {}".format(cn, self.id, self.__dict__)

    def save(self):
        """ A method that updates the updated_at attribute
            with the current the time and saves it to a file
        """
        BaseModel.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Return a dictionary containing all keys/values
            of __dict__ of an instance
        """
        dct = self.__dict__.copy()
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        dct['__class__'] = self.__class__.__name__
        dct['id'] = self.id
        return dct

    def __init__(self, *args, **kwargs):
        """ A method to initialise the base model
            and set attributes: - id
                                - created_at
                                - updated_at
                                - other attributes not set
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at'not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
