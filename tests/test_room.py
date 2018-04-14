#!/usr/bin/env/ python3

import unittest
from src.room import *
from src.map import *






class RoomAttributesTestCase(unittest.TestCase):
    """
    Contains tests for room object
    """
    @classmethod
    def setUpClass(cls):
        """
        Uses build map function from map.py to build multiple rooms for testing
        purposes
        """
        id = 1
        num_of_rooms = 5



        cls.map = Map(build_map(id, num_of_rooms))


    def test_room_has_id(self):
        """
        Verifies that room object has attribute id
        """

        for i in range(id, num_of_rooms + 1):
            att = hasattr(self.map.rooms[i], 'id')
            self.assertTrue(att)
    def test_room_has_name(self):
        """
        Verifies that room object has the attribute name
        """

        for i in range(id, num_of_rooms + 1):
            att = hasattr(self.map.rooms[i], 'name')
            self.assertTrue(att)
    def test_room_name_is_string(self):
        """
        Verifies that room object attribute name is a string
        """

        for i in range(id, num_of_rooms + 1):
            att = self.map.rooms[i].name
            self.assertIsInstance(att, str)
    def test_room_has_desc(self):
        """
        Verifies that room object has attribute desc
        """


        for i in range(id, num_of_rooms + 1):
            att = hasattr(self.map.rooms[i], 'desc')
            self.assertTrue(att)
    def test_room_desc_is_string(self):
        """
        Verifies that room object attribute desc is a string
        """

        for i in range(id, num_of_rooms + 1):
            att = self.map.rooms[i].desc
            self.assertIsInstance(att, str)

    def test_room_has_exits(self):
        """
        Verifies that room object has attribute exits
        """

        for i in range(id, num_of_rooms + 1):
            att = hasattr(self.map.rooms[i], 'exits')
            self.assertTrue(att)

    def test_room_exits_are_dict(self):

        for i in range(id, num_of_rooms +1):
            att = self.map.rooms[i].exits
            self.assertIsInstance(att, dict)
