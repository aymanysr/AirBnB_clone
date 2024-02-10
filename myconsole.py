#!/usr/bin/python3
"""This is the console for the AirBnB clone"""

import cmd
import sys
import shlex  # for splitting the line into a list of arguments
from models.base_model import BaseModel
import models
classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """This is the console for the AirBnB clone"""
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing if an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def do_help(self, arg):
        """Prints the help"""
        cmd.Cmd.do_help(self, arg)
        print()

    def precmd(self, line):
        """This method is for non-interactive mode"""
        if not sys.stdout.isatty():
            print()
            return line.strip()
        return line

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name is missing **")
            return False
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return False
        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name is missing **")
            return False
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return False
        if key in models.storage.all():
            print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name is missing **")
            return False
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return False
        if key in models.storage.all():
            models.storage.all().pop(key)
            models.storage.save()

    def do_all(self, arg):
        """Prints str reprsntation of all instncs based or not on class name"""
        args = shlex.split(arg)
        class_name = args[0] if len(args) > 0 else None
        if class_name is not None and class_name not in classes:
            print("** class doesn't exist **")
            return False
        instances = [str(value) for key, value in models.storage.all().items()
                     if class_name is None or key.split('.')[0] == class_name]
        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return False
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        attr_name = args[2]
        attr_value = args[3]
        instance = models.storage.all()[key]
        if attr_name not in ["id", "created_at", "updated_at"]:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            elif '.' in attr_value:
                if attr_value.replace('.', '', 1).isdigit():
                    attr_value = float(attr_value)
            setattr(instance, attr_name, attr_value)
            instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
