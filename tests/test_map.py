#!/usr/bin/env python3

import unittest
import os
from src.map import *
from src.room import *

class MapAttributesTestCase(unittest.TestCase):
    """
    Verifies all attributes of map class
    """
    @classmethod
    def setUpClass(cls):
        """
        Uses build_map function to create multiple room instances
        inside of the map object
        """
        
        start_id = 1
        num_of_rooms = 5
        cls.map = Map(build_map(start_id, num_of_rooms))

    def test_map_has_rooms(self):
        att = hasattr(self.map, 'rooms')
        self.assertTrue(att)

    def test_map_rooms_are_dict(self):
        att = self.map.rooms
        self.assertIsInstance(att, dict)
