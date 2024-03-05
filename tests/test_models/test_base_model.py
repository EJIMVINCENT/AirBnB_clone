import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

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
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)

    def test_save_method_updates_updated_at(self):
        """Test if save() updates updated_at"""
        old_updated_at = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(old_updated_at, self.b1.updated_at)

    def test_str_method(self):
        """Test the __str__ method"""
        expected_str = f'[BaseModel] ({self.b1.id}) {self.b1.__dict__}'
        self.assertEqual(expected_str, str(self.b1))

    def test_to_dict_method(self):
        """Test the to_dict method"""
        dict_rep = self.b1.to_dict()
        self.assertIsInstance(dict_rep, dict)
        self.assertIn('__class__', dict_rep)
        self.assertEqual(dict_rep['__class__'], type(self.b1).__name__)
        self.assertIn('created_at', dict_rep)
        self.assertIsInstance(dict_rep['created_at'], str)
        self.assertIn('updated_at', dict_rep)
        self.assertIsInstance(dict_rep['updated_at'], str)

    def test_kwargs_notnone(self):
        """Test if kwargs is not None"""
        dict_rep = self.b1.to_dict()
        b3 = BaseModel(**dict_rep)
        self.assertEqual(dict_rep, b3.to_dict())

    def test_kwargs_is_none(self):
        """Test when kwargs is None"""
        b3 = BaseModel(None)
        self.assertIn('id', b3.__dict__)
        self.assertIn('created_at', b3.__dict__)
        self.assertIn('updated_at', b3.__dict__)

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


if __name__ == '__main__':
    unittest.main()
