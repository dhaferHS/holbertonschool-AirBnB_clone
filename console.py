#!/usr/bin/python3
"""import modules"""

from models.base_model import BaseModel
from datetime import datetime
import cmd
import sys


"""HBNB Command class file"""


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        sys.exit()

    def emptyline(self):
        """Empty line command"""
        pass
    
    def do_create(self, arg):
        """Create command that creates a new instance"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(arg)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Show command prints the string representation of an instance based on the class name and id"""
        array = arg.split()

        if len(array) < 1:
            print("** class name missing **")
        elif array[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(array) < 2:
            print("** instance id missing **")
        else:
            new_dict = storage.all()
            new_str = f"{array[0]}.{array[1]}"
            if new_str not in new_dict.keys():
                print("** no instance found **")
            else:
                print(new_dict[new_str])

    
 
if __name__ == '__main__':
    HBNBCommand().cmdloop()
