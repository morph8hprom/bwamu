#!/usr/bin/env python3

import unittest
from bwamu import area
from bwamu import room

class TestDungeonMapAttributes(unittest.TestCase):
    """
    Contains tests for DungeonMap instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds test instance of DungeonMap
        """
        cls.test_map = area.DungeonMap()

    def test_dungeon_map_has_id(self):
        att = hasattr(self.test_map, '_id')
        self.assertTrue(att)

    def test_dungeon_map_has_rooms(self):
        att = hasattr(self.test_map, '_rooms')
        self.assertTrue(att)

    def test_dungeon_map_has_start_loc(self):
        att = hasattr(self.test_map, '_start_loc')
        self.assertTrue(att)

class TestDungeonMapMethods(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        """
        Builds test instance of DungeonMap
        """
        cls.test_map = area.DungeonMap()

    def test_dungeon_map_build_room(self):
        att = self.test_map._build_room(1)
        self.assertTrue(att)

    def test_dungeon_map_update_rooms(self):
        pre = len(self.test_map._rooms)
        self.test_map._update_rooms()
        post = len(self.test_map._rooms)
        self.assertNotEqual(pre, post)
