#!/usr/bin/env python3

from room import *
import json
"""
Defines a map class and a fucntion used to create an instance of map class
"""


class Map():
    def __init__(self, rooms = {}):
        self.rooms = rooms



def build_map(id, num_of_rooms):
    rooms = {}
    for i in range(id, num_of_rooms + 1):
        try:
            print("Gathering room data")
            rooms[i] = build_room(i)
            print("Successfully created room {} of {}".format(i, num_of_rooms))


        except FileNotFoundError:
            print("File not found.  Please check to make sure it exists")
    return rooms
