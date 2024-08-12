#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     '''
    #     Patch the standard output to a StringIO object (to capture the output)
    #     '''
    #     cls.patcher = patch('sys.stdout', new=StringIO())
    #     cls.mock_terminal = cls.patcher.start()
    
    # @classmethod
    # def tearDownClass(cls):
    #     '''
    #     Stop the patch
    #     '''
    #     cls.patcher.stop()
    
    def setUp(self):
        self.patcher = patch('sys.stdout', new=StringIO())
        self.mock_terminal = self.patcher.start()
    
    def tearDown(self):
        self.patcher.stop()
    
    def test_create(self):
        CLI = HBNBCommand()
        CLI.onecmd('help create')
        output = self.mock_terminal.getvalue()
        expected = '''
        Doc: Creates a new instance of the given class, saves it to the JSON
        file and prints the id.
        Ex: $ create BaseModel
'''
        self.assertEqual(output, expected)
        # self.tearDown()
        # print(f'output:\n{output}')
        # self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
