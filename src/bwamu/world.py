#!/usr/bin/env python3

import json

"""
Defines a world class and a functon used to create an instance of the world class
"""

class World():
    def __init__(self,
        map,
        player):
        self.map = map
        self.player = player
        # self.start_loc = self.player.loc
        self.map._update_areas()
