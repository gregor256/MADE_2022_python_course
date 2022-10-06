"""TestCustomClass"""
import unittest
from custom_list import CustomList


class TestCustomClass(unittest.TestCase):
    """TestCustomClass"""
    def test_custom_add(self):
        """test_custom_add"""
        first = CustomList((1, 2, 3, 4, 5))
        second = CustomList((-1, -2, -3))
        self.assertEqual(first + second, CustomList([0, 0, 0, 4, 5]))

        first = CustomList((1, 2, 3, 4, 5))
        second = [1, 2, 3]
        self.assertEqual(first + second, CustomList([2, 4, 6, 4, 5]))

        first = [1, 2, 3, 4, 5]
        second = CustomList((1, 2, 3))
        self.assertEqual(first + second, CustomList([2, 4, 6, 4, 5]))

        first = CustomList()
        second = CustomList()
        self.assertEqual(first + second, CustomList())

    def test_custom_add_type(self):
        """test_custom_add_type"""
        first = CustomList((1, 2, 3, 4, 5))
        second = [1, 2, 3]
        self.assertIsInstance(first + second, CustomList)

        first = [1, 2, 3]
        second = CustomList((1, 2, 3, 4, 5))
        self.assertIsInstance(first + second, CustomList)

    def test_custom_sub(self):
        """test_custom_sub"""
        first = CustomList((1, 2, 3, 4, 5))
        second = CustomList((-1, -2, -3))
        self.assertEqual(first - second, CustomList([2, 4, 6, 4, 5]))

        first = CustomList((1, 2, 3, 4, 5))
        second = [1, 2, 3]
        self.assertEqual(first - second, CustomList([0, 0, 0, 4, 5]))

        first = [1, 2, 3, 4, 5]
        second = CustomList((1, 2, 3))
        self.assertEqual(first - second, CustomList([0, 0, 0, 4, 5]))

        first = [1, 2, 3]
        second = CustomList((1, 2, 3, 4, 5))
        self.assertEqual(first - second, CustomList([0, 0, 0, -4, -5]))

        first = CustomList()
        second = CustomList()
        self.assertEqual(first - second, CustomList())

    def test_custom_sub_type(self):
        """test_custom_sub_type"""
        first = CustomList((1, 2, 3, 4, 5))
        second = [1, 2, 3]
        self.assertIsInstance(first - second, CustomList)

        first = [1, 2, 3]
        second = CustomList((1, 2, 3, 4, 5))
        self.assertIsInstance(first - second, CustomList)

    def test_custom_compare(self):
        """test_custom_compare"""
        self.assertTrue(CustomList([1, 2, 3, 4, 5]) == CustomList((15,)))
        self.assertTrue(CustomList([1, 2, 3, 4, 5]) ==
                        CustomList((1, 2, 3, 4, 5)))
        self.assertTrue(CustomList([1, 2, 3, 4, 5]) ==
                        CustomList((1, 2, 3, 4, 5.0000000000001)))
        self.assertFalse(CustomList([1, 2, 3, 4, 5]) ==
                         CustomList((1, 2, 3, 4, 5.00001)))
        self.assertFalse(CustomList([1, 2, 3, 0, 0, 0]) >
                         CustomList((1, 2, 3, 4, 5)))
        self.assertTrue(CustomList([1, 2, 3, 4, 5]) < CustomList((16,)))

    def test_custom_str(self):
        """test_custom_str"""
        self.assertEqual(str(CustomList((1, 2, 3))), '1 2 3; 6')


if __name__ == "__main__":
    unittest.main()
