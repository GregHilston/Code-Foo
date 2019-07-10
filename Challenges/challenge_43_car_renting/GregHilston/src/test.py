"""Greg Hilston's test code solution to Code Foo challenge 43."""

import unittest
from solution import CarRenting


class CarRentingTests(unittest.TestCase):

    """Tests CarRenting."""

    def setUp(self):
        """Set up our SUT for testing."""
        self.sut = CarRenting()

    def test1(self):
        """Test using default input/output given by challenge online."""
        self.assertEqual(
            (
                5,
                [
                    (5, 10), (13, 25), (30, 35), (40, 66), (70, 100)
                ]
            ),
            self.sut.solve(
                10,
                [
                    1, 12, 5, 12, 13, 40, 30, 22, 70, 19
                ],
                [
                    23, 10, 10, 29, 25, 66, 35, 33, 100, 6
                ]
            )
        )


if __name__ == '__main__':
    unittest.main()
