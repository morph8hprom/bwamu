#!/usr/bin/env python3

"""
Defines Area class and related methods
"""

from gim import shop_dict as Sd

class Area():
    def __init__(self, id = '1', name = 'test name',
                desc = 'test desc', area_type = None):
        self._id = id
        self._name = name
        self._desc = desc
        self._area_type = area_type

class Shop(area.Area):
    def __init__(self, id = '1', name = 'test name', desc = 'test desc',
                area_type = 'Shop', shopkeeper = None,
                items = [], stock = None):
        super().__init__(id, name, desc, area_type)
        self._shopkeeper = shopkeeper
        self._items = items
        self._stock = stock
        self._update_stock()

    def _update_stock(self):
        self._stock = Sd.ShopDict(items = self._items)
