from bwamu import area
from bwamu import mainmap as mm
import unittest

class MainmapAttributesTestCase(unittest.TestCase):
    """
    Contains tests for Mainmap instance attributes
    """

    @classmethod
    def setUpClass(cls):
        cls.test_main_map = mm.Mainmap()

    def test_map_has_areas(self):
        att = hasattr(self.test_main_map, 'areas')
        self.assertTrue(att)

    def test_map_has_start_id(self):
        att = hasattr(self.test_main_map, '_start_id')
        self.assertTrue(att)

    def test_map_has_num_of_areas(self):
        att = hasattr(self.test_main_map, '_num_of_areas')
        self.assertTrue(att)

class MainMapMethodsTestCase(unittest.TestCase):
    """
    Contains tests for Mainmap instance methods
    """

    @classmethod
    def setUpClass(cls):
        cls.test_main_map = mm.Mainmap()

    def test_update_areas(self):
        pre = len(self.test_main_map.areas)
        self.test_main_map._update_areas()
        post= len(self.test_main_map.areas)
        self.assertNotEqual(pre, post)
