#!/usr/bin/env python3
"""
LRU Least Recently Used caching
"""
from sys import maxsize
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ FIFO Cache objects blue print """

    def __init__(self):
        """ initialize """
        super().__init__()
        self.keys = {}

    def put(self, key, item):
        """ put key to a value """
        if key and item:
            if key in self.cache_data:
                self.keys[key] += 1
            else:
                self.cache_data[key] = item
                self.keys[key] = 1
        if len(self.cache_data) > self.MAX_ITEMS:
            lst = maxsize
            for k, v in self.keys.items():
                if v < lst:
                    lst = v
                    discard = k
            print("DISCARD:", discard)
            del self.cache_data[discard]
            del self.keys[discard]

    def get(self, key):
        """ get cached data """
        if not key:
            return None
        val = self.cache_data.get(key)
        if val:
            self.keys[key] += 1
        return val
