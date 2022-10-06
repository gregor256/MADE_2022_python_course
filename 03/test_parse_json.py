"""TestParseJson"""
import unittest
from parse_json_by_keyword import parse_json, my_keyword_callback


class TestParseJson(unittest.TestCase):
    """TestParseJson"""
    def test_parse_json(self):
        """test_parse_json"""
        task_json_str = '{"key1": "Word1 word2", ' \
                        '"key2": "word2 word3", "key3": "word3 word3 word3 word3"}'
        task_required_fields = ["key1"]
        task_keywords = ["word2"]
        result = parse_json(task_json_str, task_required_fields,
                            task_keywords, my_keyword_callback)
        self.assertEqual(result, ["word2"])

        task_required_fields = ["key1", "key2"]
        result = parse_json(task_json_str, task_required_fields,
                            task_keywords, my_keyword_callback)
        self.assertEqual(result, ["word2", "word2"])

        task_required_fields = ["key2", "key3"]
        task_keywords = ["word2", "word3"]
        result = parse_json(task_json_str, task_required_fields,
                            task_keywords, my_keyword_callback)
        self.assertEqual(result, ["word2", "word3", "word3",
                                  "word3", "word3", "word3"])
