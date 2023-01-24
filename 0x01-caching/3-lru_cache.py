#!/usr/bin/env python3
"""
LRU Least Recently Used caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ FIFO Cache objects blue print """

    def __init__(self):
        """ initialize """
        super().__init__()
        self.keys_cached = {}

    def put(self, key, item):
        """ put key to a value """
        if key and item:
            self.cache_data[key] = item
            self.keys_cached[key] = 0
            for k in self.cache_data:
                if k != key:
                    self.keys_cached[k] += 1
            if len(self.cache_data) > self.MAX_ITEMS:
                mx = 0
                for k, v in self.keys_cached.items():
                    if v > mx:
                        mx = v
                        discard = k
                del self.cache_data[discard]
                del self.keys_cached[discard]
                print("DISCARD:", discard)

    def get(self, key):
        """ get cached data """
        if not key:
            return None
        val = self.cache_data.get(key)
        if val:
            self.keys_cached[key] = 0
            for k in self.cache_data:
                if k != key:
                    self.keys_cached[k] += 1
        return val
