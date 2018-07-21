#!/usr/bin/env python3

"""
Defines Area class and related methods
"""
from bwamu import dungeon_map as dun_map
from gim import shop_dict as Sd

class Area():
    def __init__(self, id = '1', name = 'test name',
                desc = 'test desc', area_type = None):
        self._id = id
        self._name = name
        self._desc = desc
        self._area_type = area_type

class Shop(Area):
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

class Dungeon(Area):
    def __init__(self, id = '1', name = 'test name',
                 desc = 'test desc', area_type = 'Dungeon', map = None):
                 super().__init__(id, name, desc, area_type)
                 self._map = map

    def _update_map(self):
        """
        Creates instance of DungeonMap using id of Dungeon
        and calls function to update rooms.
        Should only be used ONCE
        """
        # Creates an instance of DungeonMap using the id of Dungeon
        self._map = dun_map.DungeonMap(self._id)
        # Calls function to update rooms
        self._map._update_rooms()
