import unittest
from crowdmap import Crowdmap

class FindPersonTests(unittest.TestCase):
    def setUp(self):
        self.crowdmap = Crowdmap(["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"])

    def test_getAllPostsForName(self):
        name = "Or"
        posts = self.crowdmap.get_all_posts_for(name)
        self.assertTrue(all(name in l for l in posts))

    def test_get_all_posts_for_missing_name(self):
        name = "Or2"
        posts = self.crowdmap.get_all_posts_for(name)
        self.assertTrue(all(name in l for l in posts))

    def test_includes_location_information(self):
        name = "Or"
        self.assertTrue(self.crowdmap.is_location(name))

    def test_includes_location_information_for_misssing_name(self):
        name = "Or2"
        self.assertFalse(self.crowdmap.is_location(name))

    def test_inconsistencies(self):
        name = "Or"
        self.assertTrue(self.crowdmap.is_inconsistencies(name))

    def test_inconsistencies_for_missing_name(self):
        name = "Or2"
        self.assertFalse(self.crowdmap.is_inconsistencies(name))