#!/usr/bin/python3
"""Test for user class"""

import unittest
from models.user import User


class TestUserClass(unittest.TestCase):
    """Test case for user class"""

    def setUp(self):
        """Setup method for all class"""
        self.user1 = User()

    def test_all_attribute(self):
        """testing all attributes"""
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(self.user1.email == "")
        self.assertTrue(hasattr(User, 'last_name'))
        self.assertTrue(self.user1.last_name == "")
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(self.user1.first_name == "")
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(self.user1.password == "")
