#!/usr/bin/python3
"""import modules"""
import cmd
import sys
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage
import json
from models import storage


"""HBNB Command class file"""


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        sys.exit()

    def emptyline(self):
        """Empty line command"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
