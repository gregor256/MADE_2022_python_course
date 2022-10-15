"""gen_file_rows"""
import unittest
from collections import defaultdict
from big_file_reader import gen_file_rows


class TestReader(unittest.TestCase):
    """gen_file_rows"""
    def test_big_file_reader(self):
        """gen_file_rows"""
        result = defaultdict(list)
        patterns = ['роза', 'розан']
        for string in gen_file_rows('really_big_file.txt'):
            for pattern in patterns:
                if pattern in string.lower().split():
                    result[pattern].append(string)

        self.assertDictEqual(
            result, {'роза': [
                "1 а Роза упала на лапу Азора\n",
                "2 а Роза упала на лапу Азора\n"]})


if __name__ == '__main__':
    unittest.main()
