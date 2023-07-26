#!/usr/bin/env python3
"""
Implementation of a basic caching system with MRU
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching"""

    def __init__(self):
        """MRU Constructor"""
        super().__init__()
        self.keys_orders = []

    def _add_element(self, key, value):
        """
            Add an element to cache system and save the key
            to keep the cache order level
        """
        if key in self.keys_orders:
            self.keys_orders.remove(key)

        self.keys_orders.append(key)
        self.cache_data[key] = value

    def put(self, key, value):
        """add a value in the caching system"""
        if not key or not value:
            return

        if self.cache_data.get(key):
            self._add_element(key, value)
            return

        keys = list(self.cache_data.keys())
        if len(keys) == BaseCaching.MAX_ITEMS:
            remove_key = self.keys_orders[-1]
            self.keys_orders.pop(-1)
            print('DISCARD: {}'.format(remove_key))
            del self.cache_data[remove_key]
            self._add_element(key, value)
            return

        self._add_element(key, value)

    def get(self, key):
        """Retrieve a value"""
        if not key:
            return None

        el = self.cache_data.get(key)
        if not el:
            return None

        # Reorder the keys
        self.keys_orders.remove(key)
        self.keys_orders.append(key)
        return self.cache_data.get(key)
