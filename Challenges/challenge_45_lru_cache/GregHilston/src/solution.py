"""Greg Hilston's source code solution to Code Foo challenge 45."""

import sys

from math import ceil

from typing import Dict
from dataclasses import dataclass


class LRUCache:

    """Implements a LRU Cache."""

    def __init__(self, capacity: int):
        """Initialize LUR cache with specific capacity.

        args:
            capacity: capacity

        """
        self.capacity = capacity
        self.cache: Dict[int, [int, int]] = {}
        self.fake_time_stamp = 0

    def get(self, key: int) -> int:
        """Fetch value by key.

        Args:
            key: key to lookup

        Returns:
            Value found or -1 if not found

        """
        if key in self.cache:
            self.fake_time_stamp += 1
            self.cache[key][0] = self.fake_time_stamp
            return self.cache[key][1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """Put value by key into cache.

        Args:
            key: Store by
            value: Actual value to store

        Returns:
            None

        """
        self.fake_time_stamp += 1
        oldest_key = -1
        oldest_fake_time_stamp = sys.maxsize

        if len(self.cache.keys()) < self.capacity:
            self.cache[key] = [self.fake_time_stamp, value]
        else:
            for k, v in self.cache.items():
                if v[0] < oldest_fake_time_stamp:
                    oldest_key = k
                    oldest_fake_time_stamp = v[0]
            # found who were replacing
            self.cache.pop(oldest_key)
            self.cache[key] = [self.fake_time_stamp, value]
        return None
