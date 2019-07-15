"""Greg Hilston's test code solution to Code Foo challenge 44."""

import unittest
from typing import Dict
from solution import IntermediateSales


class IntermediateSalesTests(unittest.TestCase):

    """Tests IntermediateSales."""

    def setUp(self):
        """Set up our SUT for testing."""
        self.sut = IntermediateSales()

    def test0(self):
        """Test using as basic as possible, with valid empty input."""
        revenue: Dict[str, Dict[str, int]] = {
        }
        expenses: Dict[str, Dict[str, int]] = {
        }
        expected_output = {
        }

        self.assertEqual(
            expected_output,
            self.sut.solve(
                revenue,
                expenses
            )
        )

    def test_basic(self):
        """Test using basic input."""
        revenue: Dict[str, Dict[str, int]] = {
            "Frank": {
                "Tea": 120,
                "Coffee": 243
            },
            "Jane": {
                "Tea": 145,
                "Coffee": 265
            }
        }
        expenses: Dict[str, Dict[str, int]] = {
            "Frank": {
                "Tea": 130,
                "Coffee": 143
            },
            "Jane": {
                "Tea": 59,
                "Coffee": 198
            }
        }
        expected_output = {
            "Frank": 6.20,
            "Jane": 9.49
        }

        self.assertEqual(
            expected_output,
            self.sut.solve(
                revenue,
                expenses
            )
        )

    def test_challenge(self):
        """Test using a challenging input."""
        revenue: Dict[str, Dict[str, int]] = {
            "Johnver": {
                "Tea": 190,
                "Coffee": 325,
                "Water": 682,
                "Milk": 829
            },
            "Vanston": {
                "Tea": 140,
                "Coffee": 19,
                "Water": 14,
                "Milk": 140
            },
            "Danbree": {
                "Tea": 1926,
                "Coffee": 293,
                "Water": 852,
                "Milk": 609
            },
            "Vansey": {
                "Tea": 14,
                "Coffee": 1491,
                "Water": 56,
                "Milk": 120
            },
            "Mundyke": {
                "Tea": 143,
                "Coffee": 162,
                "Water": 659,
                "Milk": 87
            }
        }
        expenses: Dict[str, Dict[str, int]] = {
            "Johnver": {
                "Tea": 120,
                "Coffee": 300,
                "Water": 50,
                "Milk": 67
            },
            "Vanston": {
                "Tea": 65,
                "Coffee": 10,
                "Water": 299,
                "Milk": 254
            },
            "Danbree": {
                "Tea": 890,
                "Coffee": 23,
                "Water": 1290,
                "Milk": 89
            },
            "Vansey": {
                "Tea": 54,
                "Coffee": 802,
                "Water": 12,
                "Milk": 129
            },
            "Mundyke": {
                "Tea": 430,
                "Coffee": 235,
                "Water": 145,
                "Milk": 76
            }
        }
        expected_output = {
            "Johnver": 92.32,
            "Vanston": 5.21,
            "Danbree": 113.21,
            "Vansey": 45.45,
            "Mundyke": 3.552
        }

        self.assertDictEqual(
            expected_output,
            self.sut.solve(
                revenue,
                expenses
            )
        )


if __name__ == '__main__':
    unittest.main()
