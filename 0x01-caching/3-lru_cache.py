#!/usr/bin/env python3
"""LRU caching system"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRUCache class"""
    count = {'space_1': 0, 'space_2': 0, 'space_3': 0, 'space_4': 0}

    def __init__(self):
        """init method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign value to a given key"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data.keys():
                last_key, last_value = self.cache_data.popitem(last=False)
                print(f"DISCARD {last_key}")

            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """Get value for a given key"""
        try:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        except KeyError:
            return None
