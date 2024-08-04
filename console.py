#!/usr/bin/python3
'''Documentation: the entry point of the command interpreter'''
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        '''Doc: Exits the CLI'''
        return True

    def do_EOF(self, arg):
        '''Doc: Exits the CLI'''
        print()
        return True

    def emptyline(self):
        return False

    do_exit = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
