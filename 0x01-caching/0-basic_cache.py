#!/usr/bin/env python3
"""
caching basics demo
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Cache class inherintig from BaseCaching"""

    def __init__(self):
        """ initialize instance"""
        super().__init__()

    def put(self, key, item):
        """ put cache item to cache dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ get item from cache """
        if not key:
            return None
        return self.cache_data.get(key)
