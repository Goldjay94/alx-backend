#!/usr/bin/env python3
"""
Implementation of a basic caching system with MRU
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that inherits from BaseCaching
    and is a caching system"""
    def __init__(self) -> None:
        super().__init__()
        self.__access = {}

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS\
                    and key not in self.cache_data.keys():
                key_to_discard = self.get_lrk()
                del self.cache_data[key_to_discard]
                del self.__access[key_to_discard]
                print(f"DISCARD: {key_to_discard}")
            if key not in self.cache_data:
                self.__access[key] = datetime.now()
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            if key in self.__access:
                self.__access[key] = datetime.now()
            return self.cache_data[key]
        return None

    def get_lrk(self):
        """Get the least requested key"""
        keys = list(self.__access.keys())
        lrk = 0
        # print(keys)
        for i in range(1, len(keys)):
            if self.__access[keys[lrk]] < self.__access[keys[i]]:
                lrk = i
        return keys[lrk]
