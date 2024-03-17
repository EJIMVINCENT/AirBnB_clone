#!/usr/bin/python3
"""Test for Amenity class"""

import unittest
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """Test case for Amenity class"""

    def setUp(self):
        """Setup method for all class"""
        self.Amenity1 = Amenity()

    def test_all_attribute(self):
        """testing all attributes"""
        self.assertTrue(hasattr(Amenity, "name"))
        self.assertTrue(self.Amenity1.name == "")
