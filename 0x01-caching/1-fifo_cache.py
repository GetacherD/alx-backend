#!/usr/bin/env python3
"""
FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Cache objects blue print """

    def __init__(self):
        """ initialize """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ put key to a value """
        if key and item:
            self.cache_data[key] = item
            self.keys.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")

    def get(self, key):
        """ get cached data """
        if not key:
            return None
        return self.cache_data.get(key)
