"""LRUCache"""
from collections import deque


class LRUCache:
    """LRUCache"""
    def __init__(self, max_size):
        self.max_size = max_size
        self.dictionary = {}
        self.order = deque()

    def get(self, key):
        """LRUCache"""
        if key in self.dictionary:
            self.order.remove(key)
            self.order.append(key)
        return self.dictionary.get(key)

    def add(self, key, value):
        """LRUCache"""
        if len(self.dictionary) >= self.max_size:
            to_remove = self.order.popleft()
            self.dictionary.pop(to_remove)
        self.dictionary[key] = value
        self.order.append(key)
