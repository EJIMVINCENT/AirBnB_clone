#!/usr/bin/python3
"""Test for Review class"""

import unittest
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """Test case for Review class"""

    def setUp(self):
        """Setup method for all class"""
        self.Review1 = Review()

    def test_all_attribute(self):
        """testing all Review attributes"""
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(self.Review1.place_id == "")
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(self.Review1.user_id == "")
        self.assertTrue(hasattr(Review, "text"))
        self.assertTrue(self.Review1.text == "")
