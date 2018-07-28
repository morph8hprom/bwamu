#!/usr/bin/env python3

"""
File contains main map object and related methods
"""
import json
from pkg_resources import resource_string
from bwamu import area

class Mainmap():
    def __init__(self, start_id = 1, num_of_areas = 3):
        self.areas = {}
        self._start_id = start_id
        self._num_of_areas = num_of_areas


    def _update_areas(self):
        """
        Used to build a dictionary of all areas from given directory
        Should only be used ONCE
        """
        d = {}
        for i in range(self._start_id, self._num_of_areas + 1):
            try:
                d[i] = self._build_area(i)
            except FileNotFoundError:
                print("File not found.  Please check to make sure it exists")
        self.areas = d

    def _build_area(self, id):
        jsontext = resource_string(__name__, 'data/area/area{}.json'.format(id))
        d = json.loads(jsontext.decode('utf-8'))
        d['id'] = id
        if d['area_type'] == 'Shop':
            a = area.Shop(**d)
        elif d['area_type'] == 'Dungeon':
            a = area.Dungeon(**d)
        return a
