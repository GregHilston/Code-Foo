import unittest
from solution import CountingBits

class CountingBitsTests(unittest.TestCase):
    def setUp(self):
        self.sut = CountingBits()

    def test1(self):
        self.assertEqual([0, 1, 1], self.sut.solve(2))

    def test2(self):
        self.assertEqual([0, 1, 1, 2, 1, 2], self.sut.solve(5))

if __name__ == '__main__':
    unittest.main()