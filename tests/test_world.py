# #!/usr/bin/env python3
#
# import unittest
# import os
# from src.world import *
# from src.map import *
# from src.room import *
#
#
#
# class WorldAttributeTestCase(unittest.TestCase):
#     """
#     Verifies all attributes of world instance
#     """
#     @classmethod
#     def setUpClass(cls):
#         """
#         Uses build_world function to create world data
#         """
#         start_id = 1
#         num_of_rooms = 5
#
#
#         cls.map = Map(build_map(start_id, num_of_rooms))
#         cls.start_loc = 1
#         cls.world = build_world(cls.map, cls.start_loc)
#
#     def test_world_has_map(self):
#         att = hasattr(self.world, 'map')
#         self.assertTrue(att)
#
#
#
#     def test_world_has_start_loc(self):
#         att = hasattr(self.world, 'start_loc')
#         self.assertTrue(att)
