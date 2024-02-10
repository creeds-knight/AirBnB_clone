#!/usr/bin/python3
""" A module that contains the console program"""
import cmd
import re
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Theee _AirBnB_ CONSOLE"""
    prompt = "(hbnb)"


    def do_quit(self, line):
        """A command to exit the program"""
        print()
        return True

    def do_EOF(self, line):
        """ Method to define EOF """
        print()
        return True

    def emptyline(self):
        pass

    def __str__(self):
        return f"[self.__class__.__name__] ({self.id}) {self.__dict__}"

    def do_create(self, class_):
        """ Creates a new instance of basemodel
            and stores it in a json file
        """
        class_map = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review,
                "Place": Place
                }
        if not class_:
            print("** class name missing **")
        elif class_ in class_map:
            class_inst = class_map[class_]()
            class_inst.save()
            print(class_inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ A method to show contents of the file """
        args = line.split()
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Review"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class name doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            print(storage.all()[key])

    def do_destroy(self, line):
        """ A method to del an instance based on the id"""
        args = line.split()
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Review"]
        if len(args) == 0:
            print("** class name is missing **")
        elif args[0] not in classes:
            print("** class name doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            del storage.all()[key]
            storage.save()

    def print_instances(self, instances):
        """ print instances without back lashes"""
        new_lst = []
        for item in instances:
            cleaned_instance = re.sub(r"['\"]", "", item)
            new_lst.append(cleaned_instance)
        print(new_lst)

    def do_all(self, line):
        """ A method to print all instances"""
        args = line.split()
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Review"]
        instances = []
        if len(args) == 0:
            for key, value in storage.all().items():
                instances.append(str(value))
            self.print_instances(instances)
            return
        elif len(args) == 1:
            if args[0] in classes:
                for key, value in storage.all().items():
                    instances.append(str(value))
                self.print_instances(instances)
                return
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """ A method to update an instance based on the class  name and id
            usage: update <class name> <id> <attribute name> "<atrribute>"""
        args = line.split()
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Review"]
        key = "{}.{}".format(args[0], args[1])
        if len(args) == 0:
            print("** class name is missing **")
        elif args[0] not in classes:
            print("** class name doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif key not in storage.all():
            print("** No instance found **")
        elif len(args) == 4:
            attr_name = args[2]
            attr = args[3]
            inst = storage.all()[key]
            setattr(inst, attr_name, attr)
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
