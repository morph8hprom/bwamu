#!/usr/bin/env python3

"""
Defines Area class and related methods
"""

class Area():
    def __init__(self, id = '1', name = 'test name',
                desc = 'test desc', area_type = None):
        self._id = id
        self._name = name
        self._desc = desc
        self._area_type = area_type
