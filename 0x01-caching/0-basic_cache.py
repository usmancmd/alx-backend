#!/usr/bin/env python3
"""Caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class BasicCache for basic caching"""
    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """Assign value for a given key"""
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get value of a given key"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None
