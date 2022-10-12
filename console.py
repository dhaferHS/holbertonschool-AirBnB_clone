#!/usr/bin/python3
"""import modules"""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import json
import cmd
import sys
import os

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

 
if __name__ == '__main__':
    HBNBCommand().cmdloop()
