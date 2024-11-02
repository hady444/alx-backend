#!/usr/bin/python3
from base_caching import BaseCaching
"""
Module
"""


class BasicCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """
        add item cached
        """
        if key and item:
            self.cache_data[key] = item
    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
