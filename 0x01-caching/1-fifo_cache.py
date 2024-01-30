#!/usr/bin/env python3
"""
module that contains a cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    cache using FIFO algorithm
    """
    def __init__(self):
        """
        contains attr of this cache
        """
        super().__init__()

    def put(self, key, item):
        """
        adds an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        max_items = BaseCaching.MAX_ITEMS
        if len(self.cache_data.keys()) > max_items:
            delete_item_key = list(self.cache_data.keys())[0]
            print(f"DISCARD: {delete_item_key}")
            del(self.cache_data[delete_item_key])

    def get(self, key):
        """
        gets an item using key
        """
        return self.cache_data[key] if self.cache_data.get(key, None) else None
