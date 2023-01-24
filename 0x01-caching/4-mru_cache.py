#!/usr/bin/env python3
"""
LRU Least Recently Used caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ FIFO Cache objects blue print """

    def __init__(self):
        """ initialize """
        super().__init__()
        self.discard = None

    def put(self, key, item):
        """ put key to a value """
        if len(self.cache_data) == self.MAX_ITEMS and (
                key and item and key not in self.cache_data):
            del self.cache_data[self.discard]
            print("DISCARD:", self.discard)
        if key and item:
            self.cache_data[key] = item
            self.discard = key

    def get(self, key):
        """ get cached data """
        if not key:
            return None
        val = self.cache_data.get(key)
        if val:
            self.discard = key
        return val
