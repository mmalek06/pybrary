import unittest

from app.core.search import lev_dist


class TestLevDist(unittest.TestCase):
    def test_lev_dist(self):
        full_title = 'The Witcher'
        maybe_title = 'Teh Whitcher'
        expected_distance = 3

        resulting_distance = lev_dist(full_title, maybe_title)

        self.assertEqual(resulting_distance, expected_distance)
