#!/usr/bin/env python3

"""
File contains main map object and related methods
"""
from bwamu import area

class Mainmap():
    def __init__(self, start_id = 1, num_of_areas = 5):
        self._areas = {}
        self._start_loc = None
        self._start_id = start_id
        self._num_of_areas = num_of_areas

    def _update_areas(self):
        d = {}
        for i in range(self._start_id, self._num_of_areas + 1):
            try:
                d[i] = self._build_area(i)
            except FileNotFoundError:
                print("File not found.  Please check to make sure it exists")
        self._areas = d

    def _build_area(self, id):
        jsontext = resource_string(__name__, 'data/areas/area{}.json'.format(id))
        d = json.loads(jsontext.decode('utf-8'))
        d['id'] = id
        if d['area_type'] == 'Shop':
            area = area.Shop(**d)
        elif d['area_type'] == 'Dungeon':
            area = area.Dungeon(**d)
        return area
