#!/usr/bin/env python3
"""LIFO caching system"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class LIFOCache for LIFO cache system"""
    LAST_IN = ''

    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """Assign value to a given key"""
        if key is None or item is None:
            return
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                keys = self.cache_data.keys()

                if key not in keys:
                    del self.cache_data[LIFOCache.LAST_IN]
                    print(f"DISCARD: {LIFOCache.LAST_IN}")
                else:
                    self.cache_data[key] = item
                    LIFOCache.LAST_IN = key

                if key not in keys:
                    self.cache_data[key] = item
                    for key in keys:
                        LIFOCache.LAST_IN = key
            else:
                self.cache_data[key] = item
                keys = self.cache_data.keys()
                for key in keys:
                    LIFOCache.LAST_IN = key

    def get(self, key):
        """Get value for a given key"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None
