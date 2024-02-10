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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
