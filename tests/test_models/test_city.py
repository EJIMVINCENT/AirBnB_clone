#!/usr/bin/python3
"""Test for City class"""

import unittest
from models.city import City


class TestCityClass(unittest.TestCase):
    """Test case for City class"""

    def setUp(self):
        """Setup method for all class"""
        self.City1 = City()

    def test_all_attribute(self):
        """testing all attributes"""
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(self.City1.state_id == "")
        self.assertTrue(hasattr(City, "name"))
        self.assertTrue(self.City1.name == "")
