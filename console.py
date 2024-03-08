#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place 
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class that define a command interpreter for our program"""
    prompt = "(hbnb) "

    __classes = [
                'BaseModel', 'User', 'Place',
                'State', 'City', 'Amenity', 'Review'
                ]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D)"""
        return True

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
        newBase = eval(arg1)()
        newBase.save()
        newBaseId = newBase.id
        print(newBaseId)

    def do_show(self, line):
        """Prints the string representation of an instance
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """

        if not line:
            print("** class name missing **")
            return
        my_list = line.split(" ")
        my_list[0] = my_list[0].strip(" ")

        if my_list[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(my_list) < 2:
            print("** no instance found **")
            return

        my_list[1] = my_list[1].strip(" ")
        objects = storage.all()
        key = my_list[0] + '.' + my_list[1]
        if key in objects:
            print(objects[key])
        else:
            print("** instance id missing **")           

    def do_destory(self, arg):
        """Deletes an instance based on the class name and id"""

        arg_list = arg.split()

        if not len(arg_list):
            print("** class name missing **")
            return

        elif arg_list[0] not in  HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        elif len(arg_list) < 2:
            print("** instance id missing **")
            return

        elif f'{arg_list[0]}.{arg_list[1]}' not in storage.all():
            print("** no instance found **")

        else:
            name_id = f'{arg_list[0]}.{arg_list[1]}'
            objs = storage.all()
            del objs[name_id]
            storage.save()
    
    def do_all(self, arg):
        """Prints all string representation of
        all instances based or not on the class name"""

        output = []
        objs = storage.all()
        if not arg:
            for key, value in objs.items():
                output.append(str(value))
            if (output):
                print(output)

        elif arg in HBNBCommand.__classes:
            for key, value in objs.items():
                class_name, id = key.split('.')
                if class_name == arg:
                    output.append(str(value))
            if output:
                print(output)
        else:
            print("** class doesn't exist **")


    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""

        argl = arg.split(' ')
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3].strip('"'))
            else:
                obj.__dict__[argl[2]] = argl[3].strip('"')
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def count(self, arg):
        """count the number of instances of a class"""
        counter = 0
        try:
            if arg not in self.__classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == arg:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")

    def default(self, arg):
        """Handles default commands"""
        args = arg.split(".")
        
        class_name, command = args
        if len(args) >= 2:
            if command == "all()":
                self.do_all(class_name)

            elif command == "count()":
                 self.count(class_name)

            elif command.startswith("show(") and command.endswith(")"):
                id = command.split('(')[1].split(')')[0]
                id = id.strip('"\'')
                key = f'{class_name} {id}'
                self.do_show(key)

            else:
                cmd.Cmd.default(self, arg)
        else:
            cmd.Cmd.default(self, arg)
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()   
