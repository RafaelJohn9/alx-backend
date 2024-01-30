#!/usr/bin/env python3
"""
a class BasicCache that inherits from baseCaching
and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    a class that acts as a caching system
    """
    def put(self, key, item):
        """
        used to add an item to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        gets an item using key
        """
        return self.cache_data[key] if self.cache_data.get(key, None) else None
