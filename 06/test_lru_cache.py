"""test"""
import unittest
from lru_cache import LRUCache


class TestCache(unittest.TestCase):
    """test"""

    def test_algorithm(self):
        """test"""
        cache = LRUCache(2)
        cache.set("k1", "val1")

        self.assertDictEqual({"k1": "val1"}, cache.dictionary)
        cache.set("k2", "val2")

        self.assertIsNone(cache.get("k3"))
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertIsNone(cache.get("k2"))
        self.assertEqual(cache.get("k1"), "val1")

        # rewriting value of existing key
        cache.set("k1", "val1_1")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertIsNone(cache.get("k2"))
        self.assertEqual(cache.get("k1"), "val1_1")

        cache.get("k3")
        cache.set("k1", "val1_2")
        cache.set("k4", "val4")
        # since k1 was changed, assume that it was last recently used
        self.assertIsNone(cache.get("k3"))
        self.assertEqual(cache.get("k1"), "val1_2")
        self.assertEqual(cache.get("k4"), "val4")

    def test_single_capacity(self):
        """test"""
        cache = LRUCache(1)
        cache.set("k1", "val1")
        self.assertEqual(cache.get("k1"), "val1")
        cache.set("k1", "val1_2")
        self.assertEqual(cache.get("k1"), "val1_2")
        cache.set("k2", "val2")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertIsNone(cache.get("k1"))
