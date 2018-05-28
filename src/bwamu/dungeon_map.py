#!/usr/bin/env python3

import json
from pkg_resources import resource_string
from bwamu import room as R

class DungeonMap():
    def __init__(self, id = '1', rooms = {},
                start_loc = '1', start_id = 1, num_of_rooms = 5):
        self._id = id
        self._rooms = rooms
        self._start_loc = start_loc
        self._start_id = start_id
        self._num_of_rooms = num_of_rooms


    def _update_rooms(self):
        d = {}
        for i in range(self._start_id, self._num_of_rooms + 1):
            try:
                d[i] = self._build_room(i)
            except FileNotFoundError:
                print("File not found.  Please check to make sure it exists")
        self._rooms = d

    def _build_room(self, id):
        jsontext = resource_string(__name__, 'data/dungeon{}/room{}.json'.format(self._id, id))
        d = json.loads(jsontext.decode('utf-8'))
        d['id'] = id
        room = R.Room(**d)
        return room
