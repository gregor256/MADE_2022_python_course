"""TestCountingDecorator"""
import time
import random
import unittest
from counting_decorator import counting


@counting(2)
def square_sleep_1(num):
    """square_sleep_1"""
    rand_sec = round(0.1 + random.random() * 0.01, 3)
    time.sleep(rand_sec)
    print(f'square_sleep_1 slept {rand_sec} seconds')
    return num * num


@counting(3)
def square_sleep_3(num):
    """square_sleep_3"""
    rand_sec = round(0.3 + random.random() * 0.01, 3)
    time.sleep(rand_sec)
    print(f'square_sleep_3 slept {rand_sec} seconds')
    return num * num


class TestCountingDecorator(unittest.TestCase):
    """TestCountingDecorator"""
    def test_counting_decorator(self):
        """test_counting_decorator"""
        for _ in range(6):
            square_sleep_1(10)
            square_sleep_3(10)
        self.assertTrue(True)
