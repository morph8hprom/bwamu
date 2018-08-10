#!/usr/bin/env python3

import unittest
from bwamu import world as w

"""
Contains tests for World class
"""

class WorldAttributesTestCase(unittest.TestCase):
    """
    Contains test for World instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds test instance of World using default parameters
        """
        cls.test_world = w.World()

    def test_world_has_start_id(self):
        att = hasattr(self.test_world, 'START_ID')
        self.assertTrue(att)

    def test_world_has_num_of_areas(self):
        att = hasattr(self.test_world, 'NUM_OF_AREAS')
        self.assertTrue(att)

    def test_world_has_num_of_items(self):
        att = hasattr(self.test_world, 'NUM_OF_ITEMS')
        self.assertTrue(att)

    def test_world_has_num_of_chars(self):
        att = hasattr(self.test_world, 'NUM_OF_CHARS')
        self.assertTrue(att)

    def test_world_has_start_loc(self):
        att = hasattr(self.test_world, 'START_LOC')
        self.assertTrue(att)

    def test_world_has_map(self):
        att = hasattr(self.test_world, '_map')
        self.assertTrue(att)

    def test_world_has_items(self):
        att = hasattr(self.test_world, '_items')
        self.assertTrue(att)

    def test_world_has_characters(self):
        att = hasattr(self.test_world, '_characters')
        self.assertTrue(att)
