import unittest
from solution import BulbSwitcher

class BulbSwitcherTests(unittest.TestCase):
    def setUp(self):
        self.sut = BulbSwitcher()

    def test1(self):
        self.assertEqual(1, self.sut.solve(3))

    def test2(self):
        self.assertEqual(2, self.sut.solve(4))

    def test3(self):
        self.assertEqual(1, self.sut.solve(2))

    def test4(self):
         self.assertEqual(1, self.sut.solve(1))

if __name__ == '__main__':
    unittest.main()