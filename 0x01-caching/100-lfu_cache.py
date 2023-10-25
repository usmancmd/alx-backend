#!/usr/bin/env python3
"""LFU Cache system"""

from collections import defaultdict
from datetime import datetime
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Cache class"""
    def __init__(self):
        """init method"""
        super().__init__()
        # Track the usage frequency of each key
        self.frequency = defaultdict(int)
        # Track the access time of each key
        self.access_time = {}

    def put(self, key, item):
        """Assign item for a given key"""
        if key is None or item is None:
            return

        # Check if cache is at maximum capacity
        if len(self.cache_data) >= self.MAX_ITEMS:
            least_frequency = min(self.frequency.values())

            # Find all keys with the least frequency
            least_frequent_keys = [k
                                   for k, v in self.frequency.items()
                                   if v == least_frequency]

            if len(least_frequent_keys) == 1:
                discarded_key = least_frequent_keys[0]
            else:
                discarded_key = min(least_frequent_keys,
                                    key=lambda k: self.access_time[k])

            self.frequency.pop(discarded_key)
            self.access_time.pop(discarded_key)
            self.cache_data.pop(discarded_key)
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item
        self.frequency[key] += 1
        self.access_time[key] = datetime.now()

    def get(self, key):
        """Get value for a given key"""
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.access_time[key] = datetime.now()
        return self.cache_data[key]
