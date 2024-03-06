#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Class that define a command interpreter for our program"""
    __classes = ["BaseModel"]
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing when received an empty line."""
        pass

    def do_create(self, arg):
        """Usage: create <class>
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        arg_list = arg.split()
        if not arg_list:
            print("** class name missing **")
            return
        arg1 = arg_list[0]
        if arg1 not in  HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        newBase = BaseModel(arg_list)
        newBase.save()
        newBaseId = newBase.id
        print(newBaseId)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
