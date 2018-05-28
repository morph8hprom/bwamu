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
        att = hasattr(self.test_dungeon, '_id')
        self.assertTrue(att)

    def test_dungeon_has_name(self):
        att = hasattr(self.test_dungeon, '_name')
        self.assertTrue(att)

    def test_dungeon_has_desc(self):
        att = hasattr(self.test_dungeon, '_desc')
        self.assertTrue(att)

    def test_dungeon_has_map(self):
        att = hasattr(self.test_dungeon, '_map')
        self.assertTrue(att)

class DungeonMethodsTestCase(unittest.TestCase):
    """
    Contains tests for Dungeon instance methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds test instance of Dungeon
        """
        cls.test_dungeon = dungeon.Dungeon()

    def test_dungeon_update_map(self):
        self.test_dungeon._update_map()
        att = self.test_dungeon._map
        self.assertIsNotNone(att)
