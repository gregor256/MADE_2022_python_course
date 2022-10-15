"""test"""
import unittest
from lru_cache import LRUCache


class TestCache(unittest.TestCase):
    """test"""
    def test_algorithm(self):
        """test"""
        cache = LRUCache(2)
        cache.add("k1", "val1")

        self.assertDictEqual({"k1": "val1"}, cache.dictionary)
        cache.add("k2", "val2")

        self.assertDictEqual({"k1": "val1", "k2": "val2"}, cache.dictionary)
        self.assertIsNone(cache.get("k3"))
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.add("k3", "val3")
        self.assertDictEqual({"k1": "val1", "k3": "val3"}, cache.dictionary)
