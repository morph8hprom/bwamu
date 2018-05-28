#!/usr/bin/env python3

from bwamu import dungeon
import unittest

class DungeonAttributesTestCase(unittest.TestCase):
    """
    Contains tests for Dungeon instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Creates a test instance of Dungeon
        """

        cls.test_dungeon = dungeon.Dungeon()

    def test_dungeon_has_id(self):
        att = hasattr(self.test_dungeon, 'id')
        self.assertTrue(att)

    def test_dungeon_has_name(self):
        att = hasattr(self.test_dungeon, 'name')
        self.assertTrue(att)

    def test_dungeon_has_desc(self):
        att = hasattr(self.test_dungeon, 'desc')
        self.assertTrue(att)

    def test_dungeon_has_map(self):
        att = hasattr(self.test_dungeon, 'map')
        self.assertTrue(att)
