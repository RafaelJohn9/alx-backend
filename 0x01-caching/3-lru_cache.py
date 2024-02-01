#!/usr/bin/env python3
"""
module that contains a cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    cache using LRU algorithm
    """
    def __init__(self):
        """
        contains attr of this cache
        """
        super().__init__()
        self.__mru = []

    def put(self, key, item):
        """
        adds an item in the cache
        """
        if key is None or item is None:
            return

        if self.cache_data.get(key, None):
            del(self.cache_data[key])

        self.__update_mru(key)
        self.cache_data[key] = item
        max_items = BaseCaching.MAX_ITEMS
        if len(self.cache_data.keys()) > max_items:
            delete_item_key = self.__mru[0]
            print(f"DISCARD: {delete_item_key}")
            del(self.cache_data[delete_item_key])
            del(self.__mru[self.__mru.index(delete_item_key)])

    def get(self, key):
        """
        gets an item using key
        """
        if self.cache_data.get(key, None):
            self.__update_mru(key)
            return self.cache_data[key]

        return None

    def __update_mru(self, key):
        """
        least recently used algorithm
        updates mru list
        """
        if key in self.__mru:
            del(self.__mru[self.__mru.index(key)])
        self.__mru.append(key)
