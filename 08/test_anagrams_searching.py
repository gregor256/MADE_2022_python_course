""" find_anagrams """
import unittest
from anagrams_searching import find_anagrams


class TestAnagrams(unittest.TestCase):
    """ find_anagrams """
    def test_types(self):
        """ find_anagrams """
        test_text = 'home'
        test_pattern = 'h'
        result = find_anagrams(test_text, test_pattern)
        self.assertIsInstance(result, list)
        self.assertRaises(TypeError, find_anagrams, 'abc', 1)
        self.assertRaises(TypeError, find_anagrams, 1, 'abc')

    def test_algorithm(self):
        """ find_anagrams """
        test_text = 'homme'
        test_pattern = 'home'
        result = find_anagrams(test_text, test_pattern)
        self.assertListEqual([], result)

        test_text = 'home'
        test_pattern = 'home'
        result = find_anagrams(test_text, test_pattern)
        self.assertListEqual([0], result)

        test_text = 'abcabc'
        test_pattern = 'abc'
        result = find_anagrams(test_text, test_pattern)
        self.assertListEqual([0, 1, 2, 3], result)

        test_text = 'abca1bca2cab3bbc'
        test_pattern = 'abc'
        result = find_anagrams(test_text, test_pattern)
        self.assertListEqual([0, 1, 5, 9], result)
