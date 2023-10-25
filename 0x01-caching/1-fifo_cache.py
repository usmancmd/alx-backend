#!/usr/bin/env python3
"""FIFOCache caching system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache class"""
    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """Assign value to a given key"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data.keys():
                f_key = next(iter(self.cache_data))
                del self.cache_data[f_key]
                print(f"DISCARD {f_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Get value of a given key"""
        return self.cache_data.get(key)
