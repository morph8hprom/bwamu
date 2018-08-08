#!/usr/bin/env python3

import json
from bwamu import mainmap as mm
from upacc import character_dict as cd
from gim import item_dict as id

"""
File used to define World class and it's methods
"""

class World():
    def __init__(self,
        START_ID = 1,
        NUM_OF_AREAS = 1,
        NUM_OF_ITEMS = 1,
        NUM_OF_CHARS = 1
        DEFAULT_START_LOC = 1):
        self.START_ID = START_ID
        self.NUM_OF_AREAS = NUM_OF_AREAS
        self.NUM_OF_ITEMS = NUM_OF_ITEMS
        self.NUM_OF_CHARS = NUM_OF_CHARS
        self.START_LOC = DEFAULT_START_LOC

        # Create instance of Mainmap and update areas
        self._map = mm.Mainmap(self.START_ID, self.NUM_OF_AREAS)
        self._map._update_areas()

        # Create instance of Itemdict and update all items
        self._items = id.ItemDict(self.START_ID, self.NUM_OF_ITEMS)

        # Create instance of Chardict and update all characters
        self._characters = cd.CharacterDict(self.START_ID, self.NUM_OF_CHARS)
