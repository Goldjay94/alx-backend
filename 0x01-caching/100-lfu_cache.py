#!/usr/bin/env python3
"""
create a class LFUCache that inherits from BaseCaching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU caching system
    """

    def __init__(self):
        super().__init__()
        self.keys_weight = {}

    def _add_element(self, key, value):
        """
            Add an element to cache system
        """
        self._handle_usage(key)
        self.cache_data[key] = value

    def _handle_usage(self, key):
        """
            Increase the usage weight for a particular element
        """
        if not self.keys_weight.get(key):
            self.keys_weight[key] = 0

        self.keys_weight[key] += 1

    def _get_remove_key(self):
        """
            Calculates the key that could be removed from the weight list
        """
        min_value = {'key': None, 'weight': 0}
        for key, weight in self.keys_weight.items():
            if not min_value['key'] or weight < min_value['weight']:
                min_value = {'key': key, 'weight': weight}

        return min_value['key']

    def put(self, key, value):
        """add a value in the caching system"""
        if not key or not value:
            return

        if self.cache_data.get(key):
            self._add_element(key, value)
            return

        keys = list(self.cache_data.keys())
        if len(keys) == BaseCaching.MAX_ITEMS:
            remove_key = self._get_remove_key()
            print('DISCARD: {}'.format(remove_key))
            del self.cache_data[remove_key]
            del self.keys_weight[remove_key]
            self._add_element(key, value)
            return

        self._add_element(key, value)

    def get(self, key):
        """Retrieve a value from the caching system"""
        if not key:
            return None

        el = self.cache_data.get(key)
        if not el:
            return None

        self._handle_usage(key)
        return self.cache_data.get(key)
