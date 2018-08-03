#!/usr/bin/env python3

import json
from bwamu import mainmap as mm
from upacc import character_dict as cd
from gim import item_dict as id

"""
Defines a world class and a functon used to create an instance of the world class
"""

class World():
    def __init__(self,
        START_ID = 1,
        NUM_OF_AREAS = 1,
        NUM_OF_ITEMS = 1,
        NUM_OF_CHARS = 1):
        self.START_ID = START_ID
        self.NUM_OF_AREAS = NUM_OF_AREAS
        self.NUM_OF_ITEMS = NUM_OF_ITEMS
        self.NUM_OF_CHARS = NUM_OF_CHARS

        # Create instance of Mainmap and update areas
        self.map = mm.Mainmap(self.START_ID, self.NUM_OF_AREAS)
        self.map._update_areas()

        # Create instance of Itemdict and update all items
        self.items = id.Itemdict(self.START_ID, self.NUM_OF_ITEMS)

        # Create instance of Chardict and update all characters
        self.characters = cd.CharacterDict(self.START_ID, self.NUM_OF_CHARS)
