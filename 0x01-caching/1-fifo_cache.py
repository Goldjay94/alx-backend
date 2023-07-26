#!/usr/bin/env python3
"""
Implementation of a basic caching system with FIFO
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that inherits from BaseCaching
    and is a caching system"""
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS\
                    and key not in self.cache_data.keys():
                key_to_discard = list(self.cache_data.keys())[0]
                del self.cache_data[key_to_discard]
                print(f"DISCARD: {key_to_discard}")
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
