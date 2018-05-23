#!/usr/bin/env/ python3
from pkg_resources import resource_string
import json

"""
Defines a room class and a fucntion used to create an instance of room class
"""
class Room():
    def __init__(
        self,
        id,
        name,
        desc,
        exits):
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


def build_room(id):
    room = None
    #Opens the file
    # f = resource_string(__name__, 'room{}.json'.format(id))
    # with open(f) as x:
    #     #Reads contents of file and stores in variable jsontext
    #     jsontext = x.read()
    #     #Decodes information from json file to a dictionary
    jsontext = resource_string(__name__, 'data/room{}.json'.format(id))
    d = json.loads(jsontext.decode('utf-8'))

    d['id'] = id
    room = Room(**d)
    return room
