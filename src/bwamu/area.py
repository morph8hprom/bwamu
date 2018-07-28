#!/usr/bin/env python3

"""
Defines Area class and related methods and subclasses
"""
import json
from pkg_resources import resource_string
from bwamu import room as R
from gim import shop_dict as Sd


class Area():
    def __init__(self, id = '1', name = 'test name',
                desc = 'test desc', adj = {}, area_type = None):
        self.id = id
        self.name = name
        self.desc = desc
        self.adj = adj
        self._area_type = area_type

    def _adjacent(self, id):
        if id in self.adj:
            return True
        else:
            return None


class Shop(Area):
    def __init__(self, id = '1', name = 'test name', desc = 'test desc',
                adj = [], area_type = 'Shop', shopkeeper = None,
                items = [], stock = None):
        super().__init__(id, name, desc, adj, area_type)
        self._shopkeeper = shopkeeper
        self._items = items
        self._stock = stock
        self._update_stock()

    def _update_stock(self):
        self._stock = Sd.ShopDict(items = self._items)

class Dungeon(Area):
    def __init__(self, id = '1', name = 'test name',
                 desc = 'test desc', adj = [], area_type = 'Dungeon', map = None):
                 super().__init__(id, name, desc, adj, area_type)
                 self.map = map

    def _update_map(self):
        """
        Creates instance of DungeonMap using id of Dungeon
        and calls function to update rooms.
        Should only be used ONCE
        """
        # Creates an instance of DungeonMap using the id of Dungeon
        self.map = DungeonMap(self.id)
        # Calls function to update rooms
        self.map._update_rooms()



class DungeonMap():
    """
    Defines DungeonMap class and related methods
    """
    def __init__(self, id = '1', rooms = {},
                start_loc = '1', start_id = 1, num_of_rooms = 5):
        self._id = id
        self._rooms = rooms
        self._start_loc = start_loc
        self._start_id = start_id
        self._num_of_rooms = num_of_rooms


    def _update_rooms(self):
        d = {}
        for i in range(self._start_id, self._num_of_rooms + 1):
            try:
                d[i] = self._build_room(i)
            except FileNotFoundError:
                print("File not found.  Please check to make sure it exists")
        self._rooms = d

    def _build_room(self, id):
        jsontext = resource_string(__name__, 'data/dungeon/dungeon{}/room{}.json'.format(self._id, id))
        d = json.loads(jsontext.decode('utf-8'))
        d['id'] = id
        room = R.Room(**d)
        return room
