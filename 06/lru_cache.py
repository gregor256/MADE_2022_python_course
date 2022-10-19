"""LRUCache"""
from collections import deque


class LRUCache:
    """LRUCache"""

    def __init__(self, limit=42):
        self.limit = limit
        self.dictionary = {}
        self.order = deque()

    def get(self, key):
        """LRUCache"""
        if key in self.dictionary:
            self.order.remove(key)
            self.order.append(key)
        return self.dictionary.get(key)

    def set(self, key, value):
        """LRUCache"""
        if key in self.dictionary:
            self.get(key)
            if self.dictionary[key] != value:
                self.dictionary[key] = value
            return
        if len(self.dictionary) >= self.limit:
            to_remove = self.order.popleft()
            self.dictionary.pop(to_remove)
        self.dictionary[key] = value
        self.order.append(key)
