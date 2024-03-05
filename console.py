#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Class that define a command interpreter for our program"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D)"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()   



    
