#!/usr/bin/env python3

import unittest
from gim import shop_dict as Sd
from bwamu import shop as S

class ShopAttributesTestCase(unittest.TestCase):
    """
    Contains tests for Shop instance attributes
    """

    @classmethod
    def setUpClass(cls):
        cls.test_shop = S.Shop()

    def test_shop_has_id(self):
        att = hasattr(self.test_shop, '_id')
        self.assertTrue(att)

    def test_shop_has_name(self):
        att = hasattr(self.test_shop, '_name')
        self.assertTrue(att)

    def test_shop_has_shopkeeper(self):
        att = hasattr(self.test_shop, '_shopkeeper')
        self.assertTrue(att)

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

        cls.test_shop = S.Shop()
        cls.test_list = [i for i in range(1,5)]


    def test_update_stock(self):
        self.test_shop._items = self.test_list
        self.test_shop._update_stock()
        self.assertIsInstance(self.test_shop._stock, Sd.ShopDict)
