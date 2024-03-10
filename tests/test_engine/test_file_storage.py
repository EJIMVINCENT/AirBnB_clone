#!/usr/bin/python3
"""Test file for fileStorage class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
from models import storage


class TestFileStorage(unittest.TestCase):
    """Defines test modules for filestorage"""

    def setUp(self):
        """ Set up test environment """
        self.b1 = FileStorage()
        self.b2 = FileStorage()
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass


    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)


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

    def test_all_method2(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_new_method(self):
        """Test case for new method"""
        temp = BaseModel()
        self.b1.new(temp)
        self.assertIn(temp, FileStorage._FileStorage__objects.values())
        self.assertIn(f'{type(temp).__name__}.{temp.id}',
                      FileStorage._FileStorage__objects.keys())
    
    def test_new_method2(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)
    
    def test_base_model_instantiation(self):
        """ File is not created on BaseModel initalization """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save_method(self):
        """Test cases for the save method"""
        self.assertFalse(os.path.exists(FileStorage._FileStorage__file_path))
        self.b1.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload_method(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_method_empty(self):
        """ Load from an empty file """
        with open(FileStorage._FileStorage__file_path, 'w') as f:
            f.truncate(0)
        storage.reload()
        self.assertEqual(len(storage._FileStorage__objects), 0)
    
    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))
    
    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)
    
    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)

   
if __name__ == '__main__':
    unittest.main()
