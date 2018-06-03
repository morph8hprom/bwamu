#!/usr/bin/env python3

from gim import shop_dict as Sd

class Shop():
    def __init__(self, id = '1', name = 'test name', shopkeeper = None, items = [], stock = None):
        self._id = id
        self._name = name
        self._shopkeeper = shopkeeper
        self._items = items
        self._stock = stock
        self._update_stock()

    def _update_stock(self):
        self._stock = Sd.ShopDict(items = self._items)
