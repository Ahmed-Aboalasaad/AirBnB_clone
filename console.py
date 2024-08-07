#!/usr/bin/python3
'''
Documentation: the entry point of the command interpreter

Rules:
- It assumes arguments are always in the right order
- Arguments are separated by spaces
- A string argument with a space must be between double quote
- The error management starts from the first argument to the last one
'''
import cmd
import models
import sys
import ast
from typing import Tuple


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def __is_valid_int(self, s) -> bool:
        '''Checks if the given string is an integer candidate'''
        try:
            int(s)
            return True
        except Exception:
            return False

    def __is_valid_float(self, s) -> bool:
        '''Checks if the given string is a float candidate'''
        try:
            float(s)
            return True
        except Exception:
            return False

    def do_quit(self, arg):
        '''Doc: Exits the CLI'''
        return True
    do_exit = do_quit

    def do_EOF(self, arg):
        '''Doc: Exits the CLI'''
        print()
        return True

    def emptyline(self):
        '''Makes the empty command do nothing'''
        return False

    def do_create(self, arg):
        '''
        Doc: Creates a new instance of the given class, saves it to the JSON
        file and prints the id.
        Ex: $ create BaseModel
        '''
        if arg == '':
            print('** class name missing **')
            return

        _class = models.class_registry.get(arg)
        if not _class:
            print("** class doesn't exist **")
            return

        obj = _class()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        '''
        Prints the string representation of an instance
        based on the class name and id
        Ex: $ show BaseModel 1234-1234-1234
        '''
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        class_name = args[0]
        _class = models.class_registry.get(class_name)
        if _class is None:
            print('** class doesn\'t exist **')
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        id = args[1]
        obj = models.storage.all().get(f'{class_name}.{id}')
        if obj is None:
            print('** no instance found **')
            return
        print(obj)

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id
        And saves the change into the JSON file
        Ex: $ destroy BaseModel 1234-1234-1234
        '''
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        class_name = args[0]
        _class = models.class_registry.get(class_name)
        if _class is None:
            print('** class doesn\'t exist **')
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        id = args[1]
        obj = models.storage.all().pop(f'{class_name}.{id}', None)
        if obj is None:
            print('** no instance found **')
            return
        models.storage.save()

    def do_all(self, arg):
        '''
        Prints string representation of all instances
        (of the given type, if any was provided)
        Ex: $ all BaseModel
        OR: $ all
        '''
        to_print = []
        if arg == '':
            for obj in models.storage.all().values():
                to_print.append(str(obj))
        else:
            args = arg.split()
            if models.class_registry.get(args[0]) is None:
                print("** class doesn't exist **")
                return
            for key, obj in models.storage.all().items():
                if key.split('.')[0] == args[0]:
                    to_print.append(str(obj))
        print(to_print)

    def do_update(self, arg):
        '''
        Updates an instance based on the class name and id by adding
        or updating attribute.
        Saves the change into the JSON file
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        - You mustn't try to update the attributes: created_at, updated_at, id
        - updates only simple arguments: strings, integers, floats
        '''
        # [1] Argument Checks
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        class_name = args[0]
        _class = models.class_registry.get(class_name)
        if _class is None:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        id = args[1]
        obj = models.storage.all().get(f'{class_name}.{id}')
        if obj is None:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        attribute = args[2]
        if len(args) == 3:
            print("** value missing **")
            return
        value = args[3]

        # [2] Casting the value to the attribute type
        # If such an attribute exists, cast the value to it
        if attribute in obj.__dict__:
            attr_type = type(getattr(obj, attribute))
            value = attr_type(value)
        # else, cast it to int, or float (if possible)
        else:
            if self.__is_valid_int(value):
                value = int(value)
            elif self.__is_valid_float(value):
                value = float(value)

        # [3] Updating the attribute & Saving the changes
        if attribute in ['created_at', 'updated_at', 'id']:
            return
        setattr(obj, attribute, value)
        models.storage.save()

    def onecmd(self, line: str) -> bool:
        '''
        Overrwriting the onecmd() method to process commands onctaining dots
        '''
        # [1] Handle Simple Commands
        if not ('.' in line and '(' in line and ')' in line):
            return self().onecmd(line)

        # [2] Handle Function-Like commands
        class_name, command_call = line.split('.', 1)

        # Extract from the command call the command_name, and its arguments
        try:
            # Try to Parse the Command
            # Using the abstract syntax tree module evaluation mode
            tree = ast.parse(command_call, mode='eval')

            # Make sure the parsed tree looks like a function call
            is_fun_call = isinstance(tree, ast.Expression)\
                          and isinstance(tree.body, ast.Call)
            if not is_fun_call:
                raise Exception('Abo: Invalid syntax\
                                for a function-like command')

            # Extract the method name
            if not isinstance(tree.body.func, ast.Attribute):
                raise Exception('Abo: Invalid syntax\
                                for a function-like command')
            command_name = tree.body.func.attr

            # Extract arguments
            args = [ast.literal_eval(arg) for arg in tree.body.args]

        except Exception as e:
            print(e)
            return False
        
        # [3] Call the resolved command
        command = command_name + ' ' + class_name + ' ' + ' '.join(args)
        return self.onecmd(command)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
