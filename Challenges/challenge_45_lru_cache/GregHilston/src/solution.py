"""Greg Hilston's source code solution to Code Foo challenge 45."""

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
        self.cache: Dict[int, int] = {}

    def get(self, key: int) -> int:
        """Fetch value by key.

        Args:
            key: key to lookup

        Returns:
            Value found or -1 if not found

        """
        return -1

    def put(self, key: int, value: int) -> None:
        """Put value by key into cache.

        Args:
            key: Store by
            value: Actual value to store

        Returns:
            None

        """
        return None
