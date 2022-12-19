"""LRUCache"""
from collections import deque
import logging
import logging.config
import argparse

log_conf = {
    "version": 1,
    "formatters": {
        "for_file": {
            "format": "%(asctime)s\t%(levelname)s\t%(message)s",
        },
        "for_std": {
            "format": "%(message)s",
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "filename": "cache.log",
            "formatter": "for_file",

        },
        "std_handler": {
            "level": "WARNING",
            "formatter": "for_std",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "file": {
            "level": "DEBUG",
            "handlers": ["file_handler"],
        },
        "std": {
            "level": "DEBUG",
            "handlers": ["std_handler", "file_handler"]
        },
    },
}


class LRUCache:
    """LRUCache"""

    def __init__(self, limit=42, logging_method='file'):
        self.limit = limit
        self.dictionary = {}
        self.order = deque()
        self.logger = logging.getLogger(logging_method)
        self.logger.info("Created LRUCache with parameters: limit=%s, "
                         "logging_method=%s.", limit, logging_method)

    def get(self, key=None):
        """LRUCache"""
        if key is None:
            self.logger.error('Trying to call LRUCache.get() '
                              'without parameter.')
        if key in self.dictionary:
            self.order.remove(key)
            self.order.append(key)
        else:
            self.logger.warning('Trying to get key from LRUCache that '
                                'does not exists: "%s"', key)
        return self.dictionary.get(key)

    def set(self, key='', value=''):
        """LRUCache"""
        if not key:
            self.logger.warning("Key field is empty.")
        if not value:
            self.logger.warning("Value field is empty.")
        self.logger.info('Element is added to cache: "%s": "%s"', key, value)
        if key in self.dictionary:
            self.get(key)
            if self.dictionary[key] != value:
                self.dictionary[key] = value
            return
        if len(self.dictionary) >= self.limit:
            to_remove = self.order.popleft()
            self.logger.debug('Key "%s" removed from cache', to_remove)
            self.dictionary.pop(to_remove)
        self.dictionary[key] = value
        self.order.append(key)


if __name__ == '__main__':
    logging.config.dictConfig(log_conf)
    logger = logging.getLogger('file')
    logger.debug('--- ANOTHER ONE START OF THE PROGRAM ---.')

    parser = argparse.ArgumentParser(description='logging_method')
    parser.add_argument('-s', help='logging_method', default='file')
    args = parser.parse_args()
    method = args.s

    cache = LRUCache(limit=1, logging_method=method)
    cache.set('key_1', 'val_1')
    cache.set()
    cache.get('key_2')
