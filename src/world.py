#!/usr/bin/env python3

import json

"""
Defines a world class and a functon used to create an instance of the world class
"""

class World():
    def __init__(self,
        map,
        start_loc):
        self.map = map
        self.start_loc = start_loc

def build_world(map, start_loc):
    print("Building world")
    world = World(map, start_loc)

    return world
