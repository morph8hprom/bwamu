#!/usr/bin/env python3

from bwamu import dungeon_map as dun_map

class Dungeon():
    def __init__(self, id = '1', name = 'test name',
                 desc = 'test desc', map = None):
                 self.id = id
                 self.name = name
                 self.desc = desc
                 self.map = map
