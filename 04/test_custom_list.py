import unittest
from custom_list import CustomList


class TestCustomClass(unittest.TestCase):
    def test_custom_add(self):
        a = CustomList((1, 2, 3, 4, 5))
        b = CustomList((-1, -2, -3))
        self.assertEqual(a + b, CustomList([0, 0, 0, 4, 5]))

        a = CustomList((1, 2, 3, 4, 5))
        b = [1, 2, 3]
        self.assertEqual(a + b, CustomList([2, 4, 6, 4, 5]))

        a = [1, 2, 3, 4, 5]
        b = CustomList((1, 2, 3))
        self.assertEqual(a + b, CustomList([2, 4, 6, 4, 5]))

        a = CustomList()
        b = CustomList()
        self.assertEqual(a + b, CustomList())

    def test_custom_add_type(self):
        a = CustomList((1, 2, 3, 4, 5))
        b = [1, 2, 3]
        self.assertIsInstance(a + b, CustomList)

        a = [1, 2, 3]
        b = CustomList((1, 2, 3, 4, 5))
        self.assertIsInstance(a + b, CustomList)

    def test_custom_sub(self):
        a = CustomList((1, 2, 3, 4, 5))
        b = CustomList((-1, -2, -3))
        self.assertEqual(a - b, CustomList([2, 4, 6, 4, 5]))

        a = CustomList((1, 2, 3, 4, 5))
        b = [1, 2, 3]
        self.assertEqual(a - b, CustomList([0, 0, 0, 4, 5]))

        a = [1, 2, 3, 4, 5]
        b = CustomList((1, 2, 3))
        self.assertEqual(a - b, CustomList([0, 0, 0, 4, 5]))

        a = [1, 2, 3]
        b = CustomList((1, 2, 3, 4, 5))
        self.assertEqual(a - b, CustomList([0, 0, 0, -4, -5]))

        a = CustomList()
        b = CustomList()
        self.assertEqual(a - b, CustomList())

    def test_custom_sub_type(self):
        a = CustomList((1, 2, 3, 4, 5))
        b = [1, 2, 3]
        self.assertIsInstance(a - b, CustomList)

        a = [1, 2, 3]
        b = CustomList((1, 2, 3, 4, 5))
        self.assertIsInstance(a - b, CustomList)

    def test_custom_compare(self):
        self.assertTrue(CustomList([1, 2, 3, 4, 5]) == CustomList((15,)))
        self.assertTrue(CustomList([1, 2, 3, 4, 5]) == CustomList((1, 2, 3, 4, 5)))
        self.assertTrue(CustomList([1, 2, 3, 4, 5]) == CustomList((1, 2, 3, 4, 5.0000000000001)))
        self.assertFalse(CustomList([1, 2, 3, 4, 5]) == CustomList((1, 2, 3, 4, 5.00001)))
        self.assertFalse(CustomList([1, 2, 3, 0, 0, 0]) > CustomList((1, 2, 3, 4, 5)))
# print()
# print(CustomList([1, 2, 3]) < CustomList((1, 2, 3, 4, 5)))
# print(CustomList([1, 2, 3, 4, 5]) == CustomList((1, 2, 3, 4, 5)))
# print(CustomList([1, 2, 3]) != CustomList((1, 2, 3, 4, 5)))

if __name__ == "__main__":
    unittest.main()


# print([1, 2, 3] + CustomList((1, 2, 3, 4, 5)))
# print([1, 2, 3, 4, 5] + CustomList((1, 2, 3)))
# print(CustomList((1, 2, 3, 4, 5)) + [1, 2, 3])
# print(CustomList((1, 2, 3)) + [1, 2, 3, 4, 5])
#
# print([1, 2, 3] - CustomList((1, 2, 3, 4, 5)))
# print([1, 2, 3, 4, 5] - CustomList((1, 2, 3)))
# print(CustomList((1, 2, 3, 4, 5)) - [1, 2, 3])
# print(CustomList((1, 2, 3)) - [1, 2, 3, 4, 5])
#
# print(CustomList([1, 2, 3]) > CustomList((1, 2, 3, 4, 5)))
# print(CustomList([1, 2, 3]) < CustomList((1, 2, 3, 4, 5)))
# print(CustomList([1, 2, 3, 4, 5]) == CustomList((1, 2, 3, 4, 5)))
# print(CustomList([1, 2, 3]) != CustomList((1, 2, 3, 4, 5)))
# print(CustomList([1, 2, 3]))
