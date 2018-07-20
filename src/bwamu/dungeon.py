#!/usr/bin/env python3

from bwamu import dungeon_map as dun_map
from bwamu import area

class Dungeon(area.Area):
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
