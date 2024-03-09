#!/usr/bin/python3
"""Defines unittests for models/base_model.py"""

import os
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""
    def __init__(self, *args, **kwargs):
        """ initallizes the tests"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel
    
    def setUp(self):
        """Create instances for test methods"""
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def tearDown(self):
        """perform cleanup
        operations after each test method"""
        try:
            os.remove('file.json')
        except Exception:
            pass
    
    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)


    def test_default(self):
        """Testin default """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_id_is_str(self):
        """Test if id is a string object"""
        self.assertIsInstance(self.b1.id, str)

    def test_id_is_unique(self):
        """Test if id attribute is unique"""
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_datetime_objects(self):
        """Test if created_at and updated_at are datetime objects"""
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)

    def test_save_method_updates_updated_at(self):
        """Test if save() updates updated_at"""
        old_updated_at = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(old_updated_at, self.b1.updated_at)

    def test_save(self):
        """ Testing save method"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        j = {}
        with open('file.json', 'r') as f:
            for line in f:
                c = json.loads(line)
                k = self.name + '.' + c['id']
                if k == key:
                    self.assertEqual(c, i.to_dict())
                    break

    def test_str_method(self):
        """Test the __str__ method"""
        expected_str = f'[BaseModel] ({self.b1.id}) {self.b1.__dict__}'
        self.assertEqual(expected_str, str(self.b1))

    def test_to_dict_method(self):
        """Test the to_dict method"""
        dict_rep = self.b1.to_dict()
        self.assertIsInstance(dict_rep, dict)
        self.assertIn('__class__', dict_rep)
        self.assertEqual(dict_rep['__class__'], self.b1.__class__.__name__)
        self.assertIn('created_at', dict_rep)
        self.assertIsInstance(dict_rep['created_at'], str)
        self.assertIn('updated_at', dict_rep)
        self.assertIsInstance(dict_rep['updated_at'], str)

    def test_to_dict2(self):
        """Test the to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_notnone(self):
        """Test if kwargs is not None"""
        dict_rep = self.b1.to_dict()
        b3 = BaseModel(**dict_rep)
        self.assertEqual(dict_rep, b3.to_dict())

        def test_kwargs_one(self):
            """ """
            n = {'Name': 'test'}
            with self.assertRaises(KeyError):
                new = self.value(**n)

    def test_kwargs_is_none(self):
        """Test when kwargs is None"""
        b3 = BaseModel(None)
        self.assertIn('id', b3.__dict__)
        self.assertIn('created_at', b3.__dict__)
        self.assertIn('updated_at', b3.__dict__)
    
    def test_kwargs_is_none2(self):
        """Test when kwargs is None"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_class_not_as_attributes(self):
        """Test if __class__ was added as an attribute"""
        dict_rep = self.b1.to_dict()
        b3 = BaseModel(**dict_rep)
        self.assertNotIn('__class__', b3.__dict__)

    # Additional tests for edge cases
    def test_init_with_kwargs(self):
        """Test initialization with kwargs"""
        b4 = BaseModel(id='123', created_at='2024-03-04T08:13:37.502557', updated_at='2024-03-04T08:13:37.502557')
        self.assertEqual(b4.id, '123')
        self.assertIsInstance(b4.created_at, datetime)
        self.assertIsInstance(b4.updated_at, datetime)

    def test_init_without_kwargs(self):
        """Test initialization without kwargs"""
        b5 = BaseModel()
        self.assertIsInstance(b5.id, str)
        self.assertIsInstance(b5.created_at, datetime)
        self.assertIsInstance(b5.updated_at, datetime)

    def test_updated_at(self):
        """test update """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)


if __name__ == '__main__':
    unittest.main()
