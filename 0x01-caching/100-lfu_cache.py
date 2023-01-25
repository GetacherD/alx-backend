# !/usr/bin/env python3
"""
LRU Least Recently Used caching
"""
from random import choice
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ FIFO Cache objects blue print """

    def __init__(self):
        """ initialize """
        super().__init__()
        self.frequent = {}
        self.recent = {}

    def put(self, key, item):
        """ put key to a value """
        if key and item and len(self.cache_data) == self.MAX_ITEMS and (
                key not in self.cache_data):
            min_val = min(self.frequent.values())
            discard = []
            rm_key = None
            for k, v in self.frequent.items():
                if v == min_val:
                    discard.append(k)
            if len(discard) > 1:
                min_lru = self.recent[discard[0]]
                rm_key = discard[0]
                for k in discard:
                    if min_lru < self.recent[k]:
                        min_lru = self.recent[k]
                        rm_key = k
            else:
                rm_key = discard[0]
            print(f"DISCARD: {rm_key}")
            del self.frequent[rm_key]
            del self.recent[rm_key]
            del self.cache_data[rm_key]
        if key and item:
            if key in self.cache_data:
                self.frequent[key] += 1
                self.recent[key] = 0
            else:
                self.frequent[key] = 0
                self.recent[key] = 0
            for k in self.recent:
                if k != key:
                    self.recent[k] += 1
            self.cache_data[key] = item

    def get(self, key):
        """ get cached data """
        if not key:
            return None
        val = self.cache_data.get(key)
        if val:
            self.recent[key] = 0
            for k in self.recent:
                if k != key:
                    self.recent[k] += 1
            self.frequent[key] += 1
        return val
