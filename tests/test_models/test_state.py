#!/usr/bin/python3
"""Test for State class"""

import unittest
from models.state import State


class TestStateClass(unittest.TestCase):
    """Test case for State class"""

    def setUp(self):
        """Setup method for all class"""
        self.State1 = State()

    def test_all_attribute(self):
        """testing all attributes"""
        self.assertTrue(hasattr(State, "name"))
        self.assertTrue(self.State1.name == "")
