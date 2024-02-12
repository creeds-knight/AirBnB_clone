#!/usr/bin/python3
""" A module to handle file storage"""
import json
import os
import importlib


class FileStorage():
    """ A class that defines attributes and methods
        to manipulate the items stored
        methods - all
                - new
                - save
                -reload
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ A method to return __object"""
        return FileStorage.__objects

    def new(self, obj):
        """ A method to set values of __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ A method to serialise objects to a file path"""
        ser_obj = {key: obj.to_dict() for key, obj in
                   FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(ser_obj, f)

    def reload(self):
        """ A methd to deserialise objects from a file"""
        classes = ["BaseModel", "User", "State",
                   "City", "Amenity", "Place", "Review"]
        if not os.path.exists(FileStorage.__file_path):
            pass
        else:
            with open(FileStorage.__file_path, 'r') as f:
                loaded_obj = json.load(f)
                for key, value in loaded_obj.items():
                    class_name, obj_id = key.split('.')
                    if class_name in classes:
                        if class_name == "BaseModel":
                            module_name = "models.base_model"
                        else:
                            module_name = f"models.{class_name.lower()}"
                        module = importlib.import_module(module_name)
                        class_ = getattr(module, class_name)
                        obj_instances = class_(**value)
                        FileStorage.__objects[key] = obj_instances
