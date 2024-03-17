#!/usr/bin/python3
"""contains test cases for the entry
point of the command interpreter"""

import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """Defines methods for console test"""
    
    def setUp(self):
        """Sets up values for all methods"""
        self.c1 = HBNBCommand()
        pass

    def test_quit_method(self):
        """Test the quit command"""
        self.assertTrue(hasattr(HBNBCommand, 'do_quit'))
        self.assertTrue(self.c1.onecmd('quit') == True)

    def test_EOF_method(self):
        """Defines tests for EOF method"""
        self.assertTrue(hasattr(HBNBCommand, 'do_EOF'))
        self.assertTrue(self.c1.onecmd('EOF') == True)
    
    def test_help(self):
        """Tests the help method"""
        string = """
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.c1.onecmd('help')
            self.assertEqual(string, f.getvalue().strip())
        






if __name__ == '__main__':
    unittest.main()


