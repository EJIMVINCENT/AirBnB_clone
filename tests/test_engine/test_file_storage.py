#!/usr/bin/python3
"""Test file for fileStorage class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json



class TestFileStorage(unittest.TestCase):
    """Defines test modules for filestorage"""

    def setUp(self):
        """setUp method"""
        self.b1 = FileStorage()
        self.b2 = FileStorage()

    def test_file_path(self):
        """Test __file_path"""
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        with self.assertRaises(AttributeError):
            n = self.b1.__file_path
            
    def test_objects(self):
        """Test __object attribute"""
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        with self.assertRaises(AttributeError):
            n = self.b1.__objects
        
    def test_all_method(self):
        """Test the all method"""
        self.assertEqual(FileStorage._FileStorage__objects, self.b1.all())

    def test_new_method(self):
        """Test case for new method"""
        temp = BaseModel()
        self.b1.new(temp)
        self.assertIn(temp, FileStorage._FileStorage__objects.values())
        self.assertIn(f'{type(temp).__name__}.{temp.id}', FileStorage._FileStorage__objects.keys())

    def test_save_method(self):
        """Test cases for the save method"""
        self.assertFalse(os.path.exists(FileStorage._FileStorage__file_path))
        self.b1.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload_method(self):
        """Test reload method"""
        data = {"id": "1e21e0c8-3532-40ec-b068-bae5ecfa3075", "created_at": "2024-03-10T01:45:44.616472", "updated_at": "2024-03-10T01:45:44.616487", "__class__": "BaseModel"}
        with open(FileStorage._FileStorage__file_path, 'w') as f:
            json.dump(data, f)
        self.b1.reload()
        print(FileStorage._FileStorage__objects)
        print(data)

        self.assertTrue(data in FileStorage._FileStorage__objects.values())


if __name__ == '__main__':
    unittest.main()
