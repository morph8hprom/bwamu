#!/usr/bin/env python3

from gim import shop_dict as Sd
from bwamu import area
import unittest



class ShopAttributesTestCase(unittest.TestCase):
    """
    Contains tests for Shop instance attributes
    """

    @classmethod
    def setUpClass(cls):
        cls.test_shop = area.Shop()

    def test_shop_has_id(self):
        att = hasattr(self.test_shop, '_id')
        self.assertTrue(att)

    def test_shop_has_name(self):
        att = hasattr(self.test_shop, '_name')
        self.assertTrue(att)

    # IMPORTANT
    # Must update at later date
    # def test_shop_has_shopkeeper(self):
    #     att = hasattr(self.test_shop, 'shopkeeper')
    #     self.assertTrue(att)


    def test_shop_has_items(self):
        att = hasattr(self.test_shop, '_items')

    def test_shop_has_stock(self):
        att = hasattr(self.test_shop, '_stock')
        self.assertTrue(att)

class ShopMethodsTestCase(unittest.TestCase):
    """
    Contains tests for Shop instance methods
    """

    @classmethod
    def setUpClass(cls):
        cls.test_shop = area.Shop()
        cls.test_list = [i for i in range(1,5)]


    def test_update_stock(self):
        self.test_shop._items = self.test_list
        self.test_shop._update_stock()
        self.assertIsInstance(self.test_shop._stock, Sd.ShopDict)


class DungeonAttributesTestCase(unittest.TestCase):
    """
    Contains tests for Dungeon instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Creates a test instance of Dungeon
        """

        cls.test_dungeon = area.Dungeon()

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
        cls.test_dungeon = area.Dungeon()

    def test_dungeon_update_map(self):
        self.test_dungeon._update_map()
        att = self.test_dungeon._map
        self.assertIsNotNone(att)
