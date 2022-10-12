#!/usr/bin/python3
"""import modules"""


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

 
if __name__ == '__main__':
    HBNBCommand().cmdloop()
