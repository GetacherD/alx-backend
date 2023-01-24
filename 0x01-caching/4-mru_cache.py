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

    def put(self, key, item):
        """ put key to a value """
        if key and item:
            self.cache_data[key] = item
            discard = key
            if len(self.cache_data) > self.MAX_ITEMS:
                del self.cache_data[discard]
                print("DISCARD:", discard)

    def get(self, key):
        """ get cached data """
        if not key:
            return None
        return self.cache_data.get(key)
