#!/usr/bin/env python3

from bwamu import dungeon_map as dun_map

class Dungeon():
    def __init__(self, id = '1', name = 'test name',
                 desc = 'test desc', map = None):
                 self._id = id
                 self._name = name
                 self._desc = desc
                 self._map = map

    def _update_map(self):
        self._map = dun_map.DungeonMap(self._id)
        self._map._update_rooms()
