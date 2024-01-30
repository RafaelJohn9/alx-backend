#!/usr/bin/env python3
"""
module that contains a cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
   cache using LFU algorithm
    """
    def __init__(self):
        """
        contains attr of this cache
        """
        super().__init__()
        self.__mru = {}

    def put(self, key, item):
        """
        adds an item in the cache
        """
        if key is None or item is None:
            return

        if self.cache_data.get(key, None):
            self.__mru[key] += 1
            del(self.cache_data[key])
        else:
            self.__mru[key] = 1

        self.cache_data[key] = item
        max_items = BaseCaching.MAX_ITEMS
        if len(self.cache_data.keys()) > max_items:
            delete_item_key = self.__lfu()
            print(f"DISCARD: {delete_item_key}")
            del(self.cache_data[delete_item_key])
            del(self.__mru[delete_item_key])

    def get(self, key):
        """
        gets an item using key
        """
        if self.cache_data.get(key, None):
            self.__mru[key] += 1
            return self.cache_data[key]

        return None

    def __lfu(self):
        """
        least recently used algorithm
        updates mru list
        """
        minimum_value = min(list(self.__mru.values())[:-1])
        print(self.__mru)
        for key, value in self.__mru.items():
            if value == minimum_value:
                return key
