#!/usr/bin/python3
"""Test forPlace class"""

import unittest
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """Test case forPlace class"""

    def setUp(self):
        """Setup method for all class"""
        self.Place1 = Place()

    def test_all_attribute(self):
        """testing all attributes"""
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(self.Place1.description == "")
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(self.Place1.city_id == "")
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(self.Place1.user_id == "")
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(self.Place1.name == "")
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(self.Place1.number_rooms == 0)
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(self.Place1.number_bathrooms == 0)
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(self.Place1.max_guest == 0)
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(self.Place1.price_by_night == 0)
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(self.Place1.latitude == 0.0)
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(self.Place1.longitude == 0.0)
        self.assertTrue(hasattr(Place, "amenity_ids"))
        self.assertTrue(self.Place1.amenity_ids == [])
