#!/usr/bin/env/ python3
from pkg_resources import resource_string
import json

"""
Defines a room class and a fucntion used to create an instance of room class
"""
class Room():
    def __init__(
        self,
        id = '1',
        name = 'test name',
        desc = 'test desc',
        exits = {}):
        self.id = id
        self.name = name
        self.desc = desc
        self.exits = exits

    def _exits(self, dir):
        """
        Verifies that provided exit is in room's list of exits
        """
        if dir in self.exits:
            return self.exits[dir]
        else:
            return None
