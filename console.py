#!/usr/bin/python3
"""import modules"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models import storage
import models
import json
import cmd
import sys


"""HBNB Command class file"""


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User"]

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

    def do_destroy(self, arg):
        """Destroy command deletes an instance based on the class name and id"""
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
                del(new_dict[new_str])
                storage.save()
                
    def do_all(self, arg):
        """All command prints all string representation of all instances All command with a class prints the string representation of instances of this class"""
        new_list = []
        dict_obj = storage.all()

        if not arg:
            for key, value in dict_obj.items():
                new_list.append(str(value))
            print(new_list)
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for key, value in dict_obj.items():
                if value.__class__.__name__ == arg:
                    new_list.append(str(value))
            print(new_list)

    def do_update(self, arg):
        """Update command updates an instance based on the class name and id"""
        array = arg.split()
        if len(array) < 1:
            print("** class name missing **")
            return
        elif array[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(array) < 2:
            print("** instance id missing **")
            return
        else:
            new_dict = storage.all()
            new_str = f"{array[0]}.{array[1]}"
            if new_str not in new_dict.keys():
                print("** no instance found **")
            elif len(array) < 3:
                print("** attribute name missing **")
                return
            elif len(array) < 4:
                print("** value missing **")
                return
            else:
                setattr(new_dict[new_str], array[2], array[3])
                storage.save()            
 
if __name__ == '__main__':
    HBNBCommand().cmdloop()

