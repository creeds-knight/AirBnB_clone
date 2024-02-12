#!/usr/bin/python3
""" A module that contains the console program"""
import cmd
import shlex
import re
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models import storage


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

    def parser(self, line):
        """ A method to properly parse the arguments passed into the
            command line
        """
        args = shlex.split(line)
        return args

    def execute_command(self, class_name, method_name, args):
        """ A method to get the command when using unreconginesd format"""
        all_args = "".join(args)
        if len(all_args) == 0:
            command = f"{method_name} {class_name}"
        else:
            command = f"{method_name} {class_name} {all_args}"
        self.onecmd(command)

    def default(self, line):
        """ A method to handle all unidentified arguments"""
        regex = r'^\b([A-Z][a-zA-Z0-9]*)\.\b([a-zA-Z_][a-zA-Z0-9]*)\((.*)\)$'
        classes = ["BaseModel", "User", "State",
                   "Place", "City", "Amenity", "Review"]

        match = re.match(regex, line)
        if not match:
            return super().default(line)
        class_name = match.group(1)
        method_name = match.group(2)
        idx = match.group(3)
        if class_name in classes:
            self.execute_command(class_name, method_name, idx)
        else:
            return super().default(line)

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
        args = self.parser(class_)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in class_map:
            class_inst = class_map[class_]()
            class_inst.save()
            print(class_inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ A method to show contents of the file """
        args = self.parser(line)
        classes = ["BaseModel", "User", "State",
                   "Place", "City", "Amenity", "Review"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
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
        args = self.parser(line)
        classes = ["BaseModel", "User", "State",
                   "Place", "City", "Amenity", "Review"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            del storage.all()[key]
            storage.save()

    def do_all(self, line):
        """ A method to print all instances"""
        args = self.parser(line)
        classes = ["BaseModel", "User", "State",
                   "Place", "City", "Amenity", "Review"]
        instances = []
        if len(args) == 0:
            for key, value in storage.all().items():
                instances.append(str(value))
            print(instances)
            return
        elif len(args) == 1:
            if args[0] in classes:
                for key, value in storage.all().items():
                    claas, idx = key.split('.')
                    if claas == args[0]:
                        instances.append(str(value))
                print(instances)
                return
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ A method to update an instance based on the class  name and id
            usage: update <class name> <id> <attribute name> "<atrribute>"""
        args = self.parser(line)
        classes = ["BaseModel", "User", "State",
                   "Place", "City", "Amenity", "Review"]
        key = "{}.{}".format(args[0], args[1])
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif key not in storage.all():
            print("** no instance found **")
        elif len(args) == 4:
            attr_name = args[2]
            attr = args[3]
            inst = storage.all()[key]
            setattr(inst, attr_name, attr)
            storage.save()

    def do_count(self, class_name):
        """ retrieve the number of instances of a particular class"""
        count = 0
        for key in storage.all():
            if key.startswith(class_name):
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
