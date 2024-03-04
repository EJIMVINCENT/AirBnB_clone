#!/usr/bin/python3
"""Module to test the class BaseModel"""

from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseClass(unittest.TestCase):
    """The class used to test BaseModel"""

    def setUp(self):
        """Create instances for test methods"""
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_id_is_str(self):
        """Test if id is a string object"""
        self.assertIsInstance(self.b1.id, str)

    def test_id_is_unique(self):
        """Test if id attribute is unique"""
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_datetime_objects(self):
        """Test if created_at and updated_at are datetime objects"""
        created = self.b1.created_at
        updated = self.b1.updated_at
        self.assertIsInstance(created, datetime)
        self.assertIsInstance(updated, datetime)
        

    def test_save_method_updates_updated_at(self):
        """Test if save() updates updated_at"""
        self.assertNotEqual(self.b1.updated_at, self.b1.save())

    def test_str_method(self):
        """Test the __str__ method"""
        expected_str = f'[{type(self.b1).__name__}] ({self.b1.id}) {self.b1.__dict__}'
        self.assertEqual(expected_str, str(self.b1))

    def test_to_dict_method(self):
        """Test fo the method to_dict()"""
        dict_return = self.b1.__dict__
        dict_return['__class__'] = self.b1.__class__.__name__
        created = self.b1.created_at.isoformat()
        updated  = self.b1.updated_at.isoformat()
        dict_return['created_at'] = created
        dict_return['updated_at'] = updated
        self.assertEqual(dict_return, self.b1.to_dict())

    def test_kwargs_not_none(self):
        """Test kwargs is not none"""
        dict1_rep = self.b1.to_dict()
        b3 = BaseModel(**dict1_rep)
        self.assertEqual(dict1_rep, b3.to_dict())
    
    def test_kwargs_is_none(self):
        """Test when kwargs is none"""
        dict1_rep = self.b1.to_dict()
        b3 = BaseModel(None)
        self.assertNotEqual(dict1_rep, b3.to_dict())

    def test_class_not_as_attributes(self):
        """Test if __class__ was added as an attribute"""
        dict_rep = self.b1.to_dict()
        b3 = BaseModel(**dict_rep)
        self.assertNotIn('__class__', b3.__dict__)
    
