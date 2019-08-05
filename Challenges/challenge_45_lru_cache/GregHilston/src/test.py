"""Greg Hilston's test code solution to Code Foo challenge 44."""

import unittest
from typing import Dict
from solution import LRUCache


class LRUCacheTests(unittest.TestCase):

    """Tests LRUCache."""

    def setUp(self):
        """Set up our SUT for testing."""
        self.sut = LRUCache(capacity=2)

    def test_basic(self):
        """Test using as basic as possible, with valid empty input."""
        self.assertEqual(
            None,
            self.sut.put(1, 1)
        )
        self.assertEqual(
            None,
            self.sut.put(2, 2)
        )
        self.assertEqual(
            1,
            self.sut.get(1)
        )
        self.assertEqual(
            None,
            self.sut.put(3, 3)
        )
        self.assertEqual(
            -1,
            self.sut.get(2)
        )
        self.assertEqual(
            None,
            self.sut.put(4, 4)
        )
        self.assertEqual(
            -1,
            self.sut.get(1)
        )
        self.assertEqual(
            3,
            self.sut.get(3)
        )
        self.assertEqual(
            4,
            self.sut.get(4)
        )


if __name__ == '__main__':
    unittest.main()
