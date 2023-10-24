#!/usr/bin/env python3
"""FIFO caching system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFOCache for FIFO cache system"""
    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """Assign value to the given key"""
        if key is None or item is None:
            return
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                keys = self.cache_data.keys()
                f_key = ''
                for i, k in enumerate(keys):
                    if i == 0:
                        f_key = k
                        break
                if key not in keys:
                    del self.cache_data[f_key]
                    print(f"DISCARD {f_key}")

                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """Get value for a given key"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None
